from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def homepage():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My E-commerce Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
                color: #333;
            }
            header {
                background-color: maroon;
                color: white;
                padding: 20px;
                text-align: center;
            }
            .products {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                padding: 20px;
            }
            .product {
                background: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                text-align: center;
                width: 200px;
                transition: transform 0.3s ease;
            }
            .product:hover {
                transform: scale(1.05);
            }
            .product img {
                width: 100%;
                height: auto;
                border-bottom: 1px solid #ddd;
                margin-bottom: 10px;
            }
            .product h3 {
                margin: 0;
                font-size: 18px;
            }
            .product p {
                color: #555;
                font-size: 16px;
            }
            .product a {
                display: inline-block;
                margin-top: 10px;
                padding: 8px 12px;
                background-color: maroon;
                color: white;
                text-decoration: none;
                border-radius: 4px;
            }
            .product a:hover {
                background-color: darkred;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to My Store</h1>
        </header>
        <div class="products">
            <!-- Product 1 -->
            <div class="product">
                <img src="https://via.placeholder.com/200" alt="Product 1">
                <h3>Product 1</h3>
                <p>$20.99</p>
                <a href="#">View Details</a>
            </div>
            <!-- Product 2 -->
            <div class="product">
                <img src="https://via.placeholder.com/200" alt="Product 2">
                <h3>Product 2</h3>
                <p>$35.50</p>
                <a href="#">View Details</a>
            </div>
            <!-- Product 3 -->
            <div class="product">
                <img src="https://via.placeholder.com/200" alt="Product 3">
                <h3>Product 3</h3>
                <p>$15.00</p>
                <a href="#">View Details</a>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
