import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("https://www.instagram.com/")

qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="blue")
img.save("wscube_wen.png")