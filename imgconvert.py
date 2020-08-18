import os
from PIL import Image

print('\n')
print('**************************************')
print('Image Format Converter - randomstudios')
print('**************************************')
print('\n')

listOfFormatsSupported = ['bmp', 'dib', 'eps', 'gif', 'icns', 'ico', 'im', 'jpeg', 'jpeg2000', 'msp', 'pcx', 'png', 'ppm', 'sgi', 'spider', 'tga', 'tiff', 'webp', 'xbm']

print('List of supported formats for conversion')
print('----------------------------------------')

for imgFormat in listOfFormatsSupported:
    print(imgFormat)
    
print('----------------------------------------')
print('\n')

path, ext = os.path.splitext(input('Enter Directory or File Path: ').strip())

toImg = input('Convert to e.g. bmp, tiff, jpeg etc: ').strip().lower()

if (toImg[0] == '.'):
    toImg = toImg[1:]

if (toImg == 'jpg'):
    toImg = 'jpeg'
elif (toImg == 'jpg 2000' or toImg == 'jpg2000' or toImg == 'jpeg 2000'):
    toImg = 'jpeg2000'
elif (toImg not in listOfFormatsSupported):
    print('Unsupported Output Image Format, Retry')
    exit()

if (ext != ''):
    print('Converting '+path+ext)
    im = Image.open(path+ext).convert("RGB")
    im.info.pop('background', None)
    im.save(path+"."+toImg, toImg, quality=100, subsampling=0)
    print("Done Converting\n")
    exit()

fromImg = input('Convert from e.g., png, jpg, webp etc: ').strip().lower()

if (fromImg[0] != '.'):
    fromImg = '.'+fromImg

if (fromImg[1:] == 'jpg'):
    fromImg = '.jpg'
elif (fromImg[1:] == 'jpeg'):
    fromImg = '.jpeg'
elif (fromImg[1:] == 'jpg 2000' or fromImg[1:] == 'jpg2000' or fromImg[1:] == 'jpeg 2000'):
    fromImg = '.jpeg2000'
elif (fromImg[1:] not in listOfFormatsSupported):
    print('Unsupported Input Image Format, Retry')
    exit()

if (path[-1] != '/'):
	path += '/'

files = os.listdir(path)

count = 0

print('\n')

for file in files:
    if (fromImg in file):
        print('Converting '+file)
        im = Image.open(path+file).convert("RGB")
        im.info.pop('background', None)
        im.save(os.path.splitext(path+file)[0]+"."+toImg, toImg, quality=100, subsampling=0)
        print("Done Converting\n")
        count += 1

if (count != 0):
    print(str(count) + ' files converted successfully\n')
else:
    print("No '"+fromImg[1:]+"' files found\n")

