from flask import Flask, request, send_file
from PIL import Image, ImageOps
import io

app = Flask(__name__)

prefix = '/img_filter/'

@app.route(f'{prefix}upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    image = Image.open(file.stream)
    filtered_image = ImageOps.grayscale(image)
    img_io = io.BytesIO()
    filtered_image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)