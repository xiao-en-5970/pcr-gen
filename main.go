package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/sqweek/dialog"
	"github.com/xuri/excelize/v2"
)

// TP变化参数
type TpChange struct {
	RenderFrame string  //渲染帧
	TpReturn    float64 //TP返还
	Reason      string  //TP变化原因，主要观察UB
	RoleName    string  //角色名字
}

// 轴模板参数
type AxisSheet struct {
	RoleName   string //角色名
	LogicFrame string //逻辑帧
	Operation  string //操作
	Time       string //时间
}

type Service struct {
	XlsxName     string                //文件名
	Axis         []AxisSheet           //轴模板
	Logic2Render map[string][]TpChange //逻辑帧对应TP变化
	SheetNames   []string              //表名
	RoleNamesMap map[string]bool       //角色Map，快速查找是否是可操作角色
	Sheet        map[string][][]string //表名 >> 表
	File         *excelize.File        //文件指针
	Roles        []string              //按顺序排列的角色
	Role2TpRe    map[string]float64    //角色对常规TP返还数的Map
	EndTime      string                //战斗结束
}

// 打开文件
func (s *Service) OpenXlsx(filename string) *excelize.File {
	file, err := excelize.OpenFile(filename)
	if err != nil {
		panic(err)
	}
	s.XlsxName = filename
	s.File = file
	return file
}

// 获取所有表
func (s *Service) GetAllSheets(file *excelize.File) []string {
	sheets := file.GetSheetList()
	return sheets
}

// 获取一个表所有行列
func (s *Service) GetRows(sheetName string) [][]string {
	rows, err := s.File.GetRows(sheetName)
	if err != nil {
		panic(err)
	}
	return rows
}

// 初始化表名 to 行列
func (s *Service) InitSheets(sheetNames []string) {
	s.SheetNames = sheetNames

	s.Sheet = make(map[string][][]string)
	for _, sheetName := range s.SheetNames {
		s.Sheet[sheetName] = s.GetRows(sheetName)

	}
}

// 初始化每个逻辑帧的轴并考虑boss情况
func (s *Service) InitAxis() {
	rows := s.Sheet["轴模板"]
	start := 0
	for i, row := range rows {
		if len(row) > 0 && row[0] == "帧数" {
			start = i + 1
			break
		}
	}
	s.Axis = make([]AxisSheet, 0, len(rows)-start+2)
	for i := start; i < len(rows); i++ {
		row := rows[i]
		if len(row) > 3 {
			s.Axis = append(s.Axis, AxisSheet{
				RoleName:   row[2],
				LogicFrame: row[0],
				Operation:  row[3],
				Time:       row[1],
			})
		} else if len(row) == 3 {
			s.Axis = append(s.Axis, AxisSheet{
				RoleName:   row[2],
				LogicFrame: row[0],
				Operation:  row[2],
				Time:       row[1],
			})
		}
	}
}

// 初始化TP变化中所有原因为UB的渲染帧
func (s *Service) InitRender() {
	s.Logic2Render = make(map[string][]TpChange) // 初始化一次
	rows := s.Sheet["TP变化"]
	for i, row := range rows {
		if i < 4 {
			continue
		}
		tpRe, err := strconv.ParseFloat(row[len(row)-2], 64)
		if err != nil {
			panic(err)
		}

		if len(row) <= len(rows[1])+1 && s.RoleNamesMap[rows[1][len(row)-2]] && row[len(row)-1] == "放UB" {
			//拿到开大之后常规返还TP，常规取最小
			if s.Role2TpRe[rows[1][len(row)-2]] == 0 || (s.Role2TpRe[rows[1][len(row)-2]] > tpRe && tpRe > 0) {
				s.Role2TpRe[rows[1][len(row)-2]] = tpRe
			}
			s.Logic2Render[row[0]] = append(s.Logic2Render[row[0]], TpChange{
				RenderFrame: row[1],
				TpReturn:    tpRe,
				Reason:      row[len(row)-1],
				RoleName:    rows[1][len(row)-2],
			})
		}
	}
	// 结束时间
	s.EndTime = rows[len(rows)-1][1]
}

// 初始化角色数据
func (s *Service) InitRoles() {
	rows := s.Sheet["基础数据"]
	start := 0
	s.RoleNamesMap = make(map[string]bool)
	s.Role2TpRe = make(map[string]float64)
	for i, row := range rows {
		if len(row) > 1 && row[1] == "角色名字" {
			start = i + 1
			break
		}

	}
	s.Roles = make([]string, 0, len(rows)-start+2)
	for i := start; i < len(rows); i++ {
		row := rows[i]
		if len(row) <= 1 || row[1] == "" {
			break
		}
		s.RoleNamesMap[row[1]] = true
		s.Roles = append(s.Roles, row[1])
	}
}

// 初始化主体
func NewService(filename string) *Service {
	s := &Service{}
	s.OpenXlsx(filename)
	s.InitSheets([]string{"轴模板", "TP变化", "基础数据"})
	s.InitRoles()
	s.InitAxis()
	s.InitRender()
	return s
}

// 移除builder最后两行
func (s *Service) RemoveLastTwoLines(builder *strings.Builder) {
	content := builder.String()
	lines := strings.Split(content, "\n")
	if len(lines) > 2 {
		builder.Reset()
		builder.WriteString(strings.Join(lines[:len(lines)-2], "\n"))
	} else {
		builder.Reset() // 如果行数不足两行，则清空
	}
}

// 生成模板python
func (s *Service) Gen() {
	b := strings.Builder{}
	b.WriteString(Prefix)
	//角色位置
	rolefix := 0.74
	for _, name := range s.Roles {
		b.WriteString(fmt.Sprintf(Poi, name, name, rolefix))
		rolefix -= 0.12 //位置修正
	}
	//暂停结束，开始打轴
	b.WriteString(UnPause)
	// 对于每个逻辑帧找到对应渲染帧
	renderFrame := "0"
	fix := 0
	for i, axis := range s.Axis {
		if axis.RoleName == "BOSS  UB" {
			b.WriteString(fmt.Sprintf(BossUB, axis.Time))
			continue
		}
		for _, r := range s.Logic2Render[axis.LogicFrame] {
			if r.RoleName == axis.RoleName && r.Reason == "放UB" && r.TpReturn <= s.Role2TpRe[axis.RoleName] {
				// 修正渲染帧不超过60的情况下释放顺序颠倒
				preF, err := strconv.Atoi(renderFrame)
				aftF, err := strconv.Atoi(r.RenderFrame)
				if err != nil {
					panic(err)
				}
				if i > 0 && s.Axis[i-1].Operation == "连点" && axis.Operation == "连点" && aftF-preF <= 60 {
					fix += 60
				} else {
					fix = 0
				}
				renderFrame = r.RenderFrame
				break
			}
		}
		//auto情况
		if axis.Operation == "AUTO" {
			b.WriteString(fmt.Sprintf(AUTO, renderFrame, axis.RoleName, axis.LogicFrame, axis.Time, renderFrame))
			continue
		}
		//单点变速
		if axis.Operation != "连点" {
			b.WriteString(fmt.Sprintf(Single, renderFrame, renderFrame, axis.RoleName, axis.LogicFrame, axis.Time, renderFrame))
		} else { //同渲染帧连点需修正
			if fix != 0 {
				b.WriteString(fmt.Sprintf(MutiFix, renderFrame, fix, axis.RoleName, axis.LogicFrame, axis.Time))
				continue
			} else {
				b.WriteString(fmt.Sprintf(Muti, renderFrame, axis.RoleName, axis.LogicFrame, axis.Time))
			}
		}
	}
	b.WriteString(fmt.Sprintf(Suffix, s.EndTime))
	// 写入 out.py 文件
	os.WriteFile("out.py", []byte(b.String()), 0644)
}

// 命令行参数
func GetArg() (in, out string, ok bool) {
	// 检查参数数量是否足够
	if len(os.Args) < 1 {
		fmt.Println("请提供两个参数")
		fmt.Println("用法: program <参数1> <参数2>")
		return "", "", false
	}

	// 获取参数
	arg1 := os.Args[1]
	arg2 := os.Args[2]
	return arg1, arg2, true
}
func main() {
	// 弹窗选择 xlsx 文件
	filePath, err := dialog.File().Filter("Excel文件", "xlsx").Title("请选择xlsx文件").Load()
	if err != nil {
		fmt.Println("未选择文件或发生错误:", err)
		return
	}
	service := NewService(filePath)
	service.Gen()
	fmt.Printf("%+#v\n", service.Logic2Render)
}

// 常量格式化
const (
	Prefix  = "from autotimeline import *\nimport sys\nsys.path.append('.')\n\nprint(\"minitouch 连接中\")\nminitouch.connect(\"127.0.0.1\", 1111)\nmax_x = minitouch.getMaxX()\nmax_y = minitouch.getMaxY()\nminitouch.setPos(\"暂停\", int(max_x * 0.94), int(max_y * 0.05))\nminitouch.setPos(\"SET\", int(max_x * 0.95), int(max_y * 0.64))\nminitouch.setPos(\"AUTO\", int(max_x * 0.95), int(max_y * 0.76))\nminitouch.setPos(\"SPEED\", int(max_x * 0.95), int(max_y * 0.9))\n"
	Poi     = "print(\"%s 定位中\")\nminitouch.setPos(\"%s\", int(max_x * %.2f), int(max_y * 0.8))\n"
	UnPause = "print(\"解除暂停，塔塔开!\")\n\nautopcr.setOffset(2, 0); # offset calibration\nautopcr.waitFrame(autopcr.getFrame() + 50); minitouch.press(\"SPEED\") #加速\n"
	Single  = "autopcr.waitFrame(%s - 120); minitouch.press(\"SPEED\") #减速\nautopcr.waitFrame(%s); minitouch.press(\"%s\") #lframe %s//time %s\nautopcr.waitFrame(%s + 30); minitouch.press(\"SPEED\") #加速 \n"
	Muti    = "autopcr.waitFrame(%s - 60); minitouch.press(\"%s\") #连点 lframe %s//time %s\n"
	MutiFix = "autopcr.waitFrame(%s - 60 + %d); minitouch.press(\"%s\") #连点 lframe %s//time %s\n"
	BossUB  = "#BOSS  UB//time %s\n"
	AUTO    = "autopcr.waitFrame(%s - 60); minitouch.press(\"AUTO\") #AUTO开\n# %s AUTO lframe %s//time %s\nautopcr.waitFrame(%s + 10); minitouch.press(\"AUTO\") #AUTO关\n"
	Suffix  = "autopcr.waitFrame(%s - 60); minitouch.press(\"暂停\") #暂停\n\n#日志：\n#v3:添加了最后暂停\n#v4:引入auto，修改set提前量S\n"
)
