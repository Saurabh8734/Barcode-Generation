import barcode     #pip install python-barcode
from barcode.writer import ImageWriter
import pandas as pd
import qrcode
import os


# Defining the product class
class Product:
    def __init__(self, name, price, weight, exp_date, quantity): # exp_date
        self.name = name
        self.price = price
        self.weight = weight
        self.exp_date = exp_date
        self.quantity = quantity


# Barcode generation
def generate_barcode(product, output_dir = 'barcodes'):
    # Ensuring the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    # Generate a unique identifier for each product (can be based on SKU or other fields)
    product_code = f"{product.name[:3].upper()}_001"

    # Generate a code128 barcode (Std for product identification)
    barcode_format = barcode.get_barcode_class('code128')
    product_barcode = barcode_format(product_code, writer=ImageWriter())


    # Saving the barcode as an image
    barcode_filename = os.path.join(output_dir, f"{product.name}_barcode.png")
    product_barcode.save(barcode_filename)


    print(f"Barcode for {product.name} saved as {barcode_filename}")


if __name__ == "__main__":
    # Example products
    products = [
        Product("Apple", 1.00, 0.2),
        Product("Banana", 0.50, 0.15),
        Product("Milk", 1.50, 1.0),
    ]

    # Generate barcodes and QR codes for each product
    for product in products:
        generate_barcode(product)

    