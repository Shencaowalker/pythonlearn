from PIL import Image,ImageFilter
im=Image.open("/home/alex/Pictures/295.JPG")
im2 = im.filter(ImageFilter.BLUR)
im2.save('/home/alex/Pictures/295BLUR.JPG', 'jpeg')

