# allseeingpi-selfie

The All Seeing Pi script is based on this tutorial: https://projects.raspberrypi.org/en/projects/the-all-seeing-pi
What I've changed in the code is mainly it's automated function to send the latest picture (latest.gif) to another pi (pi zero) over SCP. 


# The files

Allseeingpi.py

The main file doing all the work is allseeingpi.py. This one controls the GPIO of the Raspberri Pi, controls the camera, takes the picture (saves them twice, one for the GUI to display and one to save in the exportImg folder) and then, the most important bit for the project, sends it to the other pi's over SCP. This happens at line 44. 


Auth.py (please be carefull, sensitive information)

These are the AUTH keys to tweet the latest image to Twitter.


Change_overlays_and_take_picture.py

Speaks for itself, this script changes the different overlays/filters you can put on top of the images. I will change these filters later on, but for now they'll do. 


Latest.gif

This files gets overwritten as soon as a new picture is taken with the allseeingpi.py script. The GUI grabs this image to display the latest image taken. 


Overlay_function.py 

Changes the different overlays possible.


# The goal

http://mirrorontheether.com/wp-content/uploads/2018/06/instalaltie.jpg

Here is an render of how the installation will look. In front: the monitor connected to the Raspberry Pi 3B (with camera and code seen here), in the back two displays showing the image you just took but with an overlay making it seem like the images are for sale on some stock foto website. 


# The problem

Right now I am aware that I can't have the Pi zero's run a script using the 'latest.gif' without that blocking the Pi 3B to send any newly taken images. Right now it uses SCP to send those files, but maybe I need a different way to send those images so that it won't cause a problem to send in new ones? 
Because the goal is that if you take a picture on the pi 3B, that image also appears on the pi zero's in the back. 
