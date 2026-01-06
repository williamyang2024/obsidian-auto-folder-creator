Obsidian Folder Structure Generator - 一键生成自定义Obsidian仓库文件夹结构

A lightweight Python script to automatically create a standardized, customizable folder structure for Obsidian vaults. Eliminate manual folder creation and ensure consistency across multiple Obsidian repositories.

（轻量级Python脚本，自动为Obsidian仓库创建标准化、可自定义的文件夹结构，告别手动创建文件夹的繁琐，确保多仓库文件夹结构统一。）

核心功能
- ✅ 开箱即用的默认结构：内置符合Obsidin最佳实践的文件夹模板（如Inbox、Notes、Projects、Resources等）
- ✅ 高度自定义：通过JSON配置文件轻松修改/扩展文件夹层级，适配个人/团队的笔记管理习惯
- ✅ 跨平台兼容：支持Windows/macOS/Linux，无需额外依赖
- ✅ 安全���侵入：仅创建空文件夹，不修改/删除任何现有文件，可放心在已有仓库中使用
- ✅ 一键执行：单命令快速生成结构，支持指定仓库路径，无需复杂配置
- ✅ 注释清晰：代码模块化设计，新手可轻松理解/二次开发

快速开始
1. 安装依赖
```bash
# 无额外依赖（仅使用Python内置库）
git clone https://github.com/你的用户名/obsidian-folder-structure-generator.git
cd obsidian-folder-structure-generator
```

2. 基本使用
```python
# 方式1：使用默认结构生成（生成到当前目录的Obsidian Vault）
python obsidian_folder_generator.py

# 方式2：指定自定义仓库路径
python obsidian_folder_generator.py --path "/Users/xxx/Documents/My Obsidian Vault"

# 方式3：使用自定义配置文件
python obsidian_folder_generator.py --config custom_structure.json
```

3. 自定义文件夹结构
创建`custom_structure.json`配置文件，按以下格式定义层级（支持无限嵌套）：
```json
{
  "000-Inbox": [],
  "100-Work": [
    "101-Calendar",
    "102-Projects",
    "103-Meeting Notes"
  ],
  "200-Learning": [
    "201-Computer Science",
    "202-Reading Notes",
    "203-Study Plans"
  ],
  "300-Life": [
    "301-Travel",
    "302-Finance",
    "303-Hobbies"
  ],
  "900-Resources": [
    "901-Templates",
    "902-Plugins",
    "903-Images"
  ]
}
```

默认文件夹结构说明
生成的默认结构参考Obsidian社区最佳实践，兼顾个人笔记/工作场景：

Obsidian Vault/
├── 000-Inbox          # 临时收集箱
├── 100-Work           # 工作相关
│   ├── 101-Calendar   # 日程/待办
│   ├── 102-Projects   # 项目管理
│   └── 103-Operation  # 日常运营
├── 200-Learning       # 学习成长
│   ├── 201-Reading    # 阅读笔记
│   ├── 202-Computer   # 技术学习
│   └── 203-Language   # 语言学习
├── 300-Life           # 生活管理
│   ├── 301-Travel     # 旅行规划
│   ├── 302-Finance    # 理财记录
│   └── 303-Hobbies    # 兴趣爱好
└── 900-Resources      # 资源库
    ├── 901-Templates  # 笔记模板
    ├── 902-Images     # 图片素材
    └── 903-Plugins    # 插件配置

注意事项
1. 脚本仅创建空文件夹，不会覆盖/修改现有文件；
2. 支持Python 3.6+版本，无需安装第三方库；
3. 若指定的仓库路径不存在，脚本会自动创建该目录；
4. 可结合Obsidian插件（如Auto Note Mover）实现后续笔记自动归档。

许可证
MIT License - 自由使用、修改、分发，商用/非商用均可。

贡献指南
欢迎提交Issue/PR优化功能：
- 新增默认文件夹模板
- 支持更多配置格式（YAML/TOML）
- 增加批量生成多仓库结构的功能
