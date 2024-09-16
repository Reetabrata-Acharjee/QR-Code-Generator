from flask import Flask, render_template, request, send_file, url_for
import qrcode as qr
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        qr_code = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr_code.add_data(url)
        qr_code.make(fit=True)
        img = qr_code.make_image(fill_color="black", back_color="white")

        # Save the QR code image to an in-memory buffer
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)

        # Encode the image data in base64
        encoded_img = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        # Render the qr_code.html template with the base64-encoded QR code
        return render_template('qr_code.html', qr_code=encoded_img)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
