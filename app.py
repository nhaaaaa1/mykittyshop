from flask import Flask, render_template, request, flash
import requests
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# =============================
# ✅ Telegram Bot Configuration
# =============================
TOKEN = "8148823820:AAGX7OjvLEIz6ZQXvQSyhWWHst_nafMT26s"
CHAT_ID = "@ziyu07062002"  # Channel username (bot must be admin)
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def send_telegram_message(message):
    """Send message to Telegram channel"""
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        print(f"Telegram response: {response.status_code} - {response.text}")

        if response.status_code != 200:
            print("❌ Failed to send Telegram message. Check bot permissions or chat ID.")
        else:
            print("✅ Message sent to Telegram successfully!")

        return response.status_code == 200

    except Exception as e:
        print(f"🚨 Telegram send failed: {e}")
        return False


# =============================
# ✅ Sample Product Data
# =============================
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

# =============================
# ✅ Flask Routes
# =============================

# Fix Render HEAD request error
@app.route('/', methods=['GET', 'HEAD'])
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
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        telegram_msg = (
            f"🌹 <b>New Contact Form Submission</b> 🌹\n\n"
            f"<b>Name:</b> {name}\n"
            f"<b>Email:</b> {email}\n"
            f"<b>Message:</b> {message}\n"
        )

        if send_telegram_message(telegram_msg):
            flash("Thank you for your message! We'll get back to you soon.", "success")
        else:
            flash("Message sent, but Telegram notification failed. Check logs.", "warning")

        return render_template('contact.html')

    return render_template('contact.html')


# =============================
# ✅ Run App
# =============================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
