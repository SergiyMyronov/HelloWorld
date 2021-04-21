import qrcode
import cv2 as cv


def build_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode001.png')


# build_qr({'1': 1})
build_qr('\nHow to Generate and Decode QR Codes in Python:\n'+
         'https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0')


def decode_qr(fp: str):
    im = cv.imread(fp)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    return retval


print(decode_qr('qrcode001.png'))
