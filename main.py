from PIL import Image
import glob
import os
from pylibdmtx.pylibdmtx import decode

sDirectory = 'matrix/'
aDirs = next(os.walk(sDirectory))[1]

for sDIr in aDirs:
    aFiles = glob.glob(sDirectory + '/' + sDIr + '/' + "*.png")
    print(sDIr)
    for sFile in aFiles:
        image = Image.open(sFile)
        box = (160, 310, 320, 460)
        cropped_image = image.crop(box)
        sDM = decode(cropped_image)
        print(sDM[0].data)
        f = open('results/' + sDIr + '.txt', "a")
        f.write(sDM[0].data.decode("utf-8") + '\n')
        f.close()