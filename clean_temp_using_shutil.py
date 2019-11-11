"""
Script to clean all temp files in windows temp directory
to improve performance of system

This script uses subprocess package
"""

import os,shutil

def clean_directory(directory_path):
	'''
	Function to delete files in given directory along with sub directories

	Input:
		directory path to be delted
	Output:
		return_code - 0(success), 1(failure)
	'''
	# Iterate through the directory
	for file_in_dir in os.listdir(directory_path):
		# If it is a file remove the file
		if os.path.isfile(file_in_dir):
			os.remove(file_in_dir)
		# If it is a directory remove the directory and delete files in it
		elif os.path.isdir(file_in_dir)
			shutil.rmtree(file_in_dir, ignore_errors=True)

clean_directory(r'c:\\windows\\temp')
