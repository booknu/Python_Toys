import turtle as tt
import random
def onLeftClick(x, y):
    tSize = random.randrange(1, 10)
    r = random.random()
    g = random.random()
    b = random.random()
    tt.pencolor((r, g, b))
    tt.shapesize(tSize)
    tt.goto(x, y)
    tt.penup()
    tt.stamp()
    
tt.title('TITLE')
tt.shape('turtle')
tt.pensize(10)

tt.onscreenclick(onLeftClick, 1)

tt.done()