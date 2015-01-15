import PIL
from PIL import Image
import os.path  
<<<<<<< HEAD
from PIL import Image, ImageDraw
def Logo(original_image,logo):
    width, height = original_image.size
    watermark = Image.open(logo)
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,50))
    result.paste(original_image, (0,0), mask=watermark)
    return result
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
=======
def main():
    directory = os.path.dirname(os.path.abspath(__file__))  
    watermark_file = os.path.join(directory, 'watermark.png')  
    Original_File = os.path.join(directory, 'Fire.jpg')
    # opens the image
    main = Image.open(Original_File)
    secondary = Image.open(watermark_file)
    
     # The Regular size
    width, height = main.size
    #a mask is created
    watermark = Image.new("RGBA", main.size)
    watermark.im.paste(watermark_file, None)
    #pastes the watermark onto the mask
>>>>>>> origin/master
    
    #makes the logo white and black
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    #makes the alpha
    watermark.putalpha(watermask)
    #pastes the watermark onto the original picture
    main.paste(watermark, None, watermark)
    #saves the picture
    main.save("watermarked.jpg", "JPEG")
    return main

def get_images(directory=None):

    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
