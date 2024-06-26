from pypdf import PdfReader, PdfWriter
from flask import Flask

# Write the provided pdf to be able to 
# do functions such as encrypt
def write_pages(write_pdf, read):
    for page in read.pages:
        write_pdf.add_page(page)

# Creates a new pdf to be returned
def new_pdf(write_pdf, new_user_file):
    with open(new_user_file, "wb") as output:
        write_pdf.write(output)

# This function encrypts a pdf with a password
def encrypt_pdf(write_pdf):
    # AES-256: gov adopted symmetric-key encryption algorithm
    write_pdf.encrypt("password", algorithm="AES-256")

# This function decrypts a encrypted pdf provided by the user
def decrypt_given_pdf(read, password):
    if read.is_encrypted:
        read.decrypt(password)

# extract images from a pdf
# this only takes in one page pdf though for now
# need to test this later
# also need to install optional dependencies
def extract_image(read):
    count = 0

    for image_file in read.images:
        with open(str(count) + image_file.name, 'wb') as f:
            f.write(image_file.data)
            count += 1




