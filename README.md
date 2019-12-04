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
`$python copyme.py -h` will give you the following result:
```python
usage: testing.py [-h] [-s SOURCE] [-p PATH] [-k KEYWORD]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Pass the source file
  -p PATH, --path PATH  Pass the path where you want the files from
  -k KEYWORD, --keyword KEYWORD
                        If you have only 1 keyword/file to search, pass it.
```
Example of running the script:
`python copyme.py -s /path/to/filestocopy.txt -p /copy/files/from/here`
or
`python copyme.py -k copyonlythisfile -p /copy/file/from/here`

I know, it's that simple :)
