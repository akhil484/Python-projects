import qrcode


img = qrcode.make('https://github.com/akhil484')
img.save("qr_code.png")
