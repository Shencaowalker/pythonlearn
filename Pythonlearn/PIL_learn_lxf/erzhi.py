from PIL import Image
image=Image.open("/home/alex/Pictures/yanzhengma.jpg")
imgry=image.convert("L")
def get_bin_table(threshold=140):
	table=[]
	for i in range(256):
		if i <threshold:
			table.append(0)
		else:
			table.append(1)
	return table


table=get_bin_table()
out=imgry.point(table,'1')
print out

