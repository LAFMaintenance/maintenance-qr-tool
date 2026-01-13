"""
    Author: Christopher Gross
    Purpose: Class used to create usable QR codes 
"""

import qrcode
from urllib.parse import urlparse
from PIL import Image, ImageDraw, ImageFont

class QrEngine:
    box_size = 12

    def __init__(self):
        self.canvas = None
        self.asset_output = None
        self.document_type = None

    def generate_qr(self, data, box_size, document_type, asset_output):
        self.asset_output = asset_output
        self.document_type = document_type
         #getting into image generation of the QR Code
        qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=box_size, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        qr_width, qr_height = img.size
        label_height = 60
        canvas = Image.new("RGB", (qr_width, qr_height + label_height),(255,255,255))
        canvas.paste(img,(0,0))
        label_text = document_type

        #Draw the QR Code with "Label"
        font_size = qr_width // 14
        font = ImageFont.truetype("arial.ttf", font_size)
        draw = ImageDraw.Draw(canvas)
        label_top = qr_height
        bbox = draw.textbbox((0,0), label_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (qr_width - text_width) // 2 - bbox[0]
        y = label_top + (label_height - text_height) // 2 - bbox[1]
        draw.text((x,y),label_text, fill="black", font=font)

        return canvas
    
    def save(self, canvas):
        #save the QR Code
        canvas.save(f"{self.asset_output}_{self.document_type}.png")

    def output(self):
        #provide output to tell the user filename
        print(f"Your QR Code was saved as {self.asset_output}_{self.document_type}.png")
