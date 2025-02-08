# QR Code encoder and Decoder
import qrcode
img = qrcode.make('Muhammad Danish Zohaib, Student of GIAIC, Governor House Sindh, Karachi')
img.save('my_qr.png')


import cv2
img = cv2.imread('my_qr.png')
detector = cv2.QRCodeDetector()
V1, V2, V3 = detector.detectAndDecode(img)
print(V1)
