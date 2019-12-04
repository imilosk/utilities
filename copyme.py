import os
import glob
from shutil import copy
from argparse import ArgumentParser
from art import tprint, aprint, art
import copier
def pass_args():
    parser = ArgumentParser()
    parser.add_argument("-s", "--source", dest="source", help="Pass the source file, IMPORTANT PUT THIS FILE IN THE SAME FILE AS THE SCRIPT", metavar="SOURCE")
    parser.add_argument("-p", "--path", dest="path", help="Pass the path where you want the files from", metavar="PATH")
    parser.add_argument("-k", "--keyword", dest="keyword", help="If you have only 1 keyword/file to search, pass it.", metavar="KEYWORD")
    parser.add_argument("-m", "--my_path", dest="mypath", help="Add this if you want to copy it to special place, if not specified will copy in the same dir as the script", metavar="MYPATH")
    parser.add_argument("-i", "--images", dest="images", help="private copier", metavar="IMAGES")

    return parser.parse_args()

class copyFiles(object):
    def __init__(self, args):
        self.args = args
        self.path_to_copy = os.path.abspath(str(self.args.path))
    def copy_from_text(self):
        self.file_text = str(self.args.source)
        with open(self.file_text, 'r') as file:
            for row in file:
                for root, _, files in os.walk(self.path_to_copy):
                    for file in files:
                        if row in file:
                            if self.args.mypath:
                                self.path_to_paste = self.args.mypath
                                file_path = os.path.join(root, file)
                                os.makedirs(self.path_to_paste, exist_ok=True)
                                copy(file_path, self.path_to_paste)
        aprint("love_you", number=1, text="Copying done!")

    def copy_from_keyword(self):
        self.keyword = self.args.keyword
        for root, dirs, files in os.walk(self.path_to_copy):
            for file in files:
                if self.keyword in file:
                    if self.args.mypath:
                        self.path_to_paste = self.args.mypath
                        file_path = os.path.join(root, file)
                        os.makedirs(self.path_to_paste, exist_ok=True)
                        copy(file_path, self.path_to_paste)
        aprint("love_you", number=1, text="Copying done!")

    def milos_copy(self):
        path = '\\\\192.168.10.1\\Graphics\\Drive Backup\\'
        with open('./kits.txt', 'r') as file:
            for row in file:
                image = row.split(',')[1]
                image = image[3:]
                image = image.strip()
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if image in file:
                            image_path = os.path.join(root, file)
                            my_path = image_path[len(path):image_path.rfind('\\')]
                            my_path = os.path.join(os.getcwd(), my_path)
                            os.makedirs(my_path, exist_ok=True)
                            copy(image_path, my_path)

if __name__ == "__main__":
    copyF = copyFiles(pass_args())
    if copyF.args.images:
        tprint("MILOS",font="block",chr_ignore=True)
        copyF.milos_copy()
    elif copyF.args.source:
        tprint("coPyMe", font="bulbhead")
        copyF.copy_from_text()
    elif copyF.args.keyword:
        tprint("coPyMe", font="bulbhead")
        copyF.copy_from_keyword()
    else:
        tprint("Please add arguments :)", font="rnd-small")
