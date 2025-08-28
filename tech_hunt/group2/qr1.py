import qrcode

qr = qrcode.QRCode()
qr.add_data("https://rudrasakhalava.github.io/techfest/tech_hunt/group2/level1.html")
qr.make()
qr.print_ascii()
