import pyglet
import random
import math
from pyglet.window import key
from pyglet.window import mouse


main_batch=pyglet.graphics.Batch()

game_window=pyglet.window.Window(1200,700)
sprite_1=pyglet.image.load('/Users/asurada/Desktop/15.png')
sprite_2=pyglet.image.load('/Users/asurada/Desktop/15.png')
engine_image=pyglet.image.load('/Users/asurada/Desktop/engine_flame.png')
bullet_image=pyglet.image.load('/Users/asurada/Desktop/bullet.png')

hero=pyglet.sprite.Sprite(img=sprite_1,x=400,y=0,batch=main_batch)
hero.scale=0.1


engine_sprite=pyglet.sprite.Sprite(img=engine_image,batch=main_batch)
engine_sprite.visible=False

#bullet_sprite=pyglet.sprite.Sprite(img=bullet_image,x=hero.x+2,y=hero.y,batch=main_batch)

key_option=key.KeyStateHandler()
game_window.push_handlers(key_option)

diamond=[]
bullet=[]
for i in range(15):
    rand_x=random.randrange(0,1200,1)
    new_sprite=pyglet.sprite.Sprite(img=sprite_2,x=rand_x,y=700,batch=main_batch)
    new_sprite.scale=0.1
    diamond.append(new_sprite)
@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

def check_if_out(self):
    if self.y<-100:
        rand_x=random.randrange(-200,200,1)
        self.x+=rand_x
        if self.x>1200:
            self.x=1200
        elif self.x<0:
            self.x=0
        self.y=700


def update(dt):
    
    if key_option[key.LEFT]:
        hero.x-=7
        #bullet_sprite.x=hero.x+2
        engine_sprite.visible=False
    elif key_option[key.RIGHT]:
        hero.x+=7
       # bullet_sprite.x=hero.x+2
        engine_sprite.visible=False
    elif key_option[key.UP]:
        hero.y+=7
       # bullet_sprite.y=hero.y
        engine_sprite.x=hero.x
        engine_sprite.y=hero.y-20
        engine_sprite.visible=True
    elif key_option[key.DOWN]:
        hero.y-=7
       # bullet_sprite.y=hero.y
        engine_sprite.visible=False
    elif key_option[key.SPACE]:
        new_bullet=pyglet.sprite.Sprite(img=bullet_image,x=hero.x+5,y=hero.y,batch=main_batch)
        new_bullet.scale=0.5
        bullet.append(new_bullet)
    if hero.x>1000:
        hero.x=1000
        #bullet_sprite.x=hero.x+2
        engine_sprite.visible=False
    elif hero.x<10:
        hero.x=10
       # bullet_sprite.x=hero.x+2
        engine_sprite.visible=False
    if hero.y>600:
        hero.y=600
       # bullet_sprite.y=hero.y
        engine_sprite.visible=False
    elif hero.y<0:
        hero.y=0
       # bullet_sprite.y=hero.y
        engine_sprite.visible=False
    for live in diamond:
        rand_y=1*random.randrange(0,15,2)
        live.y-=rand_y
        #distance=math.sqrt((live.x-hero.x)**2+(live.y-hero.y)**2)
        #if distance<20:
           # game_window.clear()
           # label_gg=pyglet.text.Label(text='GG',x=600,y=350,batch=main_batch)
        check_if_out(live)
    if len(bullet)!=0:
        for bul in bullet:
            bul.y+=5
            if bul.y>600:
                bul.visible=False
            
        
   
       
        


def delete():
    engine_sprite.delete()
    hero.delete()
    
pyglet.clock.schedule_interval(update, 1/100.0)
pyglet.app.run()
    


8
