#!/usr/bin/env python3
"""
Flask基础HTML模板应用 - 简洁版本
文件: task_01_jinja.py

这个Flask应用只包含基本功能，无复杂样式设计
"""

from flask import Flask, render_template
import os

# 创建Flask应用实例
app = Flask(__name__)


def create_simple_templates():
    """创建简单的模板文件"""

    # 创建templates目录
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("✓ 创建了 templates/ 目录")

    # ========================================================================
    # 1. 创建 header.html - 简单的头部模板
    # ========================================================================
    header_content = """<header>
    <h1>My Flask App</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </nav>
</header>"""

    with open('templates/header.html', 'w', encoding='utf-8') as f:
        f.write(header_content)
    print("✓ 创建了 templates/header.html")

    # ========================================================================
    # 2. 创建 footer.html - 简单的尾部模板
    # ========================================================================
    footer_content = """<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>"""

    with open('templates/footer.html', 'w', encoding='utf-8') as f:
        f.write(footer_content)
    print("✓ 创建了 templates/footer.html")

    # ========================================================================
    # 3. 创建 index.html - 主页模板
    # ========================================================================
    index_content = """<!doctype html>
<html lang="en">
<head>
    <title>My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application.</p>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>Templates</li>
    </ul>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("✓ 创建了 templates/index.html")

    # ========================================================================
    # 4. 创建 about.html - 关于页面模板
    # ========================================================================
    about_content = """<!doctype html>
<html lang="en">
<head>
    <title>About Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>About Us</h1>
    <p>This is the about page of our Flask application. Here you can learn more about our project and the technologies we use.</p>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/about.html', 'w', encoding='utf-8') as f:
        f.write(about_content)
    print("✓ 创建了 templates/about.html")

    # ========================================================================
    # 5. 创建 contact.html - 联系页面模板
    # ========================================================================
    contact_content = """<!doctype html>
<html lang="en">
<head>
    <title>Contact Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Contact Us</h1>
    <p>Get in touch with us through this contact page. We'd love to hear from you!</p>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/contact.html', 'w', encoding='utf-8') as f:
        f.write(contact_content)
    print("✓ 创建了 templates/contact.html")


# ============================================================================
# Flask 路由定义
# ============================================================================

@app.route('/')
def home():
    """主页路由"""
    return render_template('index.html')


@app.route('/about')
def about():
    """关于页面路由"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """联系页面路由"""
    return render_template('contact.html')


# ============================================================================
# 应用启动
# ============================================================================

if __name__ == '__main__':
    create_simple_templates()

    # 启动Flask应用
    app.run(debug=True, port=5000)