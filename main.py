import json
from PIL import Image
from random import choice
from urllib import request

DATA_URL = 'http://pizzapaolo.ru/expimp/catalog.php'
BACKGROUND_URL = 'http://pizzapaolo.ru/i-base/bg-wood.jpg'


def crop_center(img, width, height):
    w_center, h_center = map(lambda dim: dim // 2, img.size)
    w_min, h_min = w_center - width // 2, h_center - height // 2
    return img.crop(box=(w_min, h_min, w_min + width, h_min + height))


def load_pizza():
    response = request.urlopen(DATA_URL)
    data = json.load(response)
    product = choice(data['shop'])
    img_link = product['picsmall']
    img = Image.open(request.urlopen(img_link))
    side_size = min(img.size)
    return crop_center(img, side_size, side_size)


img = load_pizza()
background = Image.open(request.urlopen(BACKGROUND_URL))
background = crop_center(background, *img.size).convert('RGBA')
res = Image.alpha_composite(background, img)
