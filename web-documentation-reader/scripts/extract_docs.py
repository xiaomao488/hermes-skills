#!/usr/bin/env python3
"""
Web Documentation Extractor
从网页中提取技术文档内容并保存为Markdown格式
"""

import sys
import argparse
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json
from urllib.parse import urlparse
import time

class DocumentationExtractor:
    def __init__(self, url, output_dir=None):
        self.url = url
        self.output_dir = Path(output_dir) if output_dir else Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_content(self):
        """获取网页内容"""
        try:
            response = requests.get(self.url, headers=self.headers, timeout=30)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except requests.RequestException as e:
            print(f"错误: 无法获取网页内容 - {e}", file=sys.stderr)
            return None
    
    def extract_title(self, soup):
        """提取页面标题"""
        # 尝试多种方式获取标题
        title = soup.find('h1')
        if title:
            return title.get_text(strip=True)
        
        title = soup.find('title')
        if title:
            return title.get_text(strip=True)
        
        return urlparse(self.url).path.split('/')[-1] or 'Untitled'
    
    def extract_main_content(self, soup):
        """提取主要内容"""
        # 移除不需要的元素
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()
        
        # 尝试找到主要内容容器
        main_content = (
            soup.find('main') or
            soup.find('article') or
            soup.find(class_=['content', 'documentation', 'markdown-body', 'doc-content', 'article-content']) or
            soup.find(id=['content', 'main-content', 'documentation']) or
            soup.find('body')
        )
        
        if not main_content:
            return ""
        
        return main_content.get_text(separator='\n', strip=True)
    
    def extract_code_blocks(self, soup):
        """提取代码块"""
        code_blocks = []
        
        for pre in soup.find_all('pre'):
            code = pre.find('code')
            if code:
                # 尝试获取语言
                classes = code.get('class', [])
                language = ''
                for cls in classes:
                    if cls.startswith('language-'):
                        language = cls.replace('language-', '')
                        break
                    elif cls in ['python', 'javascript', 'bash', 'java', 'cpp', 'c', 'go', 'rust']:
                        language = cls
                        break
                
                code_blocks.append({
                    'language': language,
                    'code': code.get_text()
                })
        
        return code_blocks
    
    def extract_links(self, soup):
        """提取重要链接"""
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.get_text(strip=True)
            if text and href and not href.startswith('#'):
                links.append({
                    'text': text,
                    'url': href
                })
        return links[:20]  # 限制数量
    
    def to_markdown(self, title, content, code_blocks, links):
        """转换为Markdown格式"""
        markdown = f"# {title}\n\n"
        markdown += f"**来源:** {self.url}\n"
        markdown += f"**提取时间:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        markdown += "---\n\n"
        
        # 主要内容
        markdown += "## 内容\n\n"
        markdown += content + "\n\n"
        
        # 代码示例
        if code_blocks:
            markdown += "## 代码示例\n\n"
            for i, block in enumerate(code_blocks, 1):
                lang = block['language'] or 'text'
                markdown += f"### 示例 {i}\n\n"
                markdown += f"```{lang}\n{block['code']}\n```\n\n"
        
        # 相关链接
        if links:
            markdown += "## 相关链接\n\n"
            for link in links:
                markdown += f"- [{link['text']}]({link['url']})\n"
            markdown += "\n"
        
        return markdown
    
    def save(self, content, filename=None):
        """保存内容到文件"""
        if not filename:
            # 从URL生成文件名
            parsed = urlparse(self.url)
            filename = parsed.path.strip('/').replace('/', '-') or 'index'
            filename = f"{filename}.md"
        
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def extract(self):
        """执行完整的提取流程"""
        print(f"正在提取: {self.url}")
        
        # 获取内容
        html = self.fetch_content()
        if not html:
            return None
        
        # 解析HTML
        soup = BeautifulSoup(html, 'html.parser')
        
        # 提取各部分
        title = self.extract_title(soup)
        print(f"标题: {title}")
        
        content = self.extract_main_content(soup)
        print(f"内容长度: {len(content)} 字符")
        
        code_blocks = self.extract_code_blocks(soup)
        print(f"代码块: {len(code_blocks)} 个")
        
        links = self.extract_links(soup)
        print(f"链接: {len(links)} 个")
        
        # 转换为Markdown
        markdown = self.to_markdown(title, content, code_blocks, links)
        
        # 保存
        filepath = self.save(markdown)
        print(f"已保存到: {filepath}")
        
        return filepath

def main():
    parser = argparse.ArgumentParser(
        description='从网页中提取技术文档内容',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s https://docs.python.org/3/tutorial/
  %(prog)s https://example.com/docs -o ./output
  %(prog)s https://github.com/user/repo/blob/main/README.md
        """
    )
    
    parser.add_argument('url', help='要提取的网页URL')
    parser.add_argument('-o', '--output', default='.', 
                       help='输出目录 (默认: 当前目录)')
    parser.add_argument('--json', action='store_true',
                       help='同时输出JSON格式')
    
    args = parser.parse_args()
    
    # 执行提取
    extractor = DocumentationExtractor(args.url, args.output)
    result = extractor.extract()
    
    if result:
        print(f"\n✓ 提取成功!")
        return 0
    else:
        print(f"\n✗ 提取失败", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
