import sys
import os
from PIL import Image

#get directory name by using sys

oringin_path=sys.argv[1]
dirpath=sys.argv[2]

#check the directory exists, 
#if yes change jpg to png then save in new folder
#if not create the folder then handle as below
if not os.path.isdir(dirpath):
	os.mkdir(dirpath)
	print("Directory ",dirpath," Created ") 
	
dirs=os.listdir(oringin_path)
images = [f for f in dirs if os.path.splitext(f)[-1] == '.jpg']
for image in images:
	image_name=image.split('.')
	im=Image.open(f'{oringin_path}/{image}')
	im.save(f'{dirpath}/{image_name[0]}.png')

