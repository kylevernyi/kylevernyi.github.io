#run this in any directory add -v for verbose 
#get Pillow (fork of PIL) from pip before running --> pip install Pillow

import os
import sys
from PIL import Image

def compressMe(file, verbose=False):
	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	picture.save("compressed/"+file,"JPEG",optimize=True,quality=70) 
	
	newsize = os.stat(os.path.join(os.getcwd(),"compressed/"+file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	# if (verbose):
		# print "File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent)
	return percent

def main():
	#finds present working dir
	pwd = os.getcwd()

	tot = 0
	num = 0
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			num += 1
			tot += compressMe(file)
	# print "Average Compression: %d" % (float(tot)/num)
	print("Done")

if __name__ == "__main__":
	main()