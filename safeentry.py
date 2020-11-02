from PIL import Image, ImageFont, ImageDraw 
 
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''        
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)    
    return lines
 
 
def draw_text(text):    
    # open the background file
    img = Image.open('block.png')
    
    # size() returns a tuple of (width, height)
    image_size = img.size
 
    # create the ImageFont instance
    font_file_path = '12.ttf'
    font = ImageFont.truetype(font_file_path, size=60, encoding="unic")
 
    # get shorter lines
    lines = text_wrap(text, font, image_size[0])
    return lines # ['This could be a single line text ', 'but its too long to fit in one. ']

# draw_text("MASSIMO DUTTI - MARINA SQUARE")
# lines = ['MASSIMO DUTTI - ', 'MARINA SQUARE ']

def shortcreate_image(place):
    lines = draw_text(place) #list of words
    #open image
    my_image = Image.open("template.png")
    #open font
    title_font = ImageFont.truetype('12.ttf', 60)
    image_editable = ImageDraw.Draw(my_image)
    extention = '.png'
    filename = place+extention
    y_coords = 760
    line_height = title_font.getsize('hg')[1]
    for i in lines:
        #position
        w, h = image_editable.textsize(i, title_font)
        left = (my_image.width - w) / 2
        # coords -- text -- color -- font
        image_editable.text((left,y_coords), i, (0, 0, 0), font = title_font)
        y_coords = y_coords + line_height
        #saving
        my_image.save(filename)

def longcreate_image(place):
    lines = draw_text(place) #list of words
    #open image
    my_image = Image.open("template.png")
    #open font
    title_font = ImageFont.truetype('12.ttf', 56)
    image_editable = ImageDraw.Draw(my_image)
    extention = '.png'
    filename = place+extention
    y_coords = 740
    line_height = title_font.getsize('hg')[1]
    for i in lines:
        #position
        w, h = image_editable.textsize(i, title_font)
        left = (my_image.width - w) / 2
        # coords -- text -- color -- font
        image_editable.text((left,y_coords), i, (0, 0, 0), font = title_font)
        y_coords = y_coords + line_height
        #saving
        my_image.save(filename)


longplaces = ["BEDOK COMMUNITY CENTRE",
"CATHAY CINELEISURE ORCHARD",
"CHUNG CHENG HIGH SCHOOL (MAIN)",
"TAMPINES MERIDIAN JUNIOR COLLEGE",
"ANDERSON SERANGOON JUNIOR COLLEGE",
"FOOD JUNCTION MANAGEMENT PTE. LTD.",
"ANGLO-CHINESE SCHOOL (INDEPENDENT)",
"MARINA BAY FINANCIAL CENTRE TOWER 3",
"NTUC FAIRPRICE FINEST - MARINE PARADE",
"NTUC FAIRPRICE FINEST - THOMSON PLAZA",
"UNITED SQUARE, THE KIDS LEARNING MALL",
"NUS HIGH SCHOOL OF MATHEMATICS AND SCIENCE"]

# shortplaces = []


for place in longplaces:
    longcreate_image(place)


# for place in shortplaces:
#     shortcreate_image(place)