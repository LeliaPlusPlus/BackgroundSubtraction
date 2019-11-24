# Lelia Hampton
# Background Subtraction Using Frame Differencing
# This program separates the background image from
# the foreground image, using background subtraction
# and places a red bounding box around the foreground image.

# import the math library for our background subtraction methods
import math 

# this function reads a ppm file and returns
# a list of the width and height specified
# in the file with the rgb values in the list
# from the original/background ppm files
def read_files():
    
    # create original file object in read mode
    original_file = open("original.ppm", "r")

    # read the magic number of the file header
    magic = original_file.readline()

    # read the comment of the file header
    comment = original_file.readline()

    # read the width and height
    width_height = original_file.readline()
    # split the string and store in wh
    wh = width_height.split()
    # set width and height and convert to int    
    width = int(wh[0])
    height = int(wh[1])

    # read the largest possible value
    # of all the trailing numbers
    largest_possible = original_file.readline()

    # initialize empty list for original ppm file pixels
    original_list = []

    # iterature through the rest of the
    # lines in the original ppm file
    for line in original_file:
        original_line = line.split()
        for item in original_line:
            original_list.append(int(item))

    # divide the list into 3 by the length of the list
    original_list = [original_list[i:i+3] for i in range(0, len(original_list), 3)]

    original_file.close() # be nice and close the file


    # create background file object in read mode
    background_file = open("background.ppm", "r")

    # read the magic number of the file header
    magic = background_file.readline()

    # read the comment of the file header
    comment = background_file.readline()

    # read the width and height
    width_height = background_file.readline()
    # split the string and store in wh
    wh = width_height.split()
    # set width and height and convert to int    
    width = int(wh[0])
    height = int(wh[1])

    # read the largest possible value
    # of all the trailing numbers
    largest_possible = background_file.readline()

    # initialize empty list for original ppm file pixels
    background_list = []

    # iterature through the rest of the
    # lines in the original ppm file
    for line in background_file:
        background_line = line.split()
        for item in background_line:
            background_list.append(int(item))

    # divide the list into 3 by the length of the list
    background_list = [background_list[i:i+3] for i in range(0, len(background_list), 3)]    

    background_file.close() # be nice and close the file

    # return the width, height, original list, and background list
    return width, height, original_list, background_list 


# this function performs background subtraction
# on the original and background ppm files
def background_subtraction(original_list, background_list):
    foreground_list = [] # initialize empty foreground list

    threshold = 10 # threshold for background subtraction

    # iterate over the original and background list
    for i in range(len(original_list)):

        # calculate the distance between the pixels
        distance = math.sqrt ( ( ( original_list[i][0] - background_list[i][0] ) ** 2 ) \
                   + ( ( original_list[i][1] - background_list[i][1] ) ** 2 ) \
                   + ( ( original_list[i][2] - background_list[i][2] ) ** 2 ) )

        # if it is part of the background
        # (i.e. little to no difference between original and background)
        if distance <= threshold:
            # set the element in the forground list to white
            foreground_list.append( [255, 255, 255] )
        # if it is in the foreground
        # (i.e. threshold or greater difference between original and background)
        if distance > threshold:
            # set the element in the forground list to the
            # element in the same position in the original
            foreground_list.append( original_list[i] )
        
    
    return foreground_list # return the foreground list

# this function places a red box around the object
def red_box(width, height, foreground_list):

    # convert foreground list to a 3d list, so we
    # can get the width and height of the pixels
    # initialize empty list
    foreground_list_3d = [[0 for x in range(width)] for y in range(height)]
    x = 0 # to keep track of the index in the foreground_list
    for h in range(height):
        for w in range(width):
            foreground_list_3d[h][w] = foreground_list[x]
            x+=1

    # initialize our variables which determine
    # where we should draw a box around the object
    highest_width = 0
    lowest_width = width
    highest_height = 0
    lowest_height = height

    # iterate through the foreground 3d 
    # list to find the object bounds
    for h in range(height):
        for w in range(width):
            # if the pixel isn't white
            if (foreground_list_3d[h][w][0] != 255) and \
               (foreground_list_3d[h][w][1] != 255) and \
               (foreground_list_3d[h][w][2] != 255):
                # the following if statements are the min/max algorithm
                # if h is greater than the current highest height
                if h > highest_height: 
                    highest_height = h # set highest height to h
                if h < lowest_height:
                    lowest_height = h # set lowest height to h
                if w > highest_width:
                    highest_width = w # set highest width to w
                if w < lowest_width:
                    lowest_width = w # set lowest width to w

    # create red bound box in 3d array
    # start by incrementing the box boundaries by 1
    highest_width += 1
    lowest_width += 1
    highest_height += 1
    lowest_height += 1
    
    # let's do the top line:
    # check height bounds
    if 0 <= highest_height <= height:
        # iterate over the width values for the top line
        for w in range(lowest_width, highest_width+1):           
            # check width bounds
            if 0 <= w <= width: 
                # set the pixel to red
                foreground_list_3d[highest_height][w][0] = 255
                foreground_list_3d[highest_height][w][1] = 0
                foreground_list_3d[highest_height][w][2] = 0

    # let's do the bottom line:
    # check height bounds
    if 0 <= lowest_height <= height:
        # iterate over the width values for the bottom line
        for w in range(lowest_width, highest_width+1):
            # check width bounds
            if 0 <= w <= width: 
                # set the pixel to red
                foreground_list_3d[lowest_height][w][0] = 255
                foreground_list_3d[lowest_height][w][1] = 0
                foreground_list_3d[lowest_height][w][2] = 0

    # let's do the left line:
    # check height bounds
    if 0 <= lowest_width <= width:
        # iterate over the height values for the left line
        for h in range(lowest_height, highest_height+1):
            # check height bounds
            if 0 <= h <= height:
                # set the pixel to red
                foreground_list_3d[h][lowest_width][0] = 255
                foreground_list_3d[h][lowest_width][1] = 0
                foreground_list_3d[h][lowest_width][2] = 0

    # let's do the right line:
    if 0 <= highest_width <= width:
        # iterate over the height values for the right line
        for h in range(lowest_height, highest_height+1):
            # check height bounds
            if 0 <= h <= height:
                # set the pixel to red
                foreground_list_3d[h][highest_width][0] = 255
                foreground_list_3d[h][highest_width][1] = 0
                foreground_list_3d[h][highest_width][2] = 0
        
    # convert the 3d list back to a 2d list for file processing
    # update foreground list to have red box around object
    x = 0 # to keep track of the index in the foreground_list
    for h in range(height):
        for w in range(width):
            foreground_list[x] = foreground_list_3d[h][w]
            x+=1
    

    return foreground_list # return the foreground list

# this function writes and returns
# a ppm file for the foregound image
# it takes as an argument the foreground
# list which it will write to the file
def write_file(width, height, foreground_list):

    # create a foreground file object with write access 
    foreground_file = open("foregound.ppm", "w")

    # write the header of the foreground file
    foreground_file.write("P3\n")
    foreground_file.write("# Foreground image file\n")
    foreground_file.write(str(width) + " " + str(height) + "\n")
    foreground_file.write("255\n")

    num = 1 # flag to make sure we have 15 on a line
    # iterate through foreground_list
    for i in range(len(foreground_list)):
        # add foreground_list item to file
        foreground_file.write(str(foreground_list[i][0]) + " ")
        foreground_file.write(str(foreground_list[i][1]) + " ")
        foreground_file.write(str(foreground_list[i][2]) + " ")

        # if the flag is five 
        if num == 5:
            num = 0 # reset flag
            foreground_file.write("\n") # write new line

        num+=1 # increment flag

    foreground_file.close() # be nice and close the file


#driver code
def main():
    
    # call the read_files() function to get the weight,
    # height, original list, and background list
    width, height, original_list, background_list = read_files()

    # call the background_subtraction function to create a foreground list
    foreground_list = background_subtraction(original_list, background_list)

    # update the foreground list to include the red box
    foreground_list = red_box(width, height, foreground_list)

    # write a new file with the foreground and width/height
    write_file(width, height, foreground_list)


main() # call the main function
