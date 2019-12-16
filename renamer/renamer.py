import os

path = 'your_path'

os.chdir(path)
files = filter(os.path.isfile, os.listdir(path))
files = [os.path.join(path, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getctime(x))

i = 1
to_replace = 'Testing Jargon- '
for file in files:
    # print(file + ' ' + str(os.path.getmtime(file)))
    old_name = file
    new_name = old_name.replace(to_replace, str(i) + '-')
    os.rename(old_name, new_name)
    i += 1
