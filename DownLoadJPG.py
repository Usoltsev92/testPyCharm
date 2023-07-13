import random
import urllib.request
names = []
def download_img(url):
    name = random.randrange(1,100)
    name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, name)
    names.append(name)


download_img("https://w.forfun.com/fetch/71/71cf5a68d51acab5f06c69c96b81c8a4.jpeg")
print(names)