import os
import pdb


root = 'train_1000'
image_dir = 'image_1000'
txt_dir = 'txt_1000'

image_files = os.listdir(os.path.join(root, image_dir))
txt_files = os.listdir(os.path.join(root, txt_dir))
count = 1

for image, txt in zip(image_files, txt_files):
    if image[:-4] == txt[:-4]:
        print('{0} vs {1}'.format(image[:-4], txt[:-4]))
        os.renames(os.path.join(root, image_dir, image), os.path.join(root, image_dir, str(count) + '.jpg'))
        os.renames(os.path.join(root, txt_dir, txt), os.path.join(root, txt_dir, str(count) + '.txt'))
        count += 1
    else:
        raise UserWarning('image is not corresponding to txt')
