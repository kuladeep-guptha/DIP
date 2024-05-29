from flask import Flask, request, render_template, jsonify
import cv2
import base64
import numpy as np
import os

app = Flask(__name__)

def numpy_img_to_base64(watermarked_img):
    # Convert numpy array to bytes
    _, buffer = cv2.imencode('.jpg', watermarked_img)
    img_bytes = buffer.tobytes()

    # Encode bytes to base64 string
    img_b64 = base64.b64encode(img_bytes).decode()
    return img_b64

import cv2
import numpy as np

def embed_watermark(input_image, watermark_image, position='center', size_ratio=0.2, alpha=0.8):
    if input_image and watermark_image and size_ratio > 0:
        # Convert FileStorage to numpy array
        input_img = np.frombuffer(input_image.read(), np.uint8)
        watermark_img = np.frombuffer(watermark_image.read(), np.uint8)

        # Convert numpy array to image
        img = cv2.imdecode(input_img, cv2.IMREAD_COLOR)
        watermark = cv2.imdecode(watermark_img, cv2.IMREAD_UNCHANGED)

        # Get input image dimensions
        img_height, img_width = img.shape[:2]

        # Calculate the size of the watermark based on the input image size and the specified ratio
        watermark_height = int(img_height * size_ratio)
        watermark_width = int(img_width * size_ratio)
        watermark_resized = cv2.resize(watermark, (watermark_width, watermark_height))

        # Remove alpha channel if present
        if watermark_resized.shape[2] == 4:
            watermark_resized = watermark_resized[:, :, :3]

        # Calculate the position of the watermark based on the specified position
        if position == 'center':
            x_offset = (img_width - watermark_width) // 2
            y_offset = (img_height - watermark_height) // 2
        elif position == 'top_left':
            x_offset = 0
            y_offset = 0
        elif position == 'top_right':
            x_offset = img_width - watermark_width
            y_offset = 0
        elif position == 'bottom_left':
            x_offset = 0
            y_offset = img_height - watermark_height
        elif position == 'bottom_right':
            x_offset = img_width - watermark_width
            y_offset = img_height - watermark_height
        else:
            raise ValueError("Invalid position")

        # Overlay the watermark onto the input image
        watermarked_img = img.copy()
        watermarked_img[y_offset:y_offset+watermark_height, x_offset:x_offset+watermark_width] = \
            cv2.addWeighted(img[y_offset:y_offset+watermark_height, x_offset:x_offset+watermark_width], alpha, watermark_resized, 1 - alpha, 0)
        
        return watermarked_img



def compress_image(input_image, quality = 50):
    if input_image:
        data = input_image.read()
        initial_size = len(data)

        # Convert data to numpy array
        input_img = np.frombuffer(data, np.uint8)

        # Convert numpy array to image
        img = cv2.imdecode(input_img, cv2.IMREAD_COLOR)

        output_path = './static/images/' + 'output.jpeg'
        
        cv2.imwrite(output_path, img, [cv2.IMWRITE_JPEG_QUALITY, int(quality*95/100)])

        final_size = os.path.getsize(output_path)

        reduction = 100 * (initial_size - final_size) / initial_size

        return output_path, initial_size, final_size, reduction
    return './static/images/output.jpeg', 0, 0, 0


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        input_img = request.files.get("input_img")
        watermark = request.files.get("watermark")
        position = request.form.get("position", 'bottom_right')
        size_ratio = float(request.form.get('size_ratio', 0.25))
        alpha = float(request.form.get('alpha', 0.7))
        watermarked_img = embed_watermark(input_img, watermark, position, size_ratio, alpha) 
        img_b64 = numpy_img_to_base64(watermarked_img)

        return jsonify({
            'output_img': img_b64
        })

    else:
        return render_template('watermark.html')
    
@app.route('/compress', methods=['POST', 'GET'])
def compress():
    if request.method == 'POST':
        input_img = request.files.get("input_img")
        quality = int(request.form.get('quality', 50))

        output_path, initial_size, final_size, reduction = compress_image(input_img, quality)

        return jsonify({
            'output_path': output_path,
            'initial_size': initial_size,
            'final_size': final_size,
            'reduction': reduction
        })
    
    else:
        return render_template('compress.html')

if __name__ == '__main__':
	app.run(debug=True)
