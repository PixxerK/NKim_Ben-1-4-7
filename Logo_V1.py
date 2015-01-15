import PIL
import os.path  
from PIL import Image, ImageDraw
def main():
    directory = os.path.dirname(os.path.abspath(__file__))  
    watermark_file = os.path.join(directory, 'watermark.png')  
    Original_File = os.path.join(directory, 'Fire.jpg')
    # opens the image
    main = Image.open(Original_File)
    secondary = Image.open(watermark_file)
    secondary.resize(main.size)
    #a mask is created
    watermark = Image.new("RGBA", main.size)
    #pastes the watermark onto the mask
    watermark.paste(secondary,(0,0))
    #makes the logo white and black
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    #makes the alpha
    watermark.putalpha(watermask)
    #pastes the watermark onto the original picture
    main.paste(watermark, None, watermark)
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
def main_apply(directory=None):  
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with radius = 30% of short side
        new_image = main()
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    