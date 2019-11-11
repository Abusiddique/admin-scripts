"""
Script to clean all temp files in windows temp directory
to improve performance of system

This script uses subprocess package
"""

import os, subprocess

def clean_directory(del_dir):
	'''
	Function to delete files in given directory along with sub directories

	Input:
		directory path to be delted
	Output:
		return_code - 0(success), 1(failure)
	'''
	
	# command to delete the files in temp directory clean files in the directory but do not delete subdirectories
	#pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

	# command to delete the files in temp directory clean files in the directory and delete subdirectories and parent directory
	pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)

	# recreate the deleted parent dir in case it get deleted
	os.makedirs(del_dir)

	return_value = pObj.communicate()
	return_code = pObj.returncode

try:
	return_code = clean_directory(r'c:\\windows\\temp')

	if return_code == 0:
	    print('Success: Cleaned Windows Temp Folder')
	else:
	    print('Fail: Unable to Clean Windows Temp Folder')
except Exception as error:
	print("Exception occured: " + str(error))