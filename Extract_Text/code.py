from pdf2image import convert_from_path, convert_from_bytes


import tempfile

with tempfile.TemporaryDirectory() as path:
    # images_from_path = convert_from_path('sample.pdf', output_folder=path)
    images = convert_from_path('sample.pdf', grayscale=True, fmt='png')
    print(type(images[0]))