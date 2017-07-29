#print ("hellow world")
import subprocess
import os
#subprocess.call()
#subprocess.call(("ls","-la"))
#list_comm_1 = ("ls","-la")
#list_comm = ("git","status",">","samp.txt")
#subprocess.call(list_comm)

os.system("git status > status.txt")

#print(subprocess(["cat",""]))
def Fun_print_file(Fd):
    Zip=[]
    #print ("please print file content")
    P_list = Fd.readlines()
    count=0
    for line in P_list:
        count= count+len(line)
        #print("Count",count)
        #print (line)
        if(line !='\n'):
            if "modified:" in line :
                #print("line ",line)
                temp = "".join(line.strip( ).split(':')[1])
                #print("temp",temp)
                Zip.append(temp)
                #print("Zip",Zip)
            elif "Untracked files:"in line:
                print("count",count)
                print("you are in else statement")
                #S_lines = Fd.readlines(200)
                #print(S_lines)

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