from PIL import Image
import os
from random import randint
from threading import Thread
import json


def get_photos(path_from: str):
    backgrounds = []
    for background in os.listdir(path_from):
        backgrounds.append(path_from + "\\" + background)
    return backgrounds


def process_worker(windy_path, background, save_to, name, size, offset, rotation):
    background = Image.open(background)
    windy = Image.open(windy_path)
    windy = windy.resize(
        (background.size[0]//size+offset, background.size[1]+offset))
    windy = windy.rotate(randint(-rotation, rotation))
    preview = Image.new('RGBA', size=background.size)
    preview.paste(background, (0, 0))
    try:
        preview.paste(windy, (0, 0), windy)
    except ValueError:
        preview.paste(windy, (0, 0))
    preview.save(f"{save_to}\\{name}.png")


def process_photos(windy_path, background_paths: list[str], save_to: str, size, offset, rotation):
    i = 0
    for background in background_paths:
        thread = Thread(target=process_worker, args=[
                        windy_path, background, save_to, i, size, offset, rotation])
        thread.start()
        i += 1


def main():

    with open('config.json', encoding="utf-8") as f:
        settings = json.load(f)
    settings = settings["settings"]
    photos = get_photos(settings["path_from"])
    process_photos(settings["windy_path"], photos,
                   settings["path_to"],
                   settings["size"],
                   settings['offset'],
                   settings['random_rotate'])

    print("Done! Press enter...")


if __name__ == "__main__":
    main()
