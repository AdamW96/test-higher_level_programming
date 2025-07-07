#!/usr/bin/env python3
"""
Flask数据文件显示应用 - JSON和CSV处理
文件: task_03_files.py

这个Flask应用演示了：
1. 从JSON和CSV文件读取数据
2. 使用查询参数过滤数据
3. 错误处理和边界情况
4. 动态数据在HTML模板中的渲染
"""

from flask import Flask, render_template, request
import json
import csv
import os

# 创建Flask应用实例
app = Flask(__name__)


def create_templates_directory():
    """创建templates目录（如果不存在）"""
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("✓ 创建了 templates/ 目录")


def create_data_files():
    """创建示例数据文件"""

    # ========================================================================
    # 创建 products.json 文件
    # ========================================================================
    products_json_data = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
        {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
        {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 599.50},
        {"id": 4, "name": "Desk Chair", "category": "Furniture", "price": 89.99},
        {"id": 5, "name": "Water Bottle", "category": "Home Goods", "price": 12.50}
    ]

    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products_json_data, f, indent=2)
    print("✓ 创建了 products.json 文件")

    # ========================================================================
    # 创建 products.csv 文件
    # ========================================================================
    products_csv_data = [
        ["id", "name", "category", "price"],
        [1, "Laptop", "Electronics", 799.99],
        [2, "Coffee Mug", "Home Goods", 15.99],
        [3, "Smartphone", "Electronics", 599.50],
        [4, "Desk Chair", "Furniture", 89.99],
        [5, "Water Bottle", "Home Goods", 12.50]
    ]

    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(products_csv_data)
    print("✓ 创建了 products.csv 文件")


def create_basic_templates():
    """创建基础模板文件"""

    # 创建header.html
    header_content = """<header>
    <h1>My Flask App</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/products?source=json">Products (JSON)</a></li>
            <li><a href="/products?source=csv">Products (CSV)</a></li>
            <li><a href="/about">About</a></li>
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
    <p>This Flask application demonstrates reading and displaying data from JSON and CSV files.</p>

    <h2>Features:</h2>
    <ul>
        <li>Read data from JSON files</li>
        <li>Read data from CSV files</li>
        <li>Filter data by product ID</li>
        <li>Error handling for invalid inputs</li>
    </ul>

    <h2>Try These Links:</h2>
    <ul>
        <li><a href="/products?source=json">View all products from JSON</a></li>
        <li><a href="/products?source=csv">View all products from CSV</a></li>
        <li><a href="/products?source=json&id=1">View product ID 1 from JSON</a></li>
        <li><a href="/products?source=csv&id=2">View product ID 2 from CSV</a></li>
        <li><a href="/products?source=xml">Test invalid source (should show error)</a></li>
        <li><a href="/products?source=json&id=999">Test invalid ID (should show error)</a></li>
    </ul>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("✓ 创建了 templates/index.html")


def create_product_display_template():
    """创建产品显示模板"""

    product_display_content = """<!doctype html>
<html lang="en">
<head>
    <title>Product Display - My Flask App</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        .error-message {
            color: #d32f2f;
            background-color: #ffebee;
            padding: 15px;
            border: 1px solid #f8bbd9;
            border-radius: 4px;
            margin: 20px 0;
        }

        .info-message {
            color: #1976d2;
            background-color: #e3f2fd;
            padding: 15px;
            border: 1px solid #90caf9;
            border-radius: 4px;
            margin: 20px 0;
        }

        .filters {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 4px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    {% include 'header.html' %}

    <h1>Product Display</h1>

    <!-- 显示当前过滤条件 -->
    <div class="filters">
        <strong>Current Filters:</strong>
        <p>Source: {{ source if source else 'Not specified' }}</p>
        {% if product_id %}
            <p>Product ID: {{ product_id }}</p>
        {% else %}
            <p>Showing all products</p>
        {% endif %}
    </div>

    <!-- 错误消息显示 -->
    {% if error_message %}
        <div class="error-message">
            <strong>Error:</strong> {{ error_message }}
        </div>
    {% endif %}

    <!-- 产品数据显示 -->
    {% if products %}
        {% if products is iterable and products is not string %}
            <!-- 多个产品 -->
            <div class="info-message">
                <strong>Found {{ products|length }} product(s) from {{ source.upper() }} file</strong>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {% for product in products %}
                        <tr>
                            <td>{{ product.id }}</td>
                            <td>{{ product.name }}</td>
                            <td>{{ product.category }}</td>
                            <td>${{ "%.2f"|format(product.price) }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <!-- 单个产品 -->
            <div class="info-message">
                <strong>Found 1 product from {{ source.upper() }} file</strong>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ products.id }}</td>
                        <td>{{ products.name }}</td>
                        <td>{{ products.category }}</td>
                        <td>${{ "%.2f"|format(products.price) }}</td>
                    </tr>
                </tbody>
            </table>
        {% endif %}

        <!-- 快速链接 -->
        <div style="margin-top: 30px;">
            <h3>Quick Links:</h3>
            <ul>
                <li><a href="/products?source={{ source }}">View all products from {{ source.upper() }}</a></li>
                {% if source == 'json' %}
                    <li><a href="/products?source=csv">Switch to CSV view</a></li>
                {% else %}
                    <li><a href="/products?source=json">Switch to JSON view</a></li>
                {% endif %}
                <li><a href="/">Back to Home</a></li>
            </ul>
        </div>
    {% endif %}

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/product_display.html', 'w', encoding='utf-8') as f:
        f.write(product_display_content)
    print("✓ 创建了 templates/product_display.html")


def create_about_template():
    """创建关于页面模板"""
    about_content = """<!doctype html>
<html lang="en">
<head>
    <title>About - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>About This Application</h1>
    <p>This Flask application demonstrates how to read and display data from different file formats.</p>

    <h2>Supported Features:</h2>
    <ul>
        <li>Read data from JSON files</li>
        <li>Read data from CSV files</li>
        <li>Filter products by ID</li>
        <li>Handle invalid source parameters</li>
        <li>Handle missing product IDs</li>
        <li>Display data in formatted tables</li>
    </ul>

    <h2>URL Examples:</h2>
    <ul>
        <li><code>/products?source=json</code> - All products from JSON</li>
        <li><code>/products?source=csv</code> - All products from CSV</li>
        <li><code>/products?source=json&id=1</code> - Product ID 1 from JSON</li>
        <li><code>/products?source=csv&id=2</code> - Product ID 2 from CSV</li>
    </ul>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/about.html', 'w', encoding='utf-8') as f:
        f.write(about_content)
    print("✓ 创建了 templates/about.html")


# ============================================================================
# 数据读取函数
# ============================================================================

def read_json_data():
    """从JSON文件读取产品数据"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

            # 将字典转换为对象，便于模板访问
            class Product:
                def __init__(self, **kwargs):
                    for key, value in kwargs.items():
                        setattr(self, key, value)

            return [Product(**item) for item in data]
    except FileNotFoundError:
        raise FileNotFoundError("JSON file not found")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")


def read_csv_data():
    """从CSV文件读取产品数据"""
    try:
        products = []
        with open('products.csv', 'r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)

            class Product:
                def __init__(self, **kwargs):
                    for key, value in kwargs.items():
                        setattr(self, key, value)

            for row in csv_reader:
                # 转换数据类型
                product_data = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(Product(**product_data))

        return products
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found")
    except ValueError as e:
        raise ValueError(f"Invalid CSV data: {e}")


def filter_products_by_id(products, product_id):
    """根据ID过滤产品"""
    try:
        product_id = int(product_id)
        for product in products:
            if product.id == product_id:
                return product
        return None
    except ValueError:
        return None


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


@app.route('/products')
def products():
    """
    产品显示路由

    查询参数:
    - source: 'json' 或 'csv' (必需)
    - id: 产品ID (可选)
    """
    # 获取查询参数
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 验证source参数
    if not source:
        return render_template('product_display.html',
                               error_message="Source parameter is required. Use ?source=json or ?source=csv",
                               source=source,
                               product_id=product_id)

    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               error_message="Wrong source. Use 'json' or 'csv'",
                               source=source,
                               product_id=product_id)

    try:
        # 根据source读取数据
        if source == 'json':
            products_data = read_json_data()
        else:  # source == 'csv'
            products_data = read_csv_data()

        # 如果指定了ID，过滤数据
        if product_id:
            filtered_product = filter_products_by_id(products_data, product_id)
            if filtered_product is None:
                return render_template('product_display.html',
                                       error_message="Product not found",
                                       source=source,
                                       product_id=product_id)
            products_data = filtered_product

        # 渲染模板
        return render_template('product_display.html',
                               products=products_data,
                               source=source,
                               product_id=product_id)

    except FileNotFoundError as e:
        return render_template('product_display.html',
                               error_message=f"File not found: {e}",
                               source=source,
                               product_id=product_id)

    except ValueError as e:
        return render_template('product_display.html',
                               error_message=f"Data error: {e}",
                               source=source,
                               product_id=product_id)

    except Exception as e:
        return render_template('product_display.html',
                               error_message=f"Unexpected error: {e}",
                               source=source,
                               product_id=product_id)


# ============================================================================
# 测试和调试路由
# ============================================================================

@app.route('/debug')
def debug():
    """调试路由 - 显示文件状态和测试链接"""
    debug_info = """
    <h1>Debug Information</h1>

    <h2>File Status:</h2>
    <ul>
    """

    # 检查文件状态
    files_to_check = ['products.json', 'products.csv']
    for file_name in files_to_check:
        exists = os.path.exists(file_name)
        status = "✓ 存在" if exists else "✗ 不存在"
        debug_info += f"<li>{file_name}: {status}</li>"

    debug_info += """
    </ul>

    <h2>Test Links:</h2>
    <h3>Valid Tests:</h3>
    <ul>
        <li><a href="/products?source=json">All products from JSON</a></li>
        <li><a href="/products?source=csv">All products from CSV</a></li>
        <li><a href="/products?source=json&id=1">Product ID 1 from JSON</a></li>
        <li><a href="/products?source=csv&id=2">Product ID 2 from CSV</a></li>
    </ul>

    <h3>Error Tests:</h3>
    <ul>
        <li><a href="/products?source=xml">Invalid source (xml)</a></li>
        <li><a href="/products?source=json&id=999">Invalid ID (999)</a></li>
        <li><a href="/products">Missing source parameter</a></li>
        <li><a href="/products?source=csv&id=abc">Invalid ID format (abc)</a></li>
    </ul>

    <p><a href="/">← Back to Home</a></p>
    """

    return debug_info


# ============================================================================
# 应用初始化
# ============================================================================

def setup_application():
    """设置应用 - 创建所有必要的文件和目录"""
    print("正在设置Flask应用...")

    # 创建目录和基础文件
    create_templates_directory()
    create_data_files()

    # 创建所有模板文件
    create_basic_templates()
    create_product_display_template()
    create_about_template()

    print("\n✅ 应用设置完成!")


# ============================================================================
# 应用启动
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("Flask 数据文件显示应用 - JSON和CSV处理")
    print("=" * 70)

    # 设置应用
    setup_application()

    print(f"\n🚀 启动Flask服务器...")
    print(f"访问以下URL测试功能：")
    print(f"  • 主页:           http://127.0.0.1:5000/")
    print(f"  • JSON产品:       http://127.0.0.1:5000/products?source=json")
    print(f"  • CSV产品:        http://127.0.0.1:5000/products?source=csv")
    print(f"  • 特定产品:       http://127.0.0.1:5000/products?source=json&id=1")
    print(f"  • 错误测试:       http://127.0.0.1:5000/products?source=xml")
    print(f"  • 调试页面:       http://127.0.0.1:5000/debug")
    print(f"\n按 Ctrl+C 停止服务器")
    print("-" * 70)

    # 启动Flask应用
    app.run(debug=True, port=5000)