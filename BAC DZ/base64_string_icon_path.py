import base64
import os

icons = []
icon_dir = 'image'
i = 0
for filename in os.listdir(icon_dir):
	i +=1
	file_path = os.path.join(icon_dir,filename)
	icons.append(base64.b64encode(open(file_path, "rb").read()).decode('utf-8'))
	print(i, file_path)