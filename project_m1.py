#print ("hellow world")
import subprocess
import os
#subprocess.call('git status > git_info.txt',shell=True)

	
#os.system("git status > git_info.txt")

#print(subprocess(["cat",""]))
def Fun_Remove(My_list):
	length=len(My_list)
	
	for i in (1, length):
		My_list[i-1]=My_list[i-1].lstrip(" ").lstrip("\t").rstrip("\n")
	return My_list

def Fun_print_file(Fd):
    Zip=[]
    P_list = Fd.readlines()
    count=len(P_list)
    for i, line in enumerate(P_list):
	line = line.rstrip()
	#print i,  line
        if(line !='\n'):
            #print(line)
            if "modified:" in line :
                temp = "".join(line.strip( ).split(':')[1])
                Zip.append(temp)
            elif "Untracked" in line:
		#print "got untracked files"
		for j in range(i+3, count):
			#if (len(P_list[j]) > 0):
			if (P_list[j].isspace() == False):
				#print "===", P_list[j]
				Zip.append(P_list[j])	
			else:
				return Zip
				break
				

def Fun_open_File(Filename,mode):
    try:
        fd= open(Filename,mode)
    except:
        print("unable to open file")
        exit(1)
    else:
        #print("file opened success fully")
        return fd

zip=[]
Fd = Fun_open_File("git_info.txt","r")
#print(fd)
zip = Fun_print_file(Fd)
zip=Fun_Remove(zip)
#print ("Zip",zip)
string= "tar -rvf patch.tar " +" ".join(zip)
print ("string",string)

subprocess.call(string,shell=True)

