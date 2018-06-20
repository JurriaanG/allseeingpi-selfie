from gpiozero import Button
from picamera import PiCamera
from time import gmtime, strftime
from overlay_functions import *
from guizero import App, PushButton, Text, Picture
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

from time import sleep

# import terminal options
import subprocess
import os

#Overlay knop
def next_overlay():
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)
    

#Maak de foto en koppel aan overlay
def take_picture():
    global output
    output = strftime("/home/pi/allseeingpi/exportImg/image-%d-%m %H:%M.png", gmtime())
    camera.capture(output)
    camera.stop_preview()
    remove_overlays(camera)
    output_overlay(output, overlay)

    # Kleine gif opslaan
    size = 400, 400
    gif_img = Image.open(output)
    gif_img.thumbnail(size, Image.ANTIALIAS)
    gif_img.save(latest_photo, 'gif')

    # GUI foto pakt die gif
    your_pic.set(latest_photo)
    cmd = os.popen('scp latest.gif pi@192.168.0.111:/home/pi/mirror/')
    #cmd = os.popen('scp latest.gif pi@192.168.0.222:/home/pi/mirror/')    


def new_picture():
    camera.start_preview()
    preview_overlay(camera, overlay)

def send_tweet():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )

    
# Send the tweet
    message = "Nice selfie! Check more details on our website!"
    with open(output, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)

#Knoppen en GPIO
next_overlay_btn = Button(23)
next_overlay_btn.when_pressed = next_overlay
take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture


#Camera en resolutie fotos
camera = PiCamera()
camera.resolution = (800, 480)
camera.hflip = True

#Foto preview
camera.start_preview(alpha=128)

#Bestandsnaam
output = ""

latest_photo = '/home/pi/allseeingpi/latest.gif'

app = App("The All-Seeing Pi", 600, 400)
#app.attributes("-fullscreen", True)


#GUI tekst en knoppen
message = Text(app, "don't give up yet!")
your_pic = Picture(app, latest_photo)
new_pic = PushButton(app, new_picture, text="Take a new picture")
tweet_pic = PushButton(app, send_tweet, text="Tweet picture")
app.display()



