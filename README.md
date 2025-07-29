# OCR App

A modern Optical Character Recognition (OCR) application built with a focus on accuracy, speed, and ease of use.

## Features

- Extracts text from images and PDFs
- Supports multiple languages
- Batch processing of files
- User-friendly interface
- Export results to various formats (TXT, CSV, PDF)
- Configurable OCR settings

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/shrinidhi-a/ocr-app.git
    cd ocr-app
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
    or
    ```bash
    pip install -r requirements.txt
    ```
    *(Choose the command based on your tech stack)*

## Usage

1. Start the application:
    ```bash
    npm start
    ```
    or
    ```bash
    python main.py
    ```
2. Upload images or PDFs.
3. Click "Extract Text" to process files.
4. Review and export the results.

## Configuration

- Edit `config.json` to adjust OCR settings (e.g., language, output format).
- For advanced options, refer to the documentation in the `docs/` folder.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a pull request

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- Community contributors
