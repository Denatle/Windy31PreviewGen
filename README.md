# Windy31PreviewGen
That is a simple windy31 type preview generator

### Examples:
![example1](https://media.discordapp.net/attachments/745587754439802931/1080783702243684392/0.png?width=440&height=247)![example2](https://media.discordapp.net/attachments/745587754439802931/1080783787446771722/3.png?width=247&height=247)


### How to use:
 - Clone/Download repository
 - Set up the config
 - Add backgrounds to `backgrounds` folder
 - Open `windygen.exe` or `windygen.py`
 - Done!

### Config:
**!!! YOU NEED TO SET ALL THOSE VALUES FOR IT TO WORK !!!**

 - `path_from` -  AbsPath to "backgrounds" folder
 - `windy_path` - AbsPath to windy.png
 - `path_to` - AbsPath to output folder
 - `offset` - size offset, default 10. If you see clipping or windy is
   too small, then crank it up
 - `random_rotate` - random rotation in degrees, default 5
 - `size` - size adaptation divider. If windy is too thin, reduce 
#### Requirements (not necessary for binary):
 - `python 3.11`
 - `pillow`
