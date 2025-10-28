import qrcode as qr

img = qr.make("https://maps.app.goo.gl/o63UvYK82Ce7Z5Wt7")

img.save("location.png")