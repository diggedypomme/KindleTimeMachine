# KindleTimeMachine

The KindleTimeMachine is a set of ai generated clockfaces with a script to run them on a Kindle. This is created to go alongside my Kindlefusion project here: https://github.com/diggedypomme/Kindlefusion but can also be run standalone. I have generated an image for every minute of the day, and the clock displays this sequentially. The images were made with stable diffusion 2.1 base model, with depth controlnet, and I will go into the settings below.These were made in early June but I haven't got round to updating this.

The clockfaces that I generated so far can be previewed here: https://diggedypomme.com/clockfaces/, with mixed success. I think my favourite one is the tentacle one. The html for the preview is in the preview folder.

The kindle works best with converted black and white images, so I will include a link to a zip for each clock face, and will try and share the colour ones too in case they are useful for someone


![Kindle Time Machine](info/kindle_time_machine%20(11).jpg)

## Running the clockfaces

In the "kindle" folder there are 4 files. 
- simple_eips.sh  . This tests that you can display an image
- mayclock.sh     . The actual clock script
- start_in_background . command for running this in the background
- killclock           . A script to kill a background process of the clock to stop it

You will need to update the path to match the clock name, so like 

in mayclock.sh: image_dir="/mnt/us/mayclock/anteaters"
in simple_eips.sh : anteaters/1224.jpg or anteaters/1224.jpg

## Stable diffusion





## Acknowledgements



## Contact



Happy clock-watching on your Kindle!
