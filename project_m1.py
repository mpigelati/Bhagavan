import subprocess
import os

subprocess.call('git status > git_info.txt',shell=True)

def Fun_To_Remove_Syntax(temp):
	temp1 = temp.lstrip(" ").lstrip("\t").rstrip("\n")
	return temp1

def Fun_To_List_files(Fd):
    Zip=[]
    P_list = Fd.readlines()
    count=len(P_list)
    for i, line in enumerate(P_list):
	line = line.rstrip()
        if(line !='\n'):
            if "modified:" in line :
                temp = "".join(line.strip( ).split(':')[1])
                temp = Fun_To_Remove_Syntax(temp)
		Zip.append(temp)
            elif "Untracked" in line:
		for j in range(i+3, count):
			if (P_list[j].isspace() == False):
				Zip.append(P_list[j])	
			else:
				return Zip
				break
				

def Fun_To_open_File(Filename,mode):
    try:
        fd= open(Filename,mode)
    except:
        print("unable to open file")
        exit(1)
    else:
        return fd


zip=[]

Fd = Fun_To_open_File("git_info.txt","r")

zip = Fun_To_List_files(Fd)

string= "tar -rvf patch.tar " +" ".join(zip)

subprocess.call(string,shell=True)

