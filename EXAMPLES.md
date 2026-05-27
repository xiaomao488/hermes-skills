# 使用示例

## web-documentation-reader

### 示例1: 提取Python官方文档

```bash
python3 scripts/extract_docs.py https://docs.python.org/3/tutorial/introduction.html -o ./output
```

### 示例2: 提取GitHub README

```bash
python3 scripts/extract_docs.py https://github.com/snapcast/snapcast/blob/master/README.md
```

### 示例3: 批量提取文档

```bash
#!/bin/bash
# 批量提取多个文档页面

urls=(
    "https://docs.python.org/3/tutorial/introduction.html"
    "https://docs.python.org/3/tutorial/controlflow.html"
    "https://docs.python.org/3/tutorial/datastructures.html"
)

for url in "${urls[@]}"; do
    echo "提取: $url"
    python3 scripts/extract_docs.py "$url" -o ./python-docs
    sleep 2  # 避免请求过快
done
```

## github-project-learner

### 示例1: 学习单个项目

```bash
python3 scripts/learn_project.py snapcast/snapcast -o ./github-projects
```

### 示例2: 使用GitHub Token避免限流

```bash
export GITHUB_TOKEN="ghp_your_token_here"
python3 scripts/learn_project.py HEnquist/camilladsp -t $GITHUB_TOKEN -o ./output
```

### 示例3: 从URL学习

```bash
python3 scripts/learn_project.py https://github.com/mikebrady/shairport-sync
```

### 示例4: 批量学习多个项目

```python
#!/usr/bin/env python3
import subprocess
import time

projects = [
    'snapcast/snapcast',
    'HEnquist/camilladsp',
    'mikebrady/shairport-sync',
    'badaix/snapweb',
]

for project in projects:
    print(f"\n{'='*50}")
    print(f"学习项目: {project}")
    print('='*50)
    
    subprocess.run([
        'python3', 'scripts/learn_project.py',
        project,
        '-o', './github-projects'
    ])
    
    time.sleep(3)  # 避免API限流

print("\n✓ 所有项目学习完成!")
```

## 在Hermes Agent中使用

### 直接对话使用

```
用户: 帮我学习这个文档 https://docs.python.org/3/tutorial/

助手: [自动加载 web-documentation-reader 技能]
      正在提取文档...
      已保存到知识库
```

### 学习GitHub项目

```
用户: 去GitHub上学习snapcast/snapcast项目

助手: [自动加载 github-project-learner 技能]
      正在学习项目...
      已提取README、文档、项目结构等信息
```

### 批量学习

```
用户: 学习以下嵌入式音频相关的GitHub项目：
     - snapcast/snapcast
     - HEnquist/camilladsp
     - mikebrady/shairport-sync

助手: [批量执行学习流程]
      已完成3个项目的学习，保存到知识库
```

## Python API使用

### web-documentation-reader

```python
from scripts.extract_docs import DocumentationExtractor

# 创建提取器
extractor = DocumentationExtractor(
    url='https://docs.python.org/3/tutorial/',
    output_dir='./output'
)

# 执行提取
filepath = extractor.extract()
print(f"文档已保存到: {filepath}")
```

### github-project-learner

```python
from scripts.learn_project import GitHubProjectLearner

# 创建学习器
learner = GitHubProjectLearner(
    owner='snapcast',
    repo='snapcast',
    output_dir='./github-projects',
    token='your_github_token'  # 可选
)

# 执行学习
filepath = learner.learn()
print(f"项目文档已保存到: {filepath}")
```

## 集成到工作流

### 自动化学习脚本

```bash
#!/bin/bash
# auto_learn.sh - 自动学习并更新知识库

OUTPUT_DIR="$HOME/Documents/Obsidian/GitHub项目"

# 学习GitHub项目
echo "学习GitHub项目..."
python3 github-project-learner/scripts/learn_project.py \
    snapcast/snapcast \
    -o "$OUTPUT_DIR"

# 提取项目文档
echo "提取在线文档..."
python3 web-documentation-reader/scripts/extract_docs.py \
    https://github.com/snapcast/snapcast/blob/master/doc/configuration.md \
    -o "$OUTPUT_DIR/snapcast"

echo "✓ 完成!"
```

### 定时更新

```bash
# 添加到crontab，每周更新一次
# crontab -e
0 0 * * 0 /path/to/auto_learn.sh
```

## 输出格式

### Markdown文件结构

```markdown
# 项目名称

**来源:** https://...
**提取时间:** 2026-05-27 11:30:00

---

## 内容

主要内容...

## 代码示例

### 示例 1

```python
code here
```

## 相关链接

- [链接1](url1)
- [链接2](url2)
```

### 目录结构

```
output/
├── project-name.md          # 主文档
├── project-name/
│   └── docs/
│       ├── README.md
│       ├── CONTRIBUTING.md
│       └── API.md
```

## 常见问题

### Q: GitHub API限流怎么办？

A: 使用Personal Access Token:
```bash
export GITHUB_TOKEN="your_token"
python3 scripts/learn_project.py owner/repo -t $GITHUB_TOKEN
```

### Q: 如何提取需要登录的文档？

A: 目前不支持需要认证的页面，建议先手动下载或使用浏览器导出。

### Q: 如何处理大型项目？

A: 脚本会自动限制提取的文档数量，避免过载。可以手动调整代码中的限制。

### Q: 输出的Markdown格式不理想？

A: 可以修改脚本中的`to_markdown()`方法来自定义输出格式。
