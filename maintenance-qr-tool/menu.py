"""
    Author: Christopher Gross
    Purpose: This a class used to print/create a menu
"""


from urllib.parse import urlparse
from qr_engine import QrEngine

class QrMenu:
    engine = QrEngine()

    @staticmethod
    def url_is_valid(url):
        #used to validate the URL input
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    
    def print_menu():
        #used to provide valid choices for "types of documents"
        valid_types = {"1": "Manual",
                       "2": "Operator Instructions",
                       "3": "Schematics",
                       "4": "Parts List",
                       "5": "Website",
                       "6": "Common Issues"}
        #used for standardized choices for "QR code sizes"
        valid_sizes = {
            "1": {'name': "Small", "box_size": 4},
            "2": {'name': "Medium", "box_size": 6},
            "3": {'name': "Large", "box_size": 8}
        }
        while True:
            #get size of QR code to be made
            print("\nSelect QR code size")
            for key, val in valid_sizes.items():
                print(f"{key}: {val['name']}")

            user_choice = input("> ").strip()

            if user_choice in valid_sizes:
                box_size= valid_sizes[user_choice]["box_size"]
                break
            if not user_choice:
                print("Choice must be one from selection menu")
                continue
        while True:
            #input validation for URL
            data = input("Enter a link you would like to use: ")
            if not data:
                print("URL can not be empty")
                continue
            if not QrMenu.url_is_valid(data):
                print("URL must be valid")
                continue
            break
        while True:
            #menu for "type" of document
            print("\nSelect Document Type")
            for key, value in valid_types.items():
                print(f"{key}. {value}")
            choice = input("> ").strip()

            if choice in valid_types:
                document_type = valid_types[choice]
                break
            print("Invalid choice, please enter a number 1 -5")

        #clean up user input for "asset"
        asset = input("Enter asset name: ").strip()  
        asset_output = asset.replace(" ", "_")
        
        return {
            "data": data,
            "document_type": document_type,
            "box_size": box_size,
            "asset_output":asset_output,
        }

        