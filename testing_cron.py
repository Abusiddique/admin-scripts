"""
Script to run python scripts as cron jobs
"""
import crontab

def create_cron_job(command_str):
	"""
	Function to run command as cron jobs
	"""
	try:
		cron    = crontab.CronTab()
		job = cron.new(command=command_str)
		job.minute.every(1)
		cron.write()
		
	except Exception as error:
		print("Exception occured: " + str(error))
		

def create_command(option):
	"""
	Function to create a command based on user selected option
	"""
	if option == 1:
		file_path = input("Please give the file path: \n")
		command_str = 'python ' + file_path
		create_cron_job(command_str)
		

while(True):
	option = int(input("Please select required action: \n 1. Create cron job for python script \n 2. Exit \n"))
	if option == 2:
		print("Exiting script execution")
		break
	elif option == 1:
		create_command(option)
	
		
		

