from PIL import Image

def cropImage():
    # specify the path of the image-file which you want to blur
    imgPath = r"C:\Users\ajaya\OneDrive\Desktop\Python Projects\Image Processing\lion.jpg"
    img = Image.open(imgPath)
    
    cropBox = (0, 0, 300, 300)
    croppedImg = img.crop(cropBox)

    img.show()
    croppedImg.show()

cropImage()
