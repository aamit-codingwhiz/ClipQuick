import os
import qrcode

QR_CODE_DIR = "static/qrcodes"

# Ensure the directory exists
os.makedirs(QR_CODE_DIR, exist_ok=True)

def generate_qr_code(short_code, base_url="http://127.0.0.1:5000"):
    """Generates and saves a QR code for the given short_code and returns the file path."""
    url = f"{base_url}/{short_code}"
    qr_filename = f"{short_code}.png"
    qr_path = os.path.join(QR_CODE_DIR, qr_filename)

    # Check if the QR code already exists
    if not os.path.exists(qr_path):
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(qr_path)

    return qr_filename  # Return the filename, not the full path
