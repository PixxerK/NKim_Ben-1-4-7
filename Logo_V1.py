import PIL
from PIL import Image
import os.path 
from PIL import Image, ImageDraw
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
