import qrcode

qr = qrcode.QRCode()
qr.add_data("http://192.168.68.105:8000/")
qr.make()
qr.print_ascii()
