import qrcode
from PIL import Image
from datetime import datetime

qr = qrcode.QRCode(version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size=10, border=3 )
enter_data = input('Enter Data : ')
qr.add_data(enter_data);
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
# img.save(enter_data)

# Save the QR code with the link or text as its filename
output_file = f'{enter_data.replace("https://", "").replace("/", "_")}_{datetime.now().strftime("%Y_%m_%d_%H%M%S")}.png'
img.save(output_file)
