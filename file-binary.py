#!/usr/bin/python3

def main():
	buffersize = 10000
	infile = open('me.jpg' ,'rb')
	outfile = open('new.jpg' ,'wb')
	buffer  = infile.read(buffersize)
	while len(buffer):
		outfile.write(buffer)
		print('.', end = '')
		buffer = infile.read(buffersize)
	print()
	print("Done.")
if __name__ == "__main__": main()