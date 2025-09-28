# 定义默认版本号
VERSION ?= dev

# 定义目标平台
PLATFORMS := darwin-arm64 windows-amd64

# 定义构建目录前缀
BUILD_ROOT := build/*
BUILD_DIR := build/PCR-$(VERSION)

# 定义二进制名称
BINARY_NAME := PCR-Gen

# 定义默认目标
.PHONY: all
all: build

# 构建所有平台
.PHONY: build
build: clean $(PLATFORMS)
	git tag -a $(VERSION) -m "Release version $(VERSION)" || true
	git push origin $(VERSION) || true

# 为每个平台定义构建规则
.PHONY: $(PLATFORMS)
$(PLATFORMS):
	@echo "Building for $@..."
	@mkdir -p $(BUILD_DIR)
	@GOOS=$(word 1,$(subst -, ,$@)) \
	 GOARCH=$(word 2,$(subst -, ,$@)) \
	 go build -ldflags "-X main.Version=$(VERSION)" -o $(BUILD_DIR)/$(BINARY_NAME)-$(VERSION)-$@$(if $(filter windows-%,$@),.exe,)

# 清理构建目录
.PHONY: clean
clean:
	@echo "Cleaning build directory..."
	@rm -rf $(BUILD_ROOT)

# 运行
.PHONY: run
run:
	@echo "Running $(BINARY_NAME)..."
	@go mod tidy
	@go run main.go