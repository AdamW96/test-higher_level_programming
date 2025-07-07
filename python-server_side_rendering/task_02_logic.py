#!/usr/bin/env python3
"""
Flask动态模板应用 - 循环和条件构造
文件: task_02_logic.py

这个Flask应用演示了：
1. Jinja2的循环和条件构造
2. JSON数据读取和解析
3. 动态内容渲染
4. 空列表的条件处理
"""

from flask import Flask, render_template
import json
import os

# 创建Flask应用实例
app = Flask(__name__)


def create_templates_directory():
    """创建templates目录（如果不存在）"""
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("✓ 创建了 templates/ 目录")


def create_json_file():
    """创建items.json文件"""
    items_data = {
        "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
    }

    with open('items.json', 'w', encoding='utf-8') as f:
        json.dump(items_data, f, indent=4)
    print("✓ 创建了 items.json 文件")


def create_basic_templates():
    """创建基础模板文件"""

    # 创建header.html
    header_content = """<header>
    <h1>My Flask App</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/items">Items</a></li>
        </ul>
    </nav>
</header>"""

    with open('templates/header.html', 'w', encoding='utf-8') as f:
        f.write(header_content)
    print("✓ 创建了 templates/header.html")

    # 创建footer.html
    footer_content = """<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>"""

    with open('templates/footer.html', 'w', encoding='utf-8') as f:
        f.write(footer_content)
    print("✓ 创建了 templates/footer.html")

    # 创建index.html
    index_content = """<!doctype html>
<html lang="en">
<head>
    <title>My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application with dynamic content.</p>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>Templates</li>
        <li>JSON Data</li>
    </ul>

    <p><a href="/items">View Items List →</a></p>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("✓ 创建了 templates/index.html")


def create_items_template():
    """创建items.html模板 - 包含循环和条件逻辑"""

    items_content = """<!doctype html>
<html lang="en">
<head>
    <title>Items List - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Items List</h1>

    <!-- 条件语句：检查items列表是否为空 -->
    {% if items %}
        <!-- 如果有items，使用循环显示每个item -->
        <p>Here are the available items:</p>
        <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
        <p>Total items: {{ items|length }}</p>
    {% else %}
        <!-- 如果没有items，显示消息 -->
        <p><strong>No items found</strong></p>
    {% endif %}

    <p><a href="/">← Back to Home</a></p>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/items.html', 'w', encoding='utf-8') as f:
        f.write(items_content)
    print("✓ 创建了 templates/items.html")


def create_about_template():
    """创建about.html模板"""
    about_content = """<!doctype html>
<html lang="en">
<head>
    <title>About Us - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>About Us</h1>
    <p>This Flask application demonstrates dynamic template rendering with Jinja2.</p>

    <h2>Features:</h2>
    <ul>
        <li>Dynamic content from JSON files</li>
        <li>Jinja2 loops and conditions</li>
        <li>Template inheritance</li>
        <li>Reusable components</li>
    </ul>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/about.html', 'w', encoding='utf-8') as f:
        f.write(about_content)
    print("✓ 创建了 templates/about.html")


def create_contact_template():
    """创建contact.html模板"""
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


def read_items_from_json():
    """从JSON文件读取items数据"""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('items', [])
    except FileNotFoundError:
        print("⚠️ items.json 文件未找到，返回空列表")
        return []
    except json.JSONDecodeError:
        print("⚠️ JSON文件格式错误，返回空列表")
        return []


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


@app.route('/items')
def items():
    """
    Items页面路由 - 展示动态内容
    从JSON文件读取数据并传递给模板
    """
    # 从JSON文件读取items数据
    items_list = read_items_from_json()

    # 传递数据到模板
    return render_template('items.html', items=items_list)


# ============================================================================
# 测试路由 - 用于测试不同的数据情况
# ============================================================================

@app.route('/items/empty')
def items_empty():
    """测试空列表的情况"""
    empty_items = []
    return render_template('items.html', items=empty_items)


@app.route('/items/test')
def items_test():
    """测试不同的items列表"""
    test_items = [
        "Advanced Python Programming",
        "Flask Web Development",
        "Database Design",
        "JavaScript Fundamentals",
        "Docker Container"
    ]
    return render_template('items.html', items=test_items)


@app.route('/demo')
def demo():
    """演示页面 - 展示模板逻辑的工作原理"""
    demo_html = """
    <h1>Jinja2模板逻辑演示</h1>

    <h2>📋 当前功能:</h2>
    <ul>
        <li><strong>循环 ({% for %})</strong>: 遍历items列表</li>
        <li><strong>条件 ({% if %})</strong>: 检查列表是否为空</li>
        <li><strong>变量渲染 ({{ }})</strong>: 显示item内容</li>
        <li><strong>过滤器 (|length)</strong>: 计算列表长度</li>
    </ul>

    <h2>🧪 测试不同情况:</h2>
    <ul>
        <li><a href="/items">正常items列表</a> (从JSON文件读取)</li>
        <li><a href="/items/empty">空items列表</a> (测试条件语句)</li>
        <li><a href="/items/test">测试items列表</a> (硬编码的测试数据)</li>
    </ul>

    <h2>📁 项目结构:</h2>
    <pre>
    your-project/
    ├── task_02_logic.py
    ├── items.json
    └── templates/
        ├── header.html
        ├── footer.html
        ├── index.html
        ├── about.html
        ├── contact.html
        └── items.html
    </pre>

    <h2>📄 items.json 内容:</h2>
    <pre>
    {
        "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
    }
    </pre>

    <h2>🔧 核心Jinja2语法:</h2>
    <pre>
    {% if items %}
        &lt;ul&gt;
            {% for item in items %}
                &lt;li&gt;{{ item }}&lt;/li&gt;
            {% endfor %}
        &lt;/ul&gt;
    {% else %}
        &lt;p&gt;No items found&lt;/p&gt;
    {% endif %}
    </pre>

    <p><a href="/">← 返回首页</a></p>
    """
    return demo_html


# ============================================================================
# 初始化应用
# ============================================================================

def setup_application():
    """设置应用 - 创建所有必要的文件和目录"""
    print("正在设置Flask应用...")

    # 创建目录和基础文件
    create_templates_directory()
    create_json_file()

    # 创建所有模板文件
    create_basic_templates()
    create_items_template()
    create_about_template()
    create_contact_template()

    print("\n✅ 应用设置完成!")


def create_test_json_files():
    """创建额外的测试JSON文件"""

    # 空列表测试文件
    empty_data = {"items": []}
    with open('items_empty.json', 'w', encoding='utf-8') as f:
        json.dump(empty_data, f, indent=4)

    # 大列表测试文件
    large_data = {
        "items": [
            "Python Book",
            "Flask Mug",
            "Jinja Sticker",
            "HTML Guide",
            "CSS Reference",
            "JavaScript Manual",
            "Database Tutorial",
            "API Documentation",
            "Git Handbook",
            "Docker Guide"
        ]
    }
    with open('items_large.json', 'w', encoding='utf-8') as f:
        json.dump(large_data, f, indent=4)

    print("✓ 创建了测试JSON文件")


# ============================================================================
# 应用启动
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Flask")
    print("=" * 60)

    # 设置应用
    setup_application()
    create_test_json_files()


    # 启动Flask应用
    app.run(debug=True, port=5000)