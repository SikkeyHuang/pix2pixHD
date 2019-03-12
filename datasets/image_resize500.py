from PIL import Image
import os
from os.path import join

target_width = 510
target_height = 288
'''
count = 0
croped = 0
log = open('log.txt','w')
log2 = open('filter.txt','w')
for root, dirs, files in os.walk('/scratch/shuang9/pix2pixHD/datasets/color500'):
	for name in files:
		print (croped,'/',count)
		count = count+1
		img = Image.open(join(root, name))
		ow, oh = img.size
		if ow>=target_width and oh>=target_height:
			result = img.crop((0, 0,  target_width, target_height))
			result.save(join(root, name))	
			log.write(name+' ('+str(ow)+','+str(oh)+') ->'+str(result.size)+'\n')
			croped = croped+1
		else:
			log2.write(join(root, name)+'\n')

log2.close()
'''
rm_images= open('filter.txt','r')

while True:
	img = rm_images.readline().strip()
	if not img:
		break
	os.remove(img)

checkcount = 0
for root, dirs, files in os.walk('/scratch/shuang9/pix2pixHD/datasets/color500'):
	for name in files:
		img = Image.open(join(root, name))
		ow, oh = img.size
		if ow!=target_width or oh!=target_height:
			checkcount = checkcount+1
print checkcount

