# PDF to TIFF (Fax Support) Convertor using Flask

This project provides a web application built with Flask that allows users to upload PDF files, which are then converted to TIFF format (with fax support) using the pdf2image library.

## Features

- Upload a PDF file
- Convert the PDF file to an TIFF file
- Download the converted TIFF file
- Display a loading spinner while the file is being converted
- Reset the form to perform another conversion

## Requirements

- Python 3.12.4
- Flask
- pdf2image
- Pillow

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/imrkaofficial/convert_into_tiff.git
    cd convert_into_tiff


2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install the required packages:
    ```sh
    pip install -r requirements.txt

4. Install Poppler (required for pdf2image):
- macos
    ```sh
   brew install poppler

- Ubuntu/Debian:
    ```sh
    sudo apt-get install poppler-utils



## Usage

1. Start the Flask server:
    ```sh
    python app.py

2. Open your web browser and navigate to http://127.0.0.1:7001.

3. Upload the PDF file.
    - Click on the "Choose File" button and select a PDF file from your computer.
    - Click on the "Convert" button to start the conversion proces

4. Download the converted TIFF file:
    - Once the conversion is complete, a download link will appear. Click on it to download the converted TIFF file.

5. To perform another conversion, click the "Try Again" button to reset the form.

 
# License
This project is licensed under the [MIT License](/LICENSE).