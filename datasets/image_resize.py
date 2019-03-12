from PIL import Image
import os
from os.path import join

target_width = 2040
target_height = 1080
count = 0
croped = 0
log = open('log.txt','w')
log2 = open('filter.txt','w')
for root, dirs, files in os.walk('/media/siqi/DATA/test/DIV2K_train_HR/'):
	for name in files:
		print (croped,'/',count)
		count = count+1
		img = Image.open(join(root, name))
		ow, oh = img.size
		if ow>=target_width and oh>=target_height:
			result = new_image.crop((0, 0,  target_width, target_height))
			result.save(join(root, name))	
			log.write(name+' ('+str(ow)+','+str(oh)+') ->'+str(result.size)+'\n')
			croped = croped+1
		else:
			log2.write(join(root, name)+'\n')

