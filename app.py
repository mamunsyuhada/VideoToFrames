import os, os.path
import cv2

pathDir = os.getcwd() + "/frames"
print(pathDir)

def countDir(d):
    count = 0
    for path in os.listdir(d):
        if os.path.isfile(os.path.join(d, path)):
            count += 1
    return count

def makeDir():
    try:
        os.mkdir(pathDir)
    except OSError:
        print("Creation of the directory %s failed" % pathDir)
    else:
        print("Successfully created the directory %s " % pathDir)

makeDir()

vidcap = cv2.VideoCapture('video.MOV')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec * 1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(pathDir + "/image" + str(count) + ".jpg", image)     # save frame as JPG file
    return hasFrames

sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

print("Done !\t" + str(countDir(pathDir)) + " images")