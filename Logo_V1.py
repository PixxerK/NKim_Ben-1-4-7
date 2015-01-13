import PIL
import os.path  
import PIL.ImageDraw
def Apply_logo(original_image,logo_file):
    directory = os.path.dirname(os.path.abspath(__file__))  
    logo_file = os.path.join(directory, 'Monster_logo.png')
    width, height = original_image.size
    #you need to use the paste function to put imgages on to the mask
    #top right corrner positioning
    #20 transparentcy on the mask
    #Instead we're going to do a watermark.
    #We're pasting the image that's a little transparent on top.
    #start with transparent mask
    logo = PIL.Image.new('RGBA', (width, height), (127,0,127,80))
    original_image = PIL.ImageDraw.Draw(Apply_logo)
    
                          
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=logo)
    return result
def get_images(directory=None):
    if directory == None:
        directory = os.getcwd()
        
    image_list = []
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass
    return image_list, file_list  
def apply_logo_all_images(directory=None):
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
        new_image = Apply_logo(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 