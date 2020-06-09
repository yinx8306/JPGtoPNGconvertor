import sys
import os
from PIL import Image

#get directory name by using sys
dirpath=sys.argv[2]
oringin_path=sys.argv[1]

#check the directory exists, 
#if yes change jpg to png then save in new folder
#if not create the folder then handle as below
if os.path.isdir(dirpath):
	dirs=os.listdir(oringin_path)
	images = [f for f in dirs if os.path.splitext(f)[-1] == '.jpg']
	for image in images:
		image_name=image.split('.')
		im=Image.open(f'{oringin_path}/{image}')
		im.save(f'{dirpath}/{image_name[0]}.png')

else:
	dirName = 'new'
	os.mkdir(dirName)
	print("Directory ",dirName," Created ") 
	dirs=os.listdir(oringin_path)
	images = [f for f in dirs if os.path.splitext(f)[-1] == '.jpg']
	for image in images:
		image_name=image.split('.')
		im=Image.open(f'{oringin_path}/{image}')
		im.save(f'{dirpath}/{image_name[0]}.png')