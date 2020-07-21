import os
import random
import game_config as gc 
from pygame import image, transform



anicount = dict((a,0) for a in gc.assetfiles)

def avaiani():
    return [a for a,c in anicount.items() if c<2]

class Animal:
    def __init__(self, index):
        self.index = index
        self.row = index//gc.numtiles
        self.col = index%gc.numtiles
        self.name = random.choice(avaiani())
        anicount[self.name] += 1

        self.imgpath = os.path.join(gc.assetdir,self.name)
        self.image = image.load(self.imgpath)
        self.image = transform.scale(self.image, (gc.imgsize - 2*gc.margin, gc.imgsize-2*gc.margin))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip = False
