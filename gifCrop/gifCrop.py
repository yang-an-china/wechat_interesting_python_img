# coding=utf-8

from PIL import Image
import os


def crop_gif(gif, box):
    """
    Crop gif picture.
    Args:
        gif: gif file name
        box: crop box (left, up, right, down)
    """
    _, file = os.path.split(gif)
    name, ext = os.path.splitext(file)

    im = Image.open(gif)
    duration = im.info['duration']
    frames = []
    try:
        frames.append(im.crop(box))
        while True:
            im.seek(im.tell()+1)
            frames.append(im.crop(box))
    except:
        pass

    frames[0].save(name + '_crop' + ext,
                   save_all=True,
                   append_images=frames,
                   loop=0,
                   duration=duration)

if __name__ == "__main__":
    crop_gif('4.gif', (83, 0, 578, 495))
    crop_gif('6.gif', (82, 0, 577, 495))

    pass
