import os
import pdb


root = 'train_1000'
image_dir = 'image_1000'
txt_dir = 'txt_1000'

image_files = os.listdir(os.path.join(root, image_dir))
txt_files = os.listdir(os.path.join(root, txt_dir))

for image, txt in zip(image_files, txt_files):
    print('{0} vs {1}'.format(image[:-4], txt[:-4]))
    pdb.set_trace()
