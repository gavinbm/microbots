# Tracking Microbots with Trackpy
Senior Design project for CISC498/475 by Casey Rock, Jayson Morgado, Yifan Ni, Ian McCabe, Olu Osinubi, and Gavin Morris

## STEP 1: Running the program  
`track.py`:is the standard python script version <br/>
`trackpy.ipynb` is the jupyter notebook version and will have more verbose output <br/>
<br/>
> All dependencies are kept in the virtual environments in the env directory and they must <br/>
> be running or you must have all the libraries from req.txt installed for the programs to work.
<br/>
<br/>

### Running the virtual environments on your operatinve system 

If on **windows** run this command from the microbots directory to activate the virtual envorionment

```powershell
env\win-env\Scripts\activate.bat
```
If on **Mac OSX or Linux**, run this command instead

```bash
source env/unix-env/bin/activate .
```

To deactivate the virtual environment on any machine run this commadn while it is active
```
deactivate
```

Once the virtual environments are active, you can either run the jupyter notebook via the jupyter kernel or you can run the standard script like this

```bash
python track.py VIDEOFILEPATH
```
where `VIDEOFILEPATH` is the path to your video file. If your video is in the same directory as track.py, you can just use the vieo file name, otherwise you'll need the path to the file.

## Running Jupyter Notebook
If you want to run the program in jupyter notebook you will need to run the following command 
```
jupyter notebook
```



## STEP 2:  Setting up the Videos In Jupyter Notebook

In the juypter Notenote Book On the first line you want to let the program know the name of the video file you are using. NOTE the video must be in 
the `/videos` folder 
```python
################## EDIT THIS TO START ################## 
microbot_input_video_name = "Enter Input Video Name Here"
output_Video_name = "Enter Output Video Name Here"
########################################################
```

> Once the video are names, run the jupyter notebook and get your annotated video 