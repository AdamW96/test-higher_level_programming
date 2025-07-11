#!/usr/bin/env python3
"""
Flask数据文件显示应用 - 最简洁版本
文件: task_03_files.py

仅包含核心应用逻辑，假设测试系统提供所有数据文件和模板
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# ============================================================================
# 数据读取函数
# ============================================================================

def read_json_data():
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
        raise FileNotFoundError("products.csv file not found")
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
    except (ValueError, TypeError):
        return None


# ============================================================================
# Flask 路由定义
# ============================================================================

@app.route('/')
def home():
    """主页路由"""
    return render_template('index.html')


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
                               error_message="Source parameter is required",
                               source=source,
                               product_id=product_id)

    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               error_message="Wrong source",
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

    except FileNotFoundError:
        return render_template('product_display.html',
                               error_message="Data file not found",
                               source=source,
                               product_id=product_id)

    except ValueError as e:
        return render_template('product_display.html',
                               error_message=f"Data format error: {str(e)}",
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
    app.run(debug=True, port=5000)
