import qrcode

def genereate_qr(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1, # size of the QR code (1 = 21x21)
        error_correction=qrcode.constants.ERROR_CORRECT_H, # error correction level
        box_size=10, # size of each box in pixels   
        border=4, # thickness of border
    )

    # Add data
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save to file
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    url_input = input("Enter a URL: ")
    output_file = input("Name your QR Code (Optional): ")
    if output_file:
        output_file += '.png'
    genereate_qr(url_input, output_file)