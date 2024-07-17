from flask import Flask, request, redirect, url_for, send_file, render_template
from werkzeug.utils import secure_filename
import os
from pdf2image import convert_from_path
import logging

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['CONVERTED_FOLDER'] = 'converted'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Ensure the upload and converted folders exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['CONVERTED_FOLDER']):
    os.makedirs(app.config['CONVERTED_FOLDER'])

# Configure logging
logging.basicConfig(level=logging.INFO)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        if 'file' not in request.files:
            logging.error("No file part")
            return 'No file part', 400

        file = request.files['file']
        if file.filename == '':
            logging.error("No selected file")
            return 'No selected file', 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Convert PDF to TIFF
            tiff_filename = secure_filename(os.path.splitext(filename)[0] + '.tiff')
            tiff_filepath = os.path.join(app.config['CONVERTED_FOLDER'], tiff_filename)
            images = convert_from_path(filepath)
            images[0].save(tiff_filepath, save_all=True, append_images=images[1:], compression="tiff_g4")

            return {'download_url': url_for('download_file', filename=tiff_filename)}

        logging.error("Invalid file type")
        return 'Invalid file type', 400

    except Exception as e:
        logging.exception("Error during file conversion")
        return f"An error occurred: {str(e)}", 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['CONVERTED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7001))
    app.run(debug=True, host='0.0.0.0', port=port)
