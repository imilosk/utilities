```
              ____          __  __       
  ___   ___  |  _ \  _   _ |  \/  |  ___ 
 / __| / _ \ | |_) || | | || |\/| | / _ \
| (__ | (_) ||  __/ | |_| || |  | ||  __/
 \___| \___/ |_|     \__, ||_|  |_| \___|
                     |___/

```
Why bothering doing something when python can automate it? :) If you want to automatically copy file(s) from a directory on your network, or simply on your machine but you're too lazy, we got a script for you.
# How does it work?
Python simply takes your file with data, searches through the directory you've given it and copies it on your machine, if the directory already exists, it will copy it there, if not it'll make another one. 

## How to run coPyMe?

First we need to clone this project, simply do:

`$git clone https://github.com/imilosk/utilities`

Then we need to change directory and install the requirements.txt:
`$cd utilities 

`$pip3 install -r requirements.txt`

`$python copyme.py -h` will give you the following result:
```python
usage: copyme.py [-h] [-s SOURCE] [-p PATH] [-k KEYWORD]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Pass the source file
  -p PATH, --path PATH  Pass the path where you want the files from
  -k KEYWORD, --keyword KEYWORD
                        If you have only 1 keyword/file to search, pass it.
   -m MYPATH, --my_path MYPATH
                        Add this if you want to copy it to special place,
                        if not specified will copy in the same dir as the script
```

Example of running the script:

`$ python copyme.py -s /path/to/filestocopy.txt -p /copy/files/from/here`

or

`$ python copyme.py -k copyonlythisfile -p /copy/file/from/here`

I know, it's that simple :)

Example of running it on my machine:

```
PS C:\Users\Simeon\Desktop\New folder>python copyme.py -s "./copyme.txt" -p "C:\Users\Simeon\Desktop\copy_from_here" -m "C:\Users\Simeon\Desktop\New folder/paste_here"   
                                                                                                                                                                                              ___  _____  ____  _  _  __  __  ____
 / __)(  _  )(  _ \( \/ )(  \/  )( ___)
( (__  )(_)(  )___/ \  /  )    (  )__)
 \___)(_____)(__)   (__) (_/\/\_)(____)

»-(¯`·.·´¯)->Copying done!<-(¯`·.·´¯)-«
```
