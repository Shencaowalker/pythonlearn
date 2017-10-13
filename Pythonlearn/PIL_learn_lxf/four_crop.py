from PIL import Image
im=Image.open("/home/alex/Pictures/2.jpg")
box=(10,10,20,20)
region=im.crop(box)
region.save("2_crop.jpg")

