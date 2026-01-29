import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=2,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,)

qr.add_data("https://drive.google.com/drive/folders/1y6ZICLYvFwPScIMSGSqGsgYxdgzoz5G6?usp=drive_link")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_configurado.png")




###"https://docs.google.com/forms/d/e/1FAIpQLSdWEldXWb22rzxD116OQ0A0FqYtTK5vGbrrHHyCpbDVkN0b9g/viewform?usp=dialog"