from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndChar():
	return chr(random.randint(65,90))
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
im=Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('Coval-Regular.ttf', 36)
draw = ImageDraw.Draw(im)
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())
b=rndColor2()
for t in range(4):
	draw.text((60 * t + 10, 10),rndChar(), font=font, fill=b)
im.save("/home/alex/Pictures/yanzhengma.jpg","jpeg")
im2=im.filter(ImageFilter.BLUR)
im2.save("/home/alex/Pictures/yanzhengma_BLUR.jpg","jpeg")

