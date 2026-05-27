#!/usr/bin/env python3
"""
GitHub Project Learner
深入学习GitHub项目并提取文档、代码结构等信息
"""

import sys
import argparse
import requests
import json
import time
from pathlib import Path
from urllib.parse import urlparse

class GitHubProjectLearner:
    def __init__(self, owner, repo, output_dir=None, token=None):
        self.owner = owner
        self.repo = repo
        self.output_dir = Path(output_dir) if output_dir else Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}"
        self.raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main"
        
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Project-Learner'
        }
        
        if token:
            self.headers['Authorization'] = f'token {token}'
    
    def _request(self, url, max_retries=3):
        """发送HTTP请求，带重试机制"""
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                
                # 检查速率限制
                if response.status_code == 403 and 'rate limit' in response.text.lower():
                    print("警告: GitHub API速率限制，请等待或使用token", file=sys.stderr)
                    return None
                
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                if attempt == max_retries - 1:
                    print(f"错误: 请求失败 - {e}", file=sys.stderr)
                    return None
                time.sleep(2 ** attempt)
        
        return None
    
    def get_repo_info(self):
        """获取仓库基本信息"""
        response = self._request(self.base_url)
        if response:
            return response.json()
        return None
    
    def get_readme(self):
        """获取README内容"""
        for filename in ['README.md', 'README.rst', 'README.txt', 'readme.md']:
            url = f"{self.raw_url}/{filename}"
            response = self._request(url)
            if response and response.status_code == 200:
                return {
                    'filename': filename,
                    'content': response.text
                }
        
        # 尝试其他分支
        for branch in ['master', 'develop']:
            url = f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/{branch}/README.md"
            response = self._request(url)
            if response and response.status_code == 200:
                return {
                    'filename': 'README.md',
                    'content': response.text
                }
        
        return None
    
    def get_documentation_files(self):
        """获取所有文档文件"""
        docs = []
        
        # 常见文档文件
        doc_files = [
            'CONTRIBUTING.md', 'CHANGELOG.md', 'CHANGES.md',
            'LICENSE', 'LICENSE.md', 'INSTALL.md', 
            'USAGE.md', 'API.md', 'ARCHITECTURE.md'
        ]
        
        for filename in doc_files:
            url = f"{self.raw_url}/{filename}"
            response = self._request(url)
            if response and response.status_code == 200:
                docs.append({
                    'filename': filename,
                    'content': response.text
                })
        
        # docs目录
        docs_url = f"{self.base_url}/contents/docs"
        response = self._request(docs_url)
        if response and response.status_code == 200:
            try:
                files = response.json()
                for file in files:
                    if file['type'] == 'file' and file['name'].endswith('.md'):
                        content_response = self._request(file['download_url'])
                        if content_response:
                            docs.append({
                                'filename': f"docs/{file['name']}",
                                'content': content_response.text
                            })
            except:
                pass
        
        return docs
    
    def get_directory_structure(self, path=''):
        """获取目录结构"""
        url = f"{self.base_url}/contents/{path}"
        response = self._request(url)
        
        if not response or response.status_code != 200:
            return []
        
        try:
            items = response.json()
            structure = []
            for item in items:
                structure.append({
                    'name': item['name'],
                    'type': item['type'],
                    'path': item['path'],
                    'size': item.get('size', 0)
                })
            return structure
        except:
            return []
    
    def get_languages(self):
        """获取代码语言统计"""
        url = f"{self.base_url}/languages"
        response = self._request(url)
        
        if response and response.status_code == 200:
            return response.json()
        return {}
    
    def get_contributors(self, limit=10):
        """获取贡献者信息"""
        url = f"{self.base_url}/contributors?per_page={limit}"
        response = self._request(url)
        
        if response and response.status_code == 200:
            return response.json()
        return []
    
    def get_latest_release(self):
        """获取最新版本信息"""
        url = f"{self.base_url}/releases/latest"
        response = self._request(url)
        
        if response and response.status_code == 200:
            return response.json()
        return None
    
    def get_topics(self):
        """获取项目标签"""
        url = self.base_url
        headers = self.headers.copy()
        headers['Accept'] = 'application/vnd.github.mercy-preview+json'
        
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            data = response.json()
            return data.get('topics', [])
        return []
    
    def generate_markdown(self, info, readme, docs, structure, languages, contributors, release):
        """生成Markdown文档"""
        md = f"# {info['full_name']}\n\n"
        
        # 基本信息
        md += "## 项目信息\n\n"
        md += f"**描述:** {info.get('description', 'N/A')}\n\n"
        md += f"**Stars:** ⭐ {info['stargazers_count']}\n"
        md += f"**Forks:** 🍴 {info['forks_count']}\n"
        md += f"**Watchers:** 👁️ {info['watchers_count']}\n"
        md += f"**主要语言:** {info.get('language', 'N/A')}\n"
        md += f"**许可证:** {info.get('license', {}).get('name', 'N/A')}\n"
        md += f"**创建时间:** {info['created_at']}\n"
        md += f"**最后更新:** {info['updated_at']}\n"
        md += f"**GitHub:** {info['html_url']}\n\n"
        
        # 主页和文档
        if info.get('homepage'):
            md += f"**主页:** {info['homepage']}\n\n"
        
        # 标签
        topics = self.get_topics()
        if topics:
            md += f"**标签:** {', '.join(topics)}\n\n"
        
        # 语言统计
        if languages:
            md += "## 代码语言分布\n\n"
            total = sum(languages.values())
            for lang, bytes_count in sorted(languages.items(), key=lambda x: x[1], reverse=True):
                percent = (bytes_count / total) * 100
                md += f"- **{lang}**: {percent:.1f}%\n"
            md += "\n"
        
        # 项目结构
        if structure:
            md += "## 项目结构\n\n"
            md += "```\n"
            for item in structure:
                icon = '📁' if item['type'] == 'dir' else '📄'
                md += f"{icon} {item['name']}\n"
            md += "```\n\n"
        
        # README
        if readme:
            md += "## README\n\n"
            md += readme['content'] + "\n\n"
        
        # 贡献者
        if contributors:
            md += "## 主要贡献者\n\n"
            for contributor in contributors[:10]:
                md += f"- [{contributor['login']}]({contributor['html_url']}) - {contributor['contributions']} commits\n"
            md += "\n"
        
        # 最新版本
        if release:
            md += "## 最新版本\n\n"
            md += f"**版本:** {release['tag_name']}\n"
            md += f"**发布时间:** {release['published_at']}\n"
            if release.get('body'):
                md += f"\n{release['body']}\n"
            md += "\n"
        
        # 其他文档
        if docs:
            md += "## 其他文档\n\n"
            for doc in docs:
                md += f"### {doc['filename']}\n\n"
                md += doc['content'] + "\n\n"
        
        return md
    
    def learn(self):
        """执行完整的学习流程"""
        print(f"正在学习项目: {self.owner}/{self.repo}")
        
        # 获取各种信息
        print("  获取仓库信息...")
        info = self.get_repo_info()
        if not info:
            print("错误: 无法获取仓库信息", file=sys.stderr)
            return None
        
        print("  获取README...")
        readme = self.get_readme()
        
        print("  获取文档...")
        docs = self.get_documentation_files()
        
        print("  分析项目结构...")
        structure = self.get_directory_structure()
        
        print("  统计代码语言...")
        languages = self.get_languages()
        
        print("  获取贡献者...")
        contributors = self.get_contributors()
        
        print("  获取最新版本...")
        release = self.get_latest_release()
        
        # 生成Markdown
        print("  生成文档...")
        markdown = self.generate_markdown(
            info, readme, docs, structure, 
            languages, contributors, release
        )
        
        # 保存
        filename = f"{self.repo}.md"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"✓ 已保存到: {filepath}")
        
        # 保存单独的文档文件
        if docs:
            docs_dir = self.output_dir / self.repo / 'docs'
            docs_dir.mkdir(parents=True, exist_ok=True)
            
            for doc in docs:
                doc_path = docs_dir / doc['filename'].replace('/', '-')
                with open(doc_path, 'w', encoding='utf-8') as f:
                    f.write(doc['content'])
        
        return filepath

def parse_github_url(url):
    """从GitHub URL解析owner和repo"""
    parsed = urlparse(url)
    if 'github.com' not in parsed.netloc:
        return None, None
    
    parts = parsed.path.strip('/').split('/')
    if len(parts) >= 2:
        return parts[0], parts[1]
    
    return None, None

def main():
    parser = argparse.ArgumentParser(
        description='深入学习GitHub项目',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s snapcast/snapcast
  %(prog)s https://github.com/HEnquist/camilladsp -o ./output
  %(prog)s owner/repo --token YOUR_GITHUB_TOKEN
        """
    )
    
    parser.add_argument('project', 
                       help='GitHub项目 (格式: owner/repo 或完整URL)')
    parser.add_argument('-o', '--output', default='.', 
                       help='输出目录 (默认: 当前目录)')
    parser.add_argument('-t', '--token', 
                       help='GitHub Personal Access Token (避免API限流)')
    
    args = parser.parse_args()
    
    # 解析项目
    if '/' in args.project and 'github.com' not in args.project:
        owner, repo = args.project.split('/', 1)
    else:
        owner, repo = parse_github_url(args.project)
    
    if not owner or not repo:
        print("错误: 无效的项目格式", file=sys.stderr)
        print("请使用格式: owner/repo 或 https://github.com/owner/repo", file=sys.stderr)
        return 1
    
    # 执行学习
    learner = GitHubProjectLearner(owner, repo, args.output, args.token)
    result = learner.learn()
    
    if result:
        print(f"\n✓ 学习完成!")
        return 0
    else:
        print(f"\n✗ 学习失败", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
