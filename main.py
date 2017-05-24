import json
from PIL import Image
from random import choice
from urllib import request

DATA_URL = 'http://pizzapaolo.ru/expimp/catalog.php'
BACKGROUND_URL = 'http://pizzapaolo.ru/i-base/bg-wood.jpg'


def crop_center(pic, width, height):
    """Crops the picture in the center with given size"""
    w_center, h_center = map(lambda dim: dim // 2, pic.size)
    w_min, h_min = w_center - width // 2, h_center - height // 2
    return pic.crop(box=(w_min, h_min, w_min + width, h_min + height))


def load_pizza():
    """Loads picture of a product and makes it square"""
    data = json.load(request.urlopen(DATA_URL))
    product = choice(data['shop'])
    img_link = product['picsmall']
    img = Image.open(request.urlopen(img_link))
    side_size = min(img.size)
    return crop_center(img, side_size, side_size)  # making the image square


img = load_pizza()
background = Image.open(request.urlopen(BACKGROUND_URL))
background = crop_center(background, *img.size).convert('RGBA')

# the result
res = Image.alpha_composite(background, img)
