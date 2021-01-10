from PIL import Image


img = Image.open('s14161.jpg').convert('RGB')
box = [0, -50, 100, 100]
cropped_img = img.crop(box)
cropped_img.save('cropped.jpg')
