# Hermes Skills - 网页文档学习技能集

这是一套用于Hermes Agent的技能集，专注于从网页和GitHub学习技术文档并建立知识库。

## 技能列表

### 1. web-documentation-reader
**阅读和提取网页技术文档、API文档、教程的结构化内容**

功能特点：
- 读取各类技术文档网站
- 提取Markdown文档
- 解析HTML结构化内容
- 提取代码示例
- 保存到知识库（Obsidian格式）

支持的文档平台：
- GitHub文档和Wiki
- Read the Docs
- 官方技术文档网站
- API参考文档

### 2. github-project-learner
**深入学习GitHub项目：README、文档、代码结构、Issues、Wiki**

功能特点：
- 获取项目基本信息和统计
- 读取README和所有文档
- 分析项目结构
- 获取依赖信息
- 分析Issues和讨论
- 批量学习多个项目

支持的功能：
- 项目元数据提取
- 文档自动下载
- 代码语言统计
- 贡献者分析
- Release信息获取

## 安装

将技能复制到Hermes技能目录：

```bash
# Linux/macOS
cp -r web-documentation-reader ~/.hermes/skills/research/
cp -r github-project-learner ~/.hermes/skills/research/

# Windows
copy web-documentation-reader %LOCALAPPDATA%\hermes\skills\research\
copy github-project-learner %LOCALAPPDATA%\hermes\skills\research\
```

## 使用示例

### 学习网页文档

```
请帮我学习这个文档网站的内容：https://docs.example.com
```

### 学习GitHub项目

```
去GitHub上学习snapcast/snapcast项目的架构和文档
```

### 批量学习

```
学习以下GitHub项目并建立知识库：
- snapcast/snapcast
- HEnquist/camilladsp
- mikebrady/shairport-sync
```

## 依赖

### Python包
```bash
pip install requests beautifulsoup4
```

### 系统工具
- curl
- git
- python3

## 配置

### GitHub API Token（可选）

为了避免API限流，建议配置GitHub Personal Access Token：

```bash
export GITHUB_TOKEN="your_token_here"
```

未认证：60次/小时  
已认证：5000次/小时

## 输出格式

所有学到的内容都会保存为Markdown格式，包含：

- 元数据（来源、日期、标签）
- 结构化内容
- 代码示例
- 链接和引用

适合导入到Obsidian等知识管理工具。

## 实际应用案例

我使用这些技能从GitHub学习了嵌入式音频相关的知识，并建立了完整的知识库：

1. **Snapcast多房间音频同步系统** - 学习了工作原理、架构设计、配置方法
2. **A133音频系统** - 整理了完整的服务架构和配置
3. **PulseAudio音频路由** - 理解了核心概念和蓝牙路由机制
4. **ALSA Loopback** - 掌握了虚拟声卡的工作原理

## 贡献

欢迎提交Issue和Pull Request来改进这些技能！

## 许可证

MIT License

## 作者

Created for Hermes Agent  
GitHub: https://github.com/penghong/hermes-skills
