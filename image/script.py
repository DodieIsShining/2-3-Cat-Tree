import qrcode
import qrcode.constants


def create(texte):
    qr = qrcode.QRCode(version = 1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
    qr.add_data(texte)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="blue", back_color="white")
    return qr_img

txt = "https://agir.wwf.fr/stopextinction/tortue/"
image = create(txt)
image.save("qr.png")


