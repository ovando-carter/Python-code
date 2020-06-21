## Parameters and Arguments
from record_library import place_record, rotate_record, drop_needle

def play_record(album):
  place_record(album)
  rotate_record(album)
  drop_needle(album)

next_album = "Blondie / Parallel Lines"

play_record(next_album)

## None: It's Nothing!
# None is falsy, meaning that it evaluates to False in an if statement

from review_lib import get_next_review, submit_review

# define review here!
review = get_next_review()

if review is not None: # checks if review contains a value that isn’t None
  submit_review(review) # submits it by calling submit_review()

# Default Return
# store the result of this print() statement in the variable prints_return
prints_return =  print("What does this print function return?")

# print out the value of prints_return
print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]

list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return
print(list_sort_return)

# Default Arguments
import os

def make_folders(folders_list, nest = False): # set a default value to prevent error if someone forgets to input a value here. 
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = "."
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        print(path_to_new_folder)
        os.makedirs("./" + path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)

      except FileExistsError:
        continue

make_folders(['Music', 'fun', 'parliament'])

# Using Keyword and Positional Arguments

import reqs as requests
from bs4 import BeautifulSoup

def get_id(html_id, website="http://coolsite.com"): # any default value need to be listed in the last in out function definition
  request = requests.get(website)
  parsed_html = BeautifulSoup(website.content, features="html.parser")
  return parsed_html.find(id_=html_id)

# Keyword Arguments
import shapes

def draw_shape(shape_name="box", character="x", line_breaks=True):
  shape = shapes.draw_shape(shape_name, character)
  if not line_breaks:
    print(shape[1:-1])
  else:
    print(shape)

# call draw_shape() with keyword arguments here:
draw_shape(character="m", line_breaks=False) # you can make sure that the information goes to the right place by making it equal to the argument you wish to pass. 

# Using None as a Sentinel
def update_order(new_item, current_order=None):
  if current_order is None:
    current_order=[]

  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)

# Unpacking Multiple Returns
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper =scream_and_whisper("Unpacking Multiple Returns")

# Positional Argument Unpacking
from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += '/' + arg
  return joined_string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))


# Keyword Argument Unpacking
# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(
	name="Ovando", feeling="happy"
))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict): #product_dict is a key word argument that takes in a dictionary of key words. Denoted by the **.
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  Baseball=3,
  Shirt=14,
  Guitar=70,
)

# Using Both Keyword and Positional Unpacking
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))
