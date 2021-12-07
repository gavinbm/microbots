# Tracking Microbots with Trackpy
Senior Design project for CISC498/475 by Casey Rock, Jayson Morgado, Yifan Ni, Ian McCabe, Olu Osinubi, and Gavin Morris

## Prerequsites Software
1. Anaconda 


## Whats our software comes with
`track.py`:is the standard python script version <br/>
`trackpy.ipynb`: is the jupyter notebook version that takes in a video, annotates each frame, then create a new 
video using the annotated frames. This version will have more verbose output and plots <br/>
`simple-trackpy.ipynb`: is the jupyter notebook version that simple takes in a video, annotates each frame, then create a new 
video using the annotated frames. <br/>
`req.txt`: a list of all the python Libraries that need to be downloaded.
`/videos`: a folder that stores all the input video. If you want to annotated a video add it to this files
`/tempframes`: a folder the store temporary frames (Our code uses this folder, you do not have to do anything with it)


## Running the program  

1. Open Anaconda Navigator
2. Launch CMD.exe Prompt
3. Change the Directroy to the microbots folder.
   1. For windows type `cd <add path to folder>`
   2. Example `cd C:\Users\casey\Documents\Work\Microbots`
4. Run `pip install -r req.txt` to download all the required packages
5. Close CMD.exe Prompt
6. Launch Juypter Notebook from Anaconda Navigator 
7. In Jupyter Notebook, Navigate to the microbots folder
8. Click on the files named `trackpy.ipynd` or `simple-trackpy.ipynd` to open the notebook


## Setting up the Videos In Jupyter Notebook

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