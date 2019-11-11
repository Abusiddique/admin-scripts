import os,shutil
del_dir = r'c:\\windows\\temp'
for f in os.listdir(del_dir):
    if os.path.isfile(f):
        os.remove(f)
    elif os.path.isdir(f)
        shutil.rmtree(f, ignore_errors=True)