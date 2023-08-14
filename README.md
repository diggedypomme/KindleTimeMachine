# KindleTimeMachine

The KindleTimeMachine is a set of ai generated clockfaces with a script to run them on a Kindle. This is created to go alongside my Kindlefusion project here: https://github.com/diggedypomme/Kindlefusion but can also be run standalone. I have generated an image for every minute of the day, and the clock displays this sequentially. The images were made with stable diffusion  with depth controlnet, and I will go into the settings below.These were made in May 2023, but I am just getting round to documenting. I haven't yet used it with the XL model but will give that a play.

The clockfaces that I generated so far can be previewed here: https://diggedypomme.com/clockfaces/, with mixed success. I think my favourite one is the tentacle one. The html for the preview is in the preview folder.

The kindle works best with converted black and white images, so I will include a link to a zip for each clock face, and will try and share the colour ones too in case they are useful for someone


![Kindle Time Machine](info/kindle_time_machine%20(11).jpg)

## Running the clockfaces

In the "kindle" folder there are 4 files. 
- simple_eips.sh  . This tests that you can display an image
- mayclock.sh     . The actual clock script
- start_in_background . command for running this in the background
- killclock           . A script to kill a background process of the clock to stop it

You will need to update the path to match the clock name, so:

in mayclock.sh:
image_dir="/mnt/us/mayclock/anteaters"


in simple_eips.sh :
anteaters/1224.jpg or anteaters/1224.jpg

## preparing the base images
in the source_clock_image folder there are 4 files (everyminute1-4.py). Each of these will generated a different text font and layout, and you can mess with them yourself to have it how you want

## Stable diffusion
The images were generated based on the above clock images by using controlnet depth on the images. It was an experiment so some clockfaces turned out better than others. Reading from the metadata, the settings I used were:

Creepy picture. kraken tentacles
Steps: 30, Sampler: Euler a, CFG scale: 9, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: Balanced, preprocessor params: (512, 64, 64)"

bees
Negative prompt: blurry
Steps: 50, Sampler: Euler a, CFG scale: 7.5, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 64, 64)"


human bones. creepy
Negative prompt: blurry

Steps: 40, Sampler: DPM++ 2M Karras, CFG scale: 9, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 64, 64)"


steampunk clockwork. clock. greyscale. intricate
Negative prompt: blurry

Steps: 50, Sampler: Euler a, CFG scale: 7, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 0: "preprocessor: depth_midas, model: control_depth-fp16 [400750f6], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 0.5, 64)"


dragons
Negative prompt: blurry

Steps: 32, Sampler: Euler a, CFG scale: 7, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 0: "preprocessor: depth_midas, model: control_depth-fp16 [400750f6], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 64, 64)"



fancy clock
Negative prompt: blurry

Steps: 45, Sampler: Euler a, CFG scale: 7.5, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: Balanced, preprocessor params: (512, 64, 64)"


flowers
Negative prompt: blurry

Steps: 50, Sampler: Euler a, CFG scale: 7.5, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 64, 64)"

food photography

Steps: 40, Sampler: Euler a, CFG scale: 7, Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 0: "preprocessor: depth_midas, model: control_depth-fp16 [400750f6], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: Balanced, preprocessor params: (512, 64, 64)"

shrooms
Negative prompt: blurry

Steps: 32, Sampler: Euler a, CFG scale: 7,  Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 0: "preprocessor: depth_midas, model: control_depth-fp16 [400750f6], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 0.1, 0.1)"

Parrots
Negative prompt: blurry

Steps: 45, Sampler: Euler a, CFG scale: 7.5,  Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: True, control mode: Balanced, preprocessor params: (512, 64, 64)"

snakes. creepy
Negative prompt: blurry

Steps: 30, Sampler: Euler a, CFG scale: 9,  Size: 600x800, Model hash: 6ce0161689, Model: v1.5pruned_v1-5-pruned-emaonly, Version: v1.2.1, ControlNet 1: "preprocessor: scribble_pidinet, model: control_scribble-fp16 [c508311e], weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: Balanced, preprocessor params: (512, 64, 64)"


