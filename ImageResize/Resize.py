import os
import glob
import cv2

# Enter image
imgs = glob.glob('C:\Users\pc\Desktop\GPWork\Calf4\Neck\part1/*.jpg')
def trans_square(imgs):
    for i, img_list in enumerate(imgs):
        img = cv2.imread(img_list)
        resize_img = cv2.resize(img, (224, 224))
        #h, w, c = resize_img.shape
        cv2.imwrite(f'C:\Users\pc\Desktop\GPWork\Calf4V\C4_N_D1_P1_H{i+1}.png', resize_img)
        #print("{},{},{}".format(h, w, c))
    return img
trans_square(imgs)
print("Done !!!!!!")