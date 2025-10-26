from flask import Flask, render_template, request, jsonify, flash
import requests
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Telegram Bot Configuration
TOKEN = "8148823820:AAGX7OjvLEIz6ZQXvQSyhWWHst_nafMT26s"
CHAT_ID = "@ziyu07062002"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

# Sample flower data with image URLs
flowers = [
    {
        'id': 1,
        'name': 'Keychain',
        'price': 29.99,
        'image': 'https://www.sanrio.com/cdn/shop/files/zz-2411444278_KT_--1_800x.jpg?v=1748047880',
        'description': 'Carry your charm everywhere! A trendy, lightweight bag made for girls who love fashion and fun.',
        'details': 'Material: Premium PU leather',
        'care_tips': 'Wipe gently and store me with love. 💌',
        'in_stock': True
    },
    {
        'id': 2,
        'name': 'Kitty Art Plushie',
        'price': 24.99,
        'image': 'https://www.sanrio.com/cdn/shop/files/699888-Zoom.1_800x.jpg?v=1746493013',
        'description': 'Carry your charm everywhere! A trendy, lightweight bag made for girls who love fashion and fun.',
        'details': 'Material: Premium PU leather',
        'care_tips': 'Wipe gently and store me with love. 💌',
        'in_stock': True
    },
    {
        'id': 3,
        'name': 'Kitty Baseball Plush',
        'price': 34.99,
        'image': 'https://www.sanrio.com/cdn/shop/files/696170-Zoom.1_800x.jpg?v=1746493048',
        'description': 'Carry your charm everywhere! A trendy, lightweight bag made for girls who love fashion and fun.',
        'details': 'Material: Premium PU leather',
        'care_tips': 'Wipe gently and store me with love. 💌',
        'in_stock': True
    },
    {
        'id': 4,
        'name': 'Kitty Plush Mascot Keychain',
        'price': 39.99,
        'image': 'https://www.sanrio.com/cdn/shop/files/zz-2504612898_KT_--1_800x.jpg?v=1745440807',
        'description': 'Carry your charm everywhere! A trendy, lightweight bag made for girls who love fashion and fun.',
        'details': 'Material: Premium PU leather',
        'care_tips': 'Wipe gently and store me with love. 💌',
        'in_stock': True
    },
    {
        'id': 5,
        'name': 'Kitty Customize Keychain',
        'price': 44.99,
        'image': 'https://www.sanrio.com/cdn/shop/files/4550337289839-2_800x.jpg?v=1738087203',
        'description': 'Carry your charm everywhere! A trendy, lightweight bag made for girls who love fashion and fun.',
        'details': 'Material: Premium PU leather',
        'care_tips': 'Wipe gently and store me with love. 💌',
        'in_stock': False
    },
    {
        'id': 6,
        'name': 'Kitty Smartphone Charm',
        'price': 19.99,
        'image': 'https://www.sanrio.com/cdn/shop/files/zz-2505072346_KT_--1_800x.jpg?v=1747800677',
        'description': 'Carry your charm everywhere! A trendy, lightweight bag made for girls who love fashion and fun.',
        'details': 'Material: Premium PU leather',
        'care_tips': 'Wipe gently and store me with love. 💌',
        'in_stock': True
    }
]


def send_telegram_message(message):
    """Send message to Telegram bot"""
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data)
        return response.status_code == 200
    except:
        return False


@app.route('/')
def home():
    return render_template('index.html', flowers=flowers[:4])  # Show only 4 on homepage


@app.route('/products')
def products():
    return render_template('products.html', flowers=flowers)


@app.route('/product/<int:product_id>')
def product_details(product_id):
    flower = next((f for f in flowers if f['id'] == product_id), None)
    if flower:
        return render_template('product_details.html', flower=flower)
    return "Product not found", 404


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send notification to Telegram
        telegram_msg = f"🌹 <b>New Contact Form Submission</b> 🌹\n\n"
        telegram_msg += f"<b>Name:</b> {name}\n"
        telegram_msg += f"<b>Email:</b> {email}\n"
        telegram_msg += f"<b>Message:</b> {message}\n"

        if send_telegram_message(telegram_msg):
            flash('Thank you for your message! We\'ll get back to you soon.', 'success')
        else:
            flash('Message sent! (Telegram notification failed)', 'warning')

        return render_template('contact.html')

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)