#!/usr/bin/env python3
"""
Flask task task 04
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def create_database():
    """创建SQLite数据库和表，按任务要求设置"""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


def create_templates():
    """创建必要的模板文件"""
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # header.html
    header_html = """<header>
    <h1>My Flask App</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/products?source=json">JSON</a></li>
            <li><a href="/products?source=csv">CSV</a></li>
            <li><a href="/products?source=sql">SQLite</a></li>
        </ul>
    </nav>
</header>"""

    with open('templates/header.html', 'w') as f:
        f.write(header_html)

    # footer.html
    footer_html = """<footer>
    <p>&copy; 2024 My Flask App</p>
</footer>"""

    with open('templates/footer.html', 'w') as f:
        f.write(footer_html)

    # product_display.html (从Task 3扩展)
    product_display_html = """<!doctype html>
<html lang="en">
<head>
    <title>Product Display - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <h1>Product Display</h1>

    <!-- 错误消息显示 -->
    {% if error_message %}
        <div style="color: red; background-color: #ffebee; padding: 15px; border: 1px solid #f8bbd9; margin: 20px 0;">
            <strong>Error:</strong> {{ error_message }}
        </div>
    {% endif %}

    <!-- 产品数据显示 -->
    {% if products %}
        <p><strong>Source:</strong> {{ source.upper() }}</p>
        {% if product_id %}
            <p><strong>Product ID:</strong> {{ product_id }}</p>
        {% endif %}

        <table border="1" style="border-collapse: collapse; width: 100%; margin-top: 20px;">
            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th style="padding: 10px;">Name</th>
                    <th style="padding: 10px;">Category</th>
                    <th style="padding: 10px;">Price</th>
                </tr>
            </thead>
            <tbody>
                {% if products is iterable and products is not string %}
                    <!-- 多个产品 -->
                    {% for product in products %}
                        <tr>
                            <td style="padding: 10px;">{{ product.name }}</td>
                            <td style="padding: 10px;">{{ product.category }}</td>
                            <td style="padding: 10px;">${{ "%.2f"|format(product.price) }}</td>
                        </tr>
                    {% endfor %}
                {% else %}
                    <!-- 单个产品 -->
                    <tr>
                        <td style="padding: 10px;">{{ products.name }}</td>
                        <td style="padding: 10px;">{{ products.category }}</td>
                        <td style="padding: 10px;">${{ "%.2f"|format(products.price) }}</td>
                    </tr>
                {% endif %}
            </tbody>
        </table>
    {% endif %}

    <p><a href="/">← Back to Home</a></p>

    {% include 'footer.html' %}
</body>
</html>"""

    with open('templates/product_display.html', 'w') as f:
        f.write(product_display_html)


# ============================================================================
# 数据读取函数
# ============================================================================

def read_json_data():
    """从JSON文件读取产品数据"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        class Product:
            def __init__(self, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)

        return [Product(**item) for item in data]
    except FileNotFoundError:
        raise FileNotFoundError("products.json file not found")
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
                product_data = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(Product(**product_data))

        return products
    except FileNotFoundError:
        raise FileNotFoundError("products.csv file not found")
    except ValueError as e:
        raise ValueError(f"Invalid CSV data: {e}")


def read_sql_data():
    """从SQLite数据库读取产品数据"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        # 查询所有产品
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        conn.close()

        # 将查询结果转换为Product对象
        class Product:
            def __init__(self, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)

        products = []
        for row in rows:
            product_data = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(Product(**product_data))

        return products

    except sqlite3.Error as e:
        raise sqlite3.Error(f"Database error: {e}")


def filter_products_by_id(products, product_id):
    """根据ID过滤产品"""
    try:
        product_id = int(product_id)
        for product in products:
            if product.id == product_id:
                return product
        return None
    except (ValueError, TypeError):
        return None


# ============================================================================
# Flask 路由定义
# ============================================================================

@app.route('/')
def home():
    """主页路由"""
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <title>My Flask App</title>
    </head>
    <body>
        <h1>Welcome to My Flask App</h1>
        <p>This Flask application supports JSON, CSV, and SQLite data sources.</p>

        <h2>Test Links:</h2>
        <ul>
            <li><a href="/products?source=json">View JSON products</a></li>
            <li><a href="/products?source=csv">View CSV products</a></li>
            <li><a href="/products?source=sql">View SQLite products</a></li>
            <li><a href="/products?source=sql&id=1">View product ID 1 from SQLite</a></li>
            <li><a href="/products?source=xml">Test invalid source</a></li>
        </ul>
    </body>
    </html>
    """


@app.route('/products')
def products():
    """
    产品显示路由 - 支持JSON, CSV, SQL数据源

    查询参数:
    - source: 'json', 'csv', 或 'sql' (必需)
    - id: 产品ID (可选)
    """
    # 获取查询参数
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 验证source参数
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               error_message="Wrong source",
                               source=source,
                               product_id=product_id)

    try:
        # 根据source读取数据
        if source == 'json':
            products_data = read_json_data()
        elif source == 'csv':
            products_data = read_csv_data()
        else:  # source == 'sql'
            products_data = read_sql_data()

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
                               error_message=str(e),
                               source=source,
                               product_id=product_id)

    except sqlite3.Error as e:
        return render_template('product_display.html',
                               error_message=f"Database error: {str(e)}",
                               source=source,
                               product_id=product_id)

    except ValueError as e:
        return render_template('product_display.html',
                               error_message=str(e),
                               source=source,
                               product_id=product_id)

    except Exception as e:
        return render_template('product_display.html',
                               error_message=f"Unexpected error: {str(e)}",
                               source=source,
                               product_id=product_id)


# ============================================================================
# 应用启动
# ============================================================================

if __name__ == '__main__':
    # 创建数据库和模板
    create_database()
    create_templates()

    app.run(debug=True, port=5000)
