#!/usr/bin/python
import os;
import cgi;
import cgitb; cgitb.enable()
import re;

folder = "/var/lib/mailman/archives/public/mailman"
print "Content-type: text/html\n"
print "hello<BR>"

contents=[]

for (p,d,f) in os.walk(folder):
	contents.append(d)

r=range(0,10)# r=[0,.,9]
public_folders=[]
i=1
for d in contents:
	for name in d:
		ch=str(name)[0]
		for number in r:
			if ch==str(number):
				public_folders.append(name)
				print "<span style=\"background-color:yellow\">d-name:</span>",name,"<BR>"
			        i=i+1
#attach=folder+"/attachments"
#htmlfiles=(folder,file)#a tuple repr.
#public_folders.delete("attachments")
search_folders=[]
htmlfiles=[]
htmlfiles_paths=[]
i=1
for d in public_folders:
	if "-" in str(d):
		print "folder_name:",d,"<BR>"
		search_folders.append(d)
parent= os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))#getcwd()=cgi-bin so joining gets to "/usr/lib/"
parent= os.path.abspath(os.path.join(parent, os.path.pardir))#cd .. to /usr
root= os.path.abspath(os.path.join(parent, os.path.pardir))#cd .. to /

relPath="pipermail/mailman/"
folder_names=[]
for d in search_folders:
        peekDir=folder+"/"+d
	folder_name=root+relPath+d+"/"
	folder_names.append(folder_name)
#	print "folder_name_relpath:"+folder_name+"<BR>"
	for (p,d,files) in os.walk(peekDir):
		for file in files:
			if not file=="subject.html" and not file=="date.html" and not file=="thread.html" and not file=="author.html" and not file=="index.html":
				fname=peekDir+"/"+file
				htmlfiles.append(fname)
				filepath=folder_name+file
				htmlfiles_paths.append(filepath)

hRel="<a href=\""
tagClose="\">"
aEnd="</a><BR>"
search="gibberish"
i=0
j=0
for article_file in htmlfiles:
#	print "article_file abspath:",os.path.abspath(article_file),"\n<BR>"
	relFile=htmlfiles_paths[i]
	i=i+1
	fr = open(article_file,'r')
        frlines= fr.readlines()
        found=False
        for line in frlines:
#            print line
	    if(re.search(search,line)):                  
                found=True                  
	
	if found==True:
                print("["+hRel+relFile+tagClose+article_file+aEnd+"]<BR>")
