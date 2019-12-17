
import requests
from bs4 import BeautifulSoup
import pprint
import collections
from os import walk, listdir
import os
from os.path import join, isfile
import difflib
import shutil

mypath = 'your_path'
mypath_new = 'your_path_for_new_folder' 
url = 'your_url'
name_to_replace = 'name to replace'
new_folder_name = os.path.join(mypath_new, 'new folder name')

header_class = "episode-list-title tw-mb-1 link lg:tw-leading-none tw-font-bold tw-text-xl md:tw-text-lg lg:tw-text-xl lg:tw-mb-0 tw-flex tw-items-center tw-mr-3"
div_class = "episode-list-details"

def start_scrape(url, class_name):
    my_lists = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #print(soup)
    for i in soup.findAll('div', attrs={'class' : class_name}):
        content = i.find('a').contents[0]
        my_lists.append(content.strip())
    return dict(zip(my_lists, range(1, len(my_lists) + 1)))
   
def start_renaming(pairs):
    if not isinstance(pairs, dict):
        raise TypeError
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    keepcharacters = (' ','.','_', '-')

    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)

    for file in onlyfiles:
        search = file.replace(name_to_replace, '')
        rename = difflib.get_close_matches(search, pairs.keys(), n = 1)[0]
        print(pairs)
        if rename:
            old_path = os.path.join(mypath, file)
            extension = os.path.splitext(file)[1]
            new_filename = str(pairs[rename]) + '-' + rename + extension
            new_filename = ''.join(c for c in new_filename if c.isalnum() or c in keepcharacters).rstrip()
            new_path = os.path.join(mypath, new_filename)
            os.rename(old_path, new_path)
            print("renamed with pos ", pairs[rename])
            shutil.move(new_path, new_folder_name)


mydict = start_scrape(url, div_class)
sorted_dict = collections.OrderedDict(mydict)
               
 
start_renaming(mydict)
