import os
import json

import keyboard



title = ""
content = ""

def get_title():
    title = input("give the txt file a title:")
    return title


    

def get_content():
    content = input("what should stand in there ?:")
    return content



#title = get_title() 
#content_input = get_content() 
# create txt file with title and content from the user input
def create_paper(title, content_input):
    f = open(f"{title}.txt", "x")
    f.write(content_input)
    f.close()
    
        
#open the file with the given title
def open_paper(title):
    f = open(f"{title}.txt", "r")
    print(f.read())


# add context to the file that allready exist

def add_more_to_the_file(title):
    f= open(f"{title}.txt.", "a")
    new_content = input("what would u like to add ?")
    f.write(new_content)
    f.close



#input for text file to pick


opening_title = ""
# setting openting title to the tile from open paper function
def what_file_to_open(opening_title):
    opening_title = input("what is the file name u want to show")
    open_paper(title=opening_title)


# text if the function works what_file_to_open(opening_title=opening_title)

    

add_more_to_the_file(title="okayt")

