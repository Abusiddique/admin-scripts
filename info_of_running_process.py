"""
Program to get list of running process, grep a specific program
and display its details
"""

import subprocess, string

def get_status_output(*args, **kwargs):
    # perform a ps command and assign results to a list
    p = subprocess.Popen(*args, **kwargs)
    output, _ = p.communicate()
    return output

try:
    program = input("Enter the name of the program to check: ")
    output = get_status_output('ps -f | grep "%s"' % program, stdouts=subprocess.PIPE, shell=True)
    program_info = string.split(output)

    #display results
    print("\n Full path:\t\t", program_info[5],
           "\n Owner:\t\t\t", program_info[0],
           "\n Process ID:\t\t", program_info[1],
           "\n Parent process ID:\t", program_info[2],
           "\n Time started:\t\t", program_info[4])
except:
    print("There was a problem with the program.")