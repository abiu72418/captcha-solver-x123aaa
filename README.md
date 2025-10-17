# captcha-solver-x123aaa

## Overview

`captcha-solver-x123aaa` is a simple web application that solves CAPTCHA images. It accepts a URL parameter pointing to a CAPTCHA image and displays the solved text on the page.

## Features
- Accepts a CAPTCHA image URL via query parameters.
- Displays the CAPTCHA image.
- Solves the CAPTCHA and displays the result within 15 seconds.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/captcha-solver-x123aaa.git
   cd captcha-solver-x123aaa
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000/?url=https://.../image.png`.

## Usage

To use the application, provide the URL of the CAPTCHA image as a query parameter. For example:
```
http://localhost:5000/?url=https://example.com/captcha.png
```

If no URL is provided, the application will default to using a sample CAPTCHA image.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
