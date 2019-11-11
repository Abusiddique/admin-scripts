import os, subprocess

del_dir = r'c:\\windows\\temp'

# command to delete the files in temp directory


#pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
# recreate the deleted parent dir in case it get deleted
os.makedirs(del_dir)

rTup = pObj.communicate()
rCod = pObj.returncode

if rCod == 0:
    print 'Success: Cleaned Windows Temp Folder'
else:
    print 'Fail: Unable to Clean Windows Temp Folder'