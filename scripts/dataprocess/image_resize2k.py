from PIL import Image
import os
from os.path import join

#target_width = 510
#target_height = 288
target_width = 2048
target_height = 1152

count = 0
croped = 0
log = open('hrlog.txt','w')
log2 = open('hrfilter.txt','w')
for root, dirs, files in os.walk('/scratch/shuang9/pix2pixHD/datasets/color2k'):
	for name in files:
		count = count+1
		img = Image.open(join(root, name))
		ow, oh = img.size
		
		if ow>=target_width and oh>=target_height:
			result = img.crop((0, 0,  target_width, target_height))
			result.save(join(root, name))	
			log.write(name+' ('+str(ow)+','+str(oh)+') ->'+str(result.size)+'\n')
			croped = croped+1
			
		elif ow>=2040 and oh>=target_height:
			new_image=img.resize((target_width, oh), Image.BICUBIC)
			result = new_image.crop((0, 0,  target_width, target_height))
			result.save(join(root, name))	
			log.write(name+' ('+str(ow)+','+str(oh)+') ->'+str(result.size)+'\n')
			croped = croped+1
			
		else:
			log2.write(join(root, name)+'\n')
		
		print (croped,'/',count)

log2.close()

rm_images= open('hrfilter.txt','r')

while True:
	img = rm_images.readline().strip()
	if not img:
		break
	os.remove(img)

checkcount = 0
for root, dirs, files in os.walk('/scratch/shuang9/pix2pixHD/datasets/color2k'):
	for name in files:
		img = Image.open(join(root, name))
		ow, oh = img.size
		if ow!=target_width or oh!=target_height:
			checkcount = checkcount+1
print checkcount

