# Windy31PreviewGen
That is a simple windy31 type preview generator

### How to use:

 - Clone/Download repository
 - Set up the config
 - Add backgrounds to `backgrounds` folder
 - Open `windygen.exe` or `windygen.py`
 - Done!

### Config:
**!!! YOU NEED TO SET ALL THOSE VALUES FOR IT TO WORK !!!**

 - `path_from` -  AbsPath to backgrounds folder
 - `windy_path` - AbsPath to windy.png
 - `path_to` - AbsPath to "result" folder
 - `offset` - size offset, default 10. If you see clipping or windy is
   too small, then crank it up
 - `random_rotate` - random rotation in degrees, default 5
 - `size` - size adaptation divider. If windy is too thin, reduce 
#### Requirements (not necessary for binary):
 - `python 3.11`
 - `pillow`
