from PIL import Image
im=Image.open('/home/alex/Pictures/2.jpg')
w,h=im.size
im.thumbnail((w/2,h/2))
im.save('/home/alex/Pictures/2new.jpg','jpeg')

