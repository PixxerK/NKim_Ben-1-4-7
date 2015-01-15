import PIL
from PIL import Image
import os.path  
def main(image):
     # Open the original image
    main = Image.open(image)
    Picture = Image.open('watermark.png')
    watermark = Image.new("RGBA", main.size)
    Image.resize(Picture)
    watermark.paste = (Picture, 0,0)
    

    watermask = watermark.convert("L").point(lambda x: min(x, 100))

    watermark.putalpha(watermask)
 
    image.paste(watermark, None, watermark)
    image.save("watermarked.jpg", "JPEG")

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

def Apply_logo(directory=None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.')
        new_image = main(image_list[n])
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 