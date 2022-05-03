# Tracking Microbots with Trackpy
Senior Design project for CISC498/475 by Casey Rock, Jayson Morgado, Yifan Ni, Ian McCabe, Olu Osinubi, Gavin Morris, and Brennan Gallamoza

## Prerequsites Software
1. Anaconda 


## Whats our software comes with:
**`cropper.py`**

&emsp;Jupyter notebook for realtime microbot detection. Annotates 

`trackpy.ipynb`

&emsp;is the Jupyter notebook that takes in a video, annotates each frame, then create a new 
video using the annotated frames. This version will have more verbose output and plots

`track.py`

&emsp;Standard python script version of trackpy.ipynb

`simple-trackpy.ipynb`

&emsp; Jupyter notebook version that simple takes in a video, annotates each frame, then create a new 
video using the annotated frames

`req.txt`

&emsp;a list of all the python Libraries that need to be downloaded.

`/videos`

&emsp;a folder that stores all the input video. If you want to annotated a video add it to this files

`/tempframes`

&emsp;a folder the store temporary frames (Our code uses this folder, you do not have to do anything with it)

---

## **Preparing to Run the program**  

1. Open Anaconda Navigator
2. Launch CMD.exe Prompt
3. Change the Directroy to the microbots folder.
   1. For windows type `cd <add path to folder>`
   2. Example `cd C:\Users\casey\Documents\Work\Microbots`
4. Run `pip install -r req.txt` to download all the required packages
5. Close CMD.exe Prompt
6. Launch Juypter Notebook from Anaconda Navigator 
7. In Jupyter Notebook, Navigate to the microbots folder
8. Open one of the following notebooks: `cropper.ipynb`, `trackpy.ipynb`, or `simple-trackpy.ipynb`

---

## **Using Live Annotation In Jupyter Notebook**

The `cropper.ipynb` is used to capture a portion of your screen for live annotation of cells. The process works as follows:

### 1. Run the first code block and all cells in the `Trackpy Parameters` section to select parameters for `trackpy.locate()`
   - Running the parameter code blocks will start the program with default parameters. Sometimes adjusting the parameters will improve performance for different videos.
   - Details on what each parameter means can be read [here.](http://soft-matter.github.io/trackpy/dev/generated/trackpy.locate.html)

### 2. Run the `Screen Cropper` code block. Now, drag your mouse to select a portion of your screen for the program to record
   -  The selected area will be the area that `trackpy.locate()` will crop
   - If you have already selected an area and want to reselect, simply click on a new area and drag again.
   - Selecting an area is *required*

### 3. Run the `Microbot Locator` code block. The program will continuously screenshot and annotate the selected area, displaying a stream of annotated images in a new window.
   - The window will be separate from your Jupyter Notebook
   - Potential microbots will be circled in blue.

### 4. Exit the window by clicking into the window are pressing the `q` button.

### 5. Run steps 1-2 again to adjust parameters and re-crop the screen selection. Then, follow step 3 to run live annotation again.

---

## **Setting up the Video Annotation In Jupyter Notebook**

In the both juypter NoteBook On the first line you want to let the program know the name of the video file you are using. NOTE the video must be in the `/videos` folder 

```python
################## EDIT THIS TO START ################## 
microbot_input_video_name = "Enter Input Video Name Here"
output_Video_name = "Enter Output Video Name Here"
diameter_of_cells = "enter an odd intereger for the diameters of the cells"
proccess_all_frame = True or False # IF True it will prcess all the frames in the video, If False it will process the first 200 frames
########################################################
```

> Once the video are names, run the jupyter notebook and get your annotated video 


## Required Hardware Requirment 
1. Nvidia 1060 Graphics Card
2. 8 GB of RAM
3. Intel I5 processor 
4. Operrating System: Windows or Linux

## Recomended Hardware Requirment 
1. Nvidia 2060 Graphics Card
2. 16 GB of RAM
3. Intel I7 processor 
4. Operrating System: Windows or Linux
