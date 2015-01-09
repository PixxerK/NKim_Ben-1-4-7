import PIL
import os.path  
import PIL.ImageDraw
def Apply_logo(original_image, percent_of_side):
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    #start with transparent mask
    logo = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(Apply_logo)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
                         
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