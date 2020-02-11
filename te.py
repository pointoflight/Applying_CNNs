import os
from PIL import Image
n = 43

for i in range(n) : 
	print(i)

cur_path = os.getcwd()
path = os.path.join(cur_path, 'Train', '0')
print(path)

try : 
	image = Image.open(path + '/' + '00000_00000_00000.png')
except : 
	print("error loading image")