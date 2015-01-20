import PIL
import os.path  
from PIL import Image
import Image

def Transparency():
    img = Image.open('watermark.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("watermark2.png", "PNG")
    return

def waterM(pic):
    #can only apply to one photo at a time.
    directory = os.path.dirname(os.path.abspath(__file__))  
    watermark_file = os.path.join(directory, 'watermark2.png')
    
    # opens the image
    #mainImg = Image.open(pic)
    secondary = Image.open(watermark_file)
    img2 = secondary.resize(pic.size)
    
    #a mask is created
    watermark = Image.new("RGBA", pic.size)
    
    #pastes the watermark onto the mask
    watermark.paste(img2,(0,0))
    
    #makes the logo white and black
    watermask = watermark.convert("L").point(lambda x: min(x, 255))
    
    #makes the alpha
    watermark.putalpha(watermask)
    
    #pastes the watermark onto the original picture
    result = PIL.Image.new('RGBA', pic.size, (0,0,0,0))
    result.paste(pic, None, watermark)
    return result

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

def waterM_apply(directory=None):  
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
        print image_list[n]
        new_image = waterM(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    