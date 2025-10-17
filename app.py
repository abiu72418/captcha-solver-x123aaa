from flask import Flask, request, render_template
import requests
import pytesseract
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    captcha_url = request.args.get('url', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFElEQVQYV2NkQAP/Gf4bBjCqAEMAAHQDAh0U8PYAAAAASUVORK5CYII=')
    captcha_image = None

    if captcha_url.startswith('data:image/png;base64,'):
        # Decode the base64 image
        image_data = captcha_url.split(',')[1]
        captcha_image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    else:
        # Fetch the image from the URL
        response = requests.get(captcha_url)
        captcha_image = Image.open(io.BytesIO(response.content))

    # Solve the CAPTCHA
    captcha_text = pytesseract.image_to_string(captcha_image)
    return render_template('index.html', captcha_url=captcha_url, captcha_text=captcha_text)

if __name__ == '__main__':
    app.run(debug=True)
