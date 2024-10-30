from PIL import Image
import os
import sys

# Converts all files with initalExt to files with the finalext.
def convert_images(InputPath, InitialExtention, FinalExtention):
	# Prefixes extensions with dots, of not already.
	if FinalExtention[0] != '.':
		FinalExtention = "." + FinalExtention
	if InitialExtention[0] != '.':
		InitialExtention = "." + InitialExtention

	if not os.path.exists(InputPath):
		print('The given path does not exist.')
		return

	files = os.listdir(InputPath)

	if len(files) < 1:
		print("No suitable images found.")
		return

	os.makedirs(outputPath, exist_ok=True)
	outputPath = os.path.join(InputPath, "Ouput")

	for file in files:
		if InitialExtention in file:
			withoutExtension = file.partition('.')[0] 
			im = Image.open(os.path.join(InputPath, file))
			im.save(os.path.join(outputPath, f"{withoutExtension}{FinalExtention}"), FinalExtention[1:].upper())
	
	print("Complete!\n")


if __name__ == "__main__":
	if len(sys.argv) == 3:
		folderPath = os.getcwd()
		convert_images(folderPath, sys.argv[1], sys.argv[2])
	else:
		print(sys.argv)
		print("Expected two arguments (InitalExtension, FinalExtension)")