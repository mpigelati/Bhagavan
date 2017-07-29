#print ("hellow world")
import subprocess
import os
#subprocess.call()
#subprocess.call(("ls","-la"))
#list_comm_1 = ("ls","-la")
#list_comm = ("git","status",">","samp.txt")
#subprocess.call(list_comm)

#os.system("git status > status.txt")

#print(subprocess(["cat",""]))
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
		print "got untracked files"
		for j in range(i+3, count):
			#if (len(P_list[j]) > 0):
			if (P_list[j].isspace() == False):
				print "===", P_list[j]
			else:
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

Fd = Fun_open_File("status.txt","r")

Fun_print_file(Fd)
