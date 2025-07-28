from flask import Flask, request, render_template, send_from_directory, url_for
import os
from rapidocr import RapidOCR

app = Flask(__name__)
engine = RapidOCR()

# Ensure upload and generated_imgs directories exist
os.makedirs('uploads', exist_ok=True)
os.makedirs('generated_imgs', exist_ok=True)

@app.route('/')
def index():
    return render_template('home.html', gen_img_url=None)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    if file:
        img_path = os.path.join('uploads', file.filename)
        gen_img_path = os.path.join('generated_imgs', file.filename)
        file.save(img_path)
        result = engine(img_path, return_word_box=True, return_single_char_box=True)
        result.vis(gen_img_path)
        gen_img_url = url_for('generated_img', filename=file.filename)
        orig_img_url = url_for('uploaded_img', filename=file.filename)
        return render_template('home.html', gen_img_url=gen_img_url, orig_img_url=orig_img_url)
    return "Something went wrong", 500

@app.route('/uploads/<filename>')
def uploaded_img(filename):
    return send_from_directory('uploads', filename)

@app.route('/generated_imgs/<filename>')
def generated_img(filename):
    return send_from_directory('generated_imgs', filename)

# ...existing code...
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)