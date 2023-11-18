import cv2
import pyzbar.pyzbar as pyzbar


def decode_barcode(image_path):
    image = cv2.imread(image_path)
    barcodes = pyzbar.decode(image)
    
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        print(f"Barcode Type: {barcode_type}, Barcode Data: {barcode_data}")

if __name__ == "__main__":
    image_path = "C:/Users/VeerabhadraSharma/OneDrive - Accelalpha Software Pvt. Ltd/Desktop/image.jpg"
    decode_barcode(image_path)
