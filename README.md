# Tracking Microbots with Trackpy
Senior Design project for CISC498/475 by Casey Rock, Jayson Morgado, Yifan Ni, Ian McCabe, Olu Osinubi, Gavin Morris, and Brennan Gallamoza

## Prerequsites Software
1. Anaconda 


## Whats our software comes with:
**`LiveAnnotator.py`**

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

## **Preparing to Run the Program**  

1. Open Anaconda Navigator
2. Launch CMD.exe Prompt
3. Change the Directroy to the microbots folder.
   1. For windows type `cd <add path to folder>`
   2. Example `cd C:\Users\casey\Documents\Work\Microbots`
4. Run `pip install -r req.txt` to download all the required packages
5. Close CMD.exe Prompt
6. Launch Juypter Notebook from Anaconda Navigator 
7. In Jupyter Notebook, Navigate to the microbots folder
8. Open one of the following notebooks: `LiveAnnotator.ipynb`, `trackpy.ipynb`, or `simple-trackpy.ipynb`

**Notes:**
   1. `pip` may need to be upgraded to correctly install `req.txt`. If installation fails, try upgrading pip by using `pip install --upgrade pip`
   2. If using a virtual environment, use `python -m pip install -r req.txt` instead for Step 4 to use your environment's `pip`. Likewise for Note 1
---

## **Using Live Annotation In Jupyter Notebook**

The `LiveAnnotator.ipynb` is used to capture a portion of your screen for live annotation of cells. The process works as follows:

### 1. Run the first code block and all cells in the `Trackpy Parameters` section to select parameters for `trackpy.locate()`
   - Running the parameter code blocks will start the program with default parameters. Sometimes adjusting the parameters will improve performance for different videos.
   - Details on what each parameter means can be read [here.](http://soft-matter.github.io/trackpy/dev/generated/trackpy.locate.html)

### 2. Run the `Screen Cropper` code blocks. Now, drag your mouse to select a portion of your screen for the program to record
   - Selecting an area is *required*
   - The selected area will be the area that `trackpy.locate()` will apply edge detection to.
   - If you have already selected an area and want to reselect, simply click on a new area and drag again.

### 3. Run the `Microbot Locator` code blocks. The program will continuously screenshot and annotate the selected area, displaying a stream of annotated images in a new window.
   - First, you will need to select whether or not you want the positions of potential microbots recorded
      - This only needs to be run once
   - The annotated images will be in a separate window from your Jupyter Notebook
   - Potential microbots will be circled in blue.

### 4. Exit the window by clicking into the window are pressing the `q` button.
   - This will end the `Microbot Locator` code block execution.

### 5. Run the `Export Located Positions to CSV` code block to save a timestamped CSV to the `output` folder.
   - This code will only save a CSV if "Record Located Microbot Positions?" is set to "Yes", otherwise an error will be printed.

### 6. Adjust parameters and re-crop screen as necessary. And repeat Step 4 run live annotation again.
   - You do not need to re-run the code blocks for Steps 1-2; shifting the sliders will adjust the already initialized parameters.
   - Repeating Step 2 to re-crop the screen is optional; you may simply adjust parameters and skip to Step 3 to use the same selection area.

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
