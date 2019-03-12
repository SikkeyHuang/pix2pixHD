import sys
import os
import cv2

def main():
    test_dataset=['color500/train_B/','color2k/train_B/']


    for inputpath in test_dataset:
        img_list = os.listdir(inputpath)
        img_list.sort()

        output_dir = inputpath.replace('B','A')
        print(output_dir)

        for img_fn in img_list:
            print(img_fn)
            output_fn = os.path.join(output_dir,img_fn )
            inputimage = cv2.imread(inputpath+img_fn)
            gray_image = cv2.cvtColor(inputimage, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(output_fn,gray_image)



if __name__ == '__main__':
    main()