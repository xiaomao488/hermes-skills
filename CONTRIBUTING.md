# 贡献指南

感谢你对 Hermes Skills 项目的关注！我们欢迎所有形式的贡献。

## 如何贡献

### 报告问题 (Issues)

如果你发现了bug或有功能建议：

1. 先搜索 [Issues](https://github.com/xiaomao488/hermes-skills/issues) 确认问题是否已存在
2. 如果没有，创建新的Issue
3. 清楚地描述问题或建议
4. 如果是bug，请提供：
   - 复现步骤
   - 预期行为
   - 实际行为
   - 环境信息（操作系统、Python版本等）

### 提交代码 (Pull Requests)

#### 1. Fork 仓库

点击页面右上角的 "Fork" 按钮，将仓库fork到你的账号下。

#### 2. 克隆到本地

```bash
git clone https://github.com/你的用户名/hermes-skills.git
cd hermes-skills
```

#### 3. 创建分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

分支命名规范：
- `feature/` - 新功能
- `fix/` - Bug修复
- `docs/` - 文档更新
- `refactor/` - 代码重构

#### 4. 进行修改

- 遵循现有的代码风格
- 添加必要的注释
- 更新相关文档

#### 5. 测试你的更改

```bash
# 测试脚本是否正常运行
python3 web-documentation-reader/scripts/extract_docs.py https://example.com
python3 github-project-learner/scripts/learn_project.py owner/repo
```

#### 6. 提交更改

```bash
git add .
git commit -m "描述你的更改"
```

提交信息规范：
- 使用清晰、简洁的描述
- 第一行不超过50个字符
- 如果需要详细说明，空一行后继续

示例：
```
Add support for GitLab projects

- Add GitLab API integration
- Update documentation
- Add examples for GitLab usage
```

#### 7. 推送到你的Fork

```bash
git push origin feature/your-feature-name
```

#### 8. 创建 Pull Request

1. 访问你fork的仓库页面
2. 点击 "Pull Request" 按钮
3. 选择你的分支
4. 填写PR描述：
   - 说明你做了什么
   - 为什么要做这个更改
   - 如何测试
5. 提交PR

## 贡献类型

### 🐛 Bug修复

- 修复现有功能的问题
- 提供测试用例
- 更新文档

### ✨ 新功能

- 添加新的技能
- 扩展现有技能的功能
- 改进用户体验

### 📚 文档

- 改进README
- 添加使用示例
- 翻译文档
- 修正错别字

### 🎨 代码优化

- 重构代码
- 性能优化
- 代码风格改进

## 代码规范

### Python代码风格

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范：

```python
# 好的示例
def extract_content(url, timeout=30):
    """提取网页内容
    
    Args:
        url: 网页URL
        timeout: 超时时间（秒）
    
    Returns:
        str: 提取的内容
    """
    response = requests.get(url, timeout=timeout)
    return response.text

# 避免
def extract(u,t=30):
    r=requests.get(u,timeout=t)
    return r.text
```

### 文档规范

- 使用Markdown格式
- 提供代码示例
- 保持简洁清晰
- 中英文之间加空格

### 提交信息规范

```
类型: 简短描述（不超过50字符）

详细描述（如果需要）：
- 要点1
- 要点2

相关Issue: #123
```

类型：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

## 技能开发指南

### 创建新技能

1. 在对应的category目录下创建技能文件夹
2. 创建 `SKILL.md` 文件（必需）
3. 添加 `scripts/` 目录（如果需要）
4. 添加 `examples/` 目录（推荐）
5. 添加 `references/` 目录（可选）

### SKILL.md 模板

```markdown
---
name: skill-name
description: "简短描述"
platforms: [linux, macos, windows]
tags: [tag1, tag2]
---

# Skill Name

## 使用场景

描述什么时候使用这个技能...

## 核心功能

列出主要功能...

## 使用方法

提供使用示例...

## 依赖

列出依赖项...
```

### 脚本开发规范

```python
#!/usr/bin/env python3
"""
脚本简短描述
"""

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='脚本描述')
    parser.add_argument('input', help='输入参数')
    parser.add_argument('-o', '--output', help='输出路径')
    
    args = parser.parse_args()
    
    # 主要逻辑
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

## 测试

在提交PR之前，请确保：

- [ ] 代码可以正常运行
- [ ] 没有语法错误
- [ ] 文档已更新
- [ ] 示例可以正常工作
- [ ] 遵循代码规范

## 审核流程

1. 提交PR后，维护者会进行审核
2. 可能会要求修改
3. 通过审核后会被合并
4. 你的贡献会被记录在项目中

## 行为准则

- 尊重所有贡献者
- 保持友好和专业
- 接受建设性的批评
- 关注项目的最佳利益

## 许可证

通过贡献代码，你同意你的贡献将在 [MIT License](LICENSE) 下发布。

## 需要帮助？

- 查看 [Issues](https://github.com/xiaomao488/hermes-skills/issues)
- 阅读 [README.md](README.md)
- 查看 [EXAMPLES.md](EXAMPLES.md)

## 致谢

感谢所有贡献者！你们的贡献让这个项目变得更好。

---

再次感谢你的贡献！🎉
