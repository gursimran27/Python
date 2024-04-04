# pip install pyqrcode
# pip install pypng

import pyqrcode
import png

s="https://jwt.io/"
urls=pyqrcode.create(s) # this will create qrCode and store qrcode in urls
urls.png("r1.jpg",scale=6) #it will convert in picture form and store in r1.jpg file

