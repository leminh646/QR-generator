# QR Code Generator (Python)

A simple Python application that generates a QR code from a URL you provide.  
The program prompts you for a URL and optionally lets you name the output file.

---

## Features
- Generates a QR code from any URL.
- Saves the QR code as a `.png` image.
- Lets you choose the filename (defaults to `qrcode.png`).
- Uses customizable QR code settings (size, error correction, box size, border).

---

## Requirements
- Python 3.7+
- [qrcode](https://pypi.org/project/qrcode/) library (with Pillow for image support)

Install dependencies:
```bash
pip install qrcode[pil]
```

## Usage
1. Clone or download this repository
2. Run the script
    ```bash
    python main.py
    ```
3. Enter URL when prompted:
    ```
    Enter a URL: https://example.com
    ```
4. Optionally provide a filename(without extension):
    ```
    Name your QR Code (Optional): my_code
    ```
    The file will be saved as `my_code.png`
    
    If no filename is provided, it defaults to `qrcode.png`


## Notes
- You can adjust the QR code's size, error correction, box size, and border inside the script
- The generated QR codes are standard and scannable with most devices