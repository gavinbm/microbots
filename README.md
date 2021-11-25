# Tracking Microbots with Trackpy
Senior Design project for CISC498/475 by Casey Rock, Jayson Morgado, Yifan Ni, Ian McCabe, Olu Osinubi, and Gavin Morris

# Running the program  
track.py is the standard python script version
trackpy.ipynb is the jupyter notebook version and will have more verbose output

All dependencies are kept in the virtual environments in the env directory and they must
be running or you must have all the libraries from req.txt installed for the programs to work.

If on windows run this command from the microbots directory to activate the virtual envorionment
> env\win-env\Scripts\activate.bat
If on Mac OSX or Linux, run this command instead
> source env/unix-env/activate .

To deactivate the virtual environment on any machine run this commadn while it is active
> deactivate

Once the virtual environments are active, you can either run the jupyter notebook via the jupyter kernel or 
you can run the standard script like this
> python track.py VIDEOFILEPATH
where VIDEOFILEPATH is the path to your video file. If your video is in the same directory as track.py, you can just use the vieo file name, otherwise you'll need the path to the file.