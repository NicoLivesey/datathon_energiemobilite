import cv2
import numpy as np
import sys
import subprocess
import shlex
import os

gstCommand = None

def initialize(host, port, bitrate=1024):
    global gstCommand
    if os.name == "posix":
        args = shlex.split(('gst-launch-1.0 fdsrc ! videoparse format="i420" width=640 height=480' +
        ' ! x264enc speed-preset=1 tune=zerolatency bitrate={}' +
        ' ! rtph264pay config-interval=1 pt=96 ! udpsink host={} port={}').format(
        bitrate, host, port))
        gstCommand = subprocess.Popen(args, stdin=subprocess.PIPE)

def imshow(name, img):
    if gstCommand:
        gstCommand.stdin.write(cv2.cvtColor(img, cv2.COLOR_RGB2YUV_I420))
    else:
        cv2.imshow(img)

def waitKey(delay):
    if os.name == "posix":
        return -1
    return cv2.waitKey(delay)