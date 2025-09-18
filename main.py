import qrcode

url = "https://imaginative-hamster-c4ff88.netlify.app/"  # replace with your hosted page
qr = qrcode.make(url)
qr.save("breachpoint_qr.png")
