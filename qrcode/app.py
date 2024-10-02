import qrcode

def generate_qr(text):
    qr= qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4 
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color= "black", back_colod = "white")
    img.save("qrimage.png")

generate_qr("https://google.com")
