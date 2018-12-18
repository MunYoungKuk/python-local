import os

os.chdir(r'C:\Users\student\Downloads\SSAFY_지원자\SSAFY지원자')

for filename in os.listdir("."):
    os.rename(filename,"SSAFY_"+filename[8:])