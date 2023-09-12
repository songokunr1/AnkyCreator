import pytesseract
from PIL import Image

# Open an image using PIL (Python Imaging Library)
image = Image.open(r'E:\Python\AnkyCreator\data\images\book.jpg')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)