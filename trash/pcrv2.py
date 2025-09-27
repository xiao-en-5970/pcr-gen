#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PCRv2 Script Generator
根据Excel文件自动生成PCR脚本
基于D1-松鼠水花似似花真步江雪-8365w.xlsx数据
"""

import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def load_axis_data(excel_file):
    """加载轴模板数据"""
    try:
        # 读取轴模板数据，从第9行开始作为表头
        df_axis = pd.read_excel(excel_file, sheet_name='轴模板', header=9)
        df_axis = df_axis.iloc[:, :9]  # 只取前9列有用的数据
        df_axis.columns = ['帧数', '秒数', '角色', '操作', 'col4', 'col5', '伤害', 'ub总伤', '说明']
        
        # 过滤有效数据行（帧数不为空且为数字）
        valid_rows = df_axis.dropna(subset=['帧数'])
        valid_rows = valid_rows[pd.to_numeric(valid_rows['帧数'], errors='coerce').notna()]
        
        return valid_rows[['帧数', '角色', '操作']]
    except Exception as e:
        print(f"Error loading axis data: {e}")
        return None

def load_tp_mapping(excel_file):
    """加载TP变化数据，创建逻辑帧到渲染帧的映射"""
    try:
        df_tp = pd.read_excel(excel_file, sheet_name='TP变化', header=2)
        df_tp.columns = ['逻辑帧', '渲染帧', '角色1', '角色2', '角色3', '角色4', '角色5'] + ['col' + str(i) for i in range(7, len(df_tp.columns))]
        
        # 创建逻辑帧到渲染帧的映射，支持一个逻辑帧对应多个渲染帧
        frame_mapping = {}
        for _, row in df_tp.iterrows():
            if pd.notna(row['逻辑帧']) and pd.notna(row['渲染帧']):
                frame = int(row['逻辑帧'])
                render_frame = int(row['渲染帧'])
                
                if frame not in frame_mapping:
                    frame_mapping[frame] = []
                
                # 避免重复添加相同的渲染帧
                if render_frame not in frame_mapping[frame]:
                    frame_mapping[frame].append(render_frame)
        
        # 对每个逻辑帧的渲染帧列表进行排序
        for frame in frame_mapping:
            frame_mapping[frame].sort()
        
        return frame_mapping
    except Exception as e:
        print(f"Error loading TP mapping: {e}")
        return {}

def select_render_frames(render_frames, operation_count, operation_type):
    """根据操作类型和数量选择合适的渲染帧"""
    if not render_frames:
        return [0] * operation_count
    
    # 对于UB操作，使用第一个渲染帧3次（减速、UB、加速）
    if operation_type == 'UB':
        if len(render_frames) >= 1:
            return [render_frames[0]] * 3
        else:
            return [render_frames[0]] * 3
    
    # 对于AUTO操作，使用第一个渲染帧3次（AUTO开、AUTO关、其他操作）
    elif operation_type == 'AUTO':
        if len(render_frames) >= 1:
            return [render_frames[0]] * 3
        else:
            return [render_frames[0]] * 3
    
    # 对于连点操作，根据基准脚本的选择模式
    else:
        if len(render_frames) == 1:
            return [render_frames[0]] * operation_count
        
        # 基准脚本的选择模式：基于实际观察到的精确模式
        selected = []
        
        # 总是选择第一个渲染帧
        if operation_count > 0:
            selected.append(render_frames[0])
        
        # 根据操作数量选择其他渲染帧，基于基准脚本的实际模式
        if operation_count > 1:
            # 对于2个操作：选择第1个和第3个渲染帧（间隔2）
            if len(render_frames) >= 3:
                selected.append(render_frames[2])
            elif len(render_frames) >= 2:
                selected.append(render_frames[1])
            else:
                selected.append(render_frames[0])
        
        if operation_count > 2:
            # 对于3个操作：选择第1个、第3个、第4个渲染帧
            if len(render_frames) >= 4:
                selected.append(render_frames[3])
            elif len(render_frames) >= 3:
                selected.append(render_frames[2])
            else:
                selected.append(render_frames[-1])
        
        if operation_count > 3:
            # 对于4个操作：选择第1个、第2个、第4个渲染帧
            if len(render_frames) >= 4:
                selected.append(render_frames[3])
            elif len(render_frames) >= 3:
                selected.append(render_frames[2])
            else:
                selected.append(render_frames[-1])
        
        if operation_count > 4:
            # 对于5个操作：选择第1个、第1个、第1个、第2个、第4个渲染帧
            if len(render_frames) >= 4:
                selected.append(render_frames[3])
            elif len(render_frames) >= 3:
                selected.append(render_frames[2])
            else:
                selected.append(render_frames[-1])
        
        # 如果还需要更多渲染帧，重复使用最后一个
        while len(selected) < operation_count:
            selected.append(render_frames[-1])
        
        return selected[:operation_count]

def generate_script_content(axis_data, frame_mapping):
    """根据轴模板数据和帧映射生成脚本内容"""
    
    # 脚本头部
    script_content = """from autotimeline import *
import sys
sys.path.append('.')

print("minitouch 连接中")
minitouch.connect("127.0.0.1", 1111)
max_x = minitouch.getMaxX()
max_y = minitouch.getMaxY()
minitouch.setPos("暂停", int(max_x * 0.94), int(max_y * 0.05))
minitouch.setPos("SET", int(max_x * 0.95), int(max_y * 0.64))
minitouch.setPos("AUTO", int(max_x * 0.95), int(max_y * 0.76))
minitouch.setPos("SPEED", int(max_x * 0.95), int(max_y * 0.9))
print("松鼠 定位中")
minitouch.setPos("松鼠", int(max_x * 0.74), int(max_y * 0.8))
print("水花 定位中")
minitouch.setPos("水花", int(max_x * 0.62), int(max_y * 0.8))
print("普花 定位中")
minitouch.setPos("普花", int(max_x * 0.5), int(max_y * 0.8))
print("真步 定位中")
minitouch.setPos("真步", int(max_x * 0.38), int(max_y * 0.8))
print("江雪 定位中")
minitouch.setPos("江雪", int(max_x * 0.26), int(max_y * 0.8))
print("解除暂停，塔塔开!")

autopcr.setOffset(2, 0); # offset calibration
autopcr.waitFrame(autopcr.getFrame() + 50); minitouch.press("SPEED") #加速
"""
    
    # 角色名称映射
    char_mapping = {
        '松鼠': '松鼠',
        '水花': '水花', 
        '似似花': '普花',  # 似似花在脚本中对应普花
        '真步': '真步',
        '江雪': '江雪'
    }
    
    # 按帧数分组，处理同一帧的多个操作，保持原始顺序
    grouped_operations = {}
    for _, row in axis_data.iterrows():
        frame = int(row['帧数'])
        character = row['角色']
        operation = row['操作']
        
        # 跳过BOSS UB行和无效操作
        if character == 'BOSS  UB' or pd.isna(operation):
            if character == 'BOSS  UB':
                grouped_operations[frame] = [('BOSS_UB', None)]
            continue
            
        if frame not in grouped_operations:
            grouped_operations[frame] = []
        grouped_operations[frame].append((character, operation))
    
    # 按帧数排序生成操作序列
    sorted_frames = sorted(grouped_operations.keys())
    
    for frame in sorted_frames:
        operations = grouped_operations[frame]
        
        # 处理BOSS UB标记
        if operations == [('BOSS_UB', None)]:
            script_content += f"#BOSS  UB\n"
            continue
        
        # 分析操作类型
        has_ub = False  # 是否有UB操作（押技能）
        has_auto = False  # 是否有AUTO操作
        normal_ops = []  # 普通连点操作
        
        for character, operation in operations:
            if operation == 'AUTO':
                has_auto = True
            elif '押' in str(operation) or '连点后' in str(operation) or 'BOSS唱名后' in str(operation):
                # 识别UB操作：包含"押"字，或者包含"连点后"、"BOSS唱名后"等特殊描述
                has_ub = True
                ub_char = char_mapping.get(character, character)
            else:
                normal_ops.append(char_mapping.get(character, character))
        
        # 获取渲染帧列表
        render_frames = frame_mapping.get(frame, [frame])
        if not render_frames:
            render_frames = [frame]
        
        # 生成代码 - 按照操作在Excel中的顺序处理
        if has_ub:
            # UB操作需要减速，使用第一个渲染帧
            render_frame = render_frames[0]
            script_content += f"autopcr.waitFrame({render_frame} - 60); minitouch.press(\"SPEED\") #减速 lframe {frame}\n"
            script_content += f"autopcr.waitFrame({render_frame}); minitouch.press(\"{ub_char}\") # lframe {frame}\n"
            script_content += f"autopcr.waitFrame({render_frame} + 30); minitouch.press(\"SPEED\") #加速 lframe {frame}\n"
            # 处理同帧的其他操作，按照原始顺序，使用智能选择的渲染帧
            normal_ops = [char_mapping.get(character, character) for character, operation in operations 
                         if character != ub_char and operation != 'AUTO' and '押' not in str(operation) and '连点后' not in str(operation) and 'BOSS唱名后' not in str(operation)]
            if normal_ops:
                selected_frames = select_render_frames(render_frames, len(normal_ops), 'NORMAL')
                for i, char in enumerate(normal_ops):
                    render_frame = selected_frames[i] if i < len(selected_frames) else selected_frames[-1]
                    script_content += f"autopcr.waitFrame({render_frame} - 45); minitouch.press(\"{char}\") #连点 lframe {frame}\n"
        elif has_auto:
            # AUTO操作，使用第一个渲染帧
            render_frame = render_frames[0]
            script_content += f"autopcr.waitFrame({render_frame} - 45); minitouch.press(\"AUTO\") #AUTO开 lframe {frame}\n"
            script_content += f"#AUTO\n"
            script_content += f"autopcr.waitFrame({render_frame} + 10); minitouch.press(\"AUTO\") #AUTO关 lframe {frame}\n"
            # 处理同帧的其他操作，按照原始顺序，使用智能选择的渲染帧
            normal_ops = [char_mapping.get(character, character) for character, operation in operations 
                         if operation != 'AUTO' and '押' not in str(operation)]
            if normal_ops:
                selected_frames = select_render_frames(render_frames, len(normal_ops), 'NORMAL')
                for i, char in enumerate(normal_ops):
                    render_frame = selected_frames[i] if i < len(selected_frames) else selected_frames[-1]
                    script_content += f"autopcr.waitFrame({render_frame} - 45); minitouch.press(\"{char}\") #连点 lframe {frame}\n"
        else:
            # 纯连点操作，按照原始顺序，使用智能选择的渲染帧
            normal_ops = [char_mapping.get(character, character) for character, operation in operations 
                         if '押' not in str(operation)]
            if normal_ops:
                selected_frames = select_render_frames(render_frames, len(normal_ops), 'NORMAL')
                for i, char in enumerate(normal_ops):
                    render_frame = selected_frames[i] if i < len(selected_frames) else selected_frames[-1]
                    script_content += f"autopcr.waitFrame({render_frame} - 45); minitouch.press(\"{char}\") #连点 lframe {frame}\n"
    
    # 脚本结尾
    if sorted_frames:
        last_frame = sorted_frames[-1]
        last_render_frames = frame_mapping.get(last_frame, [last_frame])
        if last_render_frames:
            last_render_frame = last_render_frames[-1]  # 使用最后一个渲染帧
        else:
            last_render_frame = last_frame
        script_content += f"autopcr.waitFrame({last_render_frame + 100} - 60); minitouch.press(\"暂停\") #暂停\n\n"
    
    script_content += "#日志：\n"
    script_content += "#v3:添加了最后暂停\n"
    script_content += "#v4:引入auto，修改set提前量S\n"
    script_content += "#v5:基于Excel数据自动生成，使用逻辑帧到渲染帧映射\n"
    
    return script_content

class PCRv2GUI:
    """PCRv2 图形用户界面"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("PCRv2 脚本生成器")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')
        
        self.excel_file = None
        self.setup_ui()
        
    def setup_ui(self):
        """设置用户界面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 标题
        title_label = ttk.Label(main_frame, text="PCRv2 脚本生成器", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Excel文件选择
        ttk.Label(main_frame, text="Excel文件:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.file_var = tk.StringVar()
        self.file_entry = ttk.Entry(main_frame, textvariable=self.file_var, width=50)
        self.file_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=5)
        
        self.browse_btn = ttk.Button(main_frame, text="浏览...", command=self.browse_file)
        self.browse_btn.grid(row=1, column=2, pady=5)
        
        # 输出文件名
        ttk.Label(main_frame, text="输出文件:").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.output_var = tk.StringVar(value="D1-松鼠水花似似花真步江雪-8365w变速v4_generated.py")
        self.output_entry = ttk.Entry(main_frame, textvariable=self.output_var, width=50)
        self.output_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=5)
        
        # 生成按钮
        self.generate_btn = ttk.Button(main_frame, text="生成脚本", 
                                      command=self.generate_script, style='Accent.TButton')
        self.generate_btn.grid(row=3, column=0, columnspan=3, pady=20)
        
        # 进度条
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # 状态标签
        self.status_var = tk.StringVar(value="请选择Excel文件")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var)
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # 日志文本框
        ttk.Label(main_frame, text="日志:").grid(row=6, column=0, sticky=tk.W, pady=(10, 5))
        
        # 创建文本框和滚动条
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.log_text = tk.Text(text_frame, height=10, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 配置主框架的行权重
        main_frame.rowconfigure(7, weight=1)
        
    def browse_file(self):
        """浏览并选择Excel文件"""
        file_path = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=[("Excel文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
        )
        
        if file_path:
            self.file_var.set(file_path)
            self.excel_file = file_path
            self.log_message(f"已选择文件: {os.path.basename(file_path)}")
            
            # 自动设置输出文件名
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_name = f"{base_name}_generated.py"
            self.output_var.set(output_name)
            
    def log_message(self, message):
        """添加日志消息"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def generate_script(self):
        """生成脚本"""
        if not self.excel_file or not os.path.exists(self.excel_file):
            messagebox.showerror("错误", "请先选择一个有效的Excel文件！")
            return
            
        # 开始生成
        self.generate_btn.config(state='disabled')
        self.progress.start()
        self.status_var.set("正在生成脚本...")
        self.log_text.delete(1.0, tk.END)
        
        try:
            self.log_message("开始加载Excel数据...")
            
            # 加载轴模板数据
            axis_data = load_axis_data(self.excel_file)
            if axis_data is None:
                raise Exception("无法加载轴模板数据！")
            
            self.log_message(f"已加载 {len(axis_data)} 个操作")
            
            # 加载TP映射
            frame_mapping = load_tp_mapping(self.excel_file)
            if not frame_mapping:
                raise Exception("无法加载TP映射数据！")
            
            self.log_message(f"已加载 {len(frame_mapping)} 个帧映射")
            
            # 生成脚本内容
            self.log_message("正在生成脚本内容...")
            script_content = generate_script_content(axis_data, frame_mapping)
            
            # 写入文件
            output_file = self.output_var.get()
            if not output_file:
                output_file = "generated_script.py"
                
            self.log_message(f"正在写入文件: {output_file}")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            self.log_message("脚本生成完成！")
            self.status_var.set(f"脚本已生成: {output_file}")
            
            # 显示成功消息
            messagebox.showinfo("成功", f"脚本已成功生成！\n文件位置: {os.path.abspath(output_file)}")
            
        except Exception as e:
            error_msg = f"生成脚本时出错: {str(e)}"
            self.log_message(error_msg)
            self.status_var.set("生成失败")
            messagebox.showerror("错误", error_msg)
            
        finally:
            self.progress.stop()
            self.generate_btn.config(state='normal')

def main():
    """主函数 - 启动GUI"""
    root = tk.Tk()
    app = PCRv2GUI(root)
    
    # 设置窗口图标（如果有的话）
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    # 启动GUI
    root.mainloop()

if __name__ == "__main__":
    main()