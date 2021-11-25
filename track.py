from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt

import cv2, glob
import sys

import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

import pims
import trackpy as tp

# change the following to %matplotlib notebook for interactive plotting
# matplotlib inline

# Optionally, tweak styles.
mpl.rc('figure',  figsize=(10, 10))
mpl.rc('image', cmap='gray')

##reads in sequence of images
##use pims.Video for videos but it is buggy
frames = pims.Video(sys.argv[1])

# construct file name of new video
arr = []
if '\\' in sys.argv[1]:
    arr = sys.argv[1].split('\\')

elif '/' in sys.argv[1]:
    arr = sys.argv[1].split('/')

if len(arr) != 0:
    new_video_name = "annotated-" + arr[len(arr) - 1]
else:
    new_video_name = "annotated-" + sys.argv[1]

##converts frames to grey scale
@pims.pipeline
def as_grey(frame):
    red = frame[:, :, 0]
    green = frame[:, :, 1]
    blue = frame[:, :, 2]
    return 0.2125 * red + 0.7154 * green + 0.0721 * blue

frames = as_grey(frames)

##101st frame
#plt.imshow(frames[200])

##takes in a frame, max size of the particle diameter-wise, invert = true bc features are darker than background
##returns a dataframe with potential particles
f = tp.locate(frames[0], 13, invert=True)

##.head shows first few rows of pandas dataframe
f.head()

plt.figure()  # make a new figure
##annotate searches for the particles and circles them
##this is just the first frame
tp.annotate(f, frames[0])

fig, ax = plt.subplots()
ax.hist(f['mass'], bins=20)
##plots the 'mass' of each detected particle
# Optionally, label the axes.
ax.set(xlabel='mass', ylabel='count')

f = tp.locate(frames[0], 13, invert=True, minmass=450)
##set min 'mass' to 450

##print image before manually dropping non-particles
tp.annotate(f, frames[0])

##batch does tp.locate on each frame
f = tp.batch(frames[:199], 13, minmass=450, invert=True, processes=1)

fig, ax = plt.subplots()
ax.hist(f['mass'], bins=20)
##plots the 'mass' of each detected particle
# Optionally, label the axes.
ax.set(xlabel='mass', ylabel='count')

##pass in f
## second parameter is maximum displacement
## third is the most frames a particle can disappear before it is forgotten from memory
t = tp.link_df(f, 10, memory=10)

##goes through and saves each annotated frame as a png
for i in range(199):
    tp.annotate(f.loc[f["frame"] == i], frames[i]).figure.savefig("tempframes/f" + str(i))

##gets the annotated frames and turns them into a video
img_array = []

for i in range(1, len(frames[:199])):
    #glob.glob('tempframes/*.png'):
    filename = "tempframes/f" + str(i) + ".png"
    frame = Image.open(filename)
    img = cv2.imread(filename)
    height,width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter(new_video_name, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(img_array)):
    out.write(img_array[i])

out.release()

t1 = tp.filter_stubs(t, 15)
# Compare the number of particles in the unfiltered and filtered data.
print('Before:', t['particle'].nunique())
print('After:', t1['particle'].nunique())

#t1 = t1[(t1.y < 50) & (t1.x <250)].index
plt.figure()
tp.mass_size(t1.groupby('particle').mean())

plt.figure()
tp.annotate(t1,frames[0])

t1 = t1[(t1.y < 50)].index

##filters out bad annotations
condition = lambda x: ((x['mass'].mean() > 825) & (x['size'].mean() < 8) &
                       (x['ecc'].mean() > 0.1))
t2 = tp.filter(t1, condition)  # a wrapper for pandas' filter that works around a bug in v 0.12

plt.figure()
tp.annotate(t2, frames[0])

##plots movements 
plt.figure()
tp.plot_traj(t2)