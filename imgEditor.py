import os
from sys import argv
from cv2 import imread, imwrite

from resize.py import resize
from blur.py import blur
from sharpen.py import sharpen

def menu(fileName, dirPath, i):
	cmd = input("Now, what to do whith {}? ".format(fileName)).lower()

	originalImg = imread(fileName)

	isValidCmd = False
	while (not isValidCmd):
		if cmd[0] == "r":
			newImg = resize(originalImg)
			isValidCmd = True
		elif cmd[0] == "b":
			newImg = blur(originalImg)
			isValidCmd = True
		elif cmd[0] == "f":
			newImg = sharpen(originalImg)
			isValidCmd = True
		else:
			cmd = input("Invalid command. Try again: ".format()).lower()

	if dirPath != "." and dirPath != "..":
		if not os.path.exists(dirPath): os.makedirs(dirPath)

	newFilePath = "{}/new_{}".format(dirPath, fileName)
	print("Saving {}...".format(newFilePath))
	imwrite(newFilePath, newImg)

def main():
	if len(argv) < 2:
		print("Try python3 imageEditor.py <fileName1> <fileName2> ...")
		exit()

	print("This editor has the following commands:")
	print(" •Image [r]esize")
	print(" •Apply [b]lur")
	print(" •Apply [f]ilter")

	print("First, enter the path to the directory where you want to save the news edits?")
	dirPath = input(">> ")
	for idx, fileName in enumerate(argv[1:]):
		menu(fileName, dirPath, idx)

if __name__ == "__main__": main()