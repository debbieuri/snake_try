import pyautogui as pp
pp.PAUSE = 0.01
size=[10,10]
ss=0
s=[]
z=pp.screenshot()
for y in range(z.height):
    if ss==0:
        for x in range(z.width):
            if z.getpixel((x,y))==(255,0,0):#...
                while z.getpixel((x+ss,y))==(255,0,0):
                    ss+=1
                ss-=1
                if ss>10:#don't shrink it too much...
                    for i in range(ss-1):#keep it square..
                        if not z.getpixel((x+ss,y))==(255,0,0):
                            ss=0
                            break
                    else:
                        ss+=3
                        s=[x+ss/2,y+ss/2]
                        print(x,y,ss)
                        while True:
                            if s[0]-ss<0:
                                break
                            a=z.getpixel((s[0]-ss,s[1]))
                            if a!=(255,0,0) and a!=(0,0,0) and a!=(0,255,0):
                                break
                            s[0]-=ss
                        while True:
                            if s[1]-ss<0:
                                break
                            a=z.getpixel((s[0],s[1]-ss))
                            if a!=(255,0,0) and a!=(0,0,0) and a!=(0,255,0):
                                break
                            s[1]-=ss
                        break
if s==[]:
    print('nnnnnnnnnnnnnn')
    brkeajfnc
pp.moveTo(s[0],s[1])
pp.click()
#ways=[[0,-1],[1,0],[0,1],[-1,0]]
b=[[0 for _ in range(size[1])]for _ in range(size[0])]
for x in range(size[0]):
    for y in range(size[1]):
        a=z.getpixel((s[0]+x*ss,s[1]+y*ss))
        if a==(0,255,0):
            b[x][y]=1
        if a==(255,0,0):
            b[x][y]=2
pp.press('down')
while True:
    z=pp.screenshot(region=(s[0],s[1],s[0]+ss*size[0],s[1]+ss*size[1]))
    g=[[0 for _ in range(size[1])] for _ in range(size[0])]
    for x in range(size[0]):
        for y in range(size[1]):
            a=z.getpixel((x*ss,y*ss))
            if a==(0,255,0):
                g[x][y]=1
            if a==(255,0,0):
                g[x][y]=2
    h=[]
    for x in range(size[0]):
        for y in range(size[1]):
            if g[x][y]==1:
                if b[x][y]!=1:
                    h=[x,y]
            elif g[x][y]==2:
                f=[x,y]
    if h!=[]:
        b=[[i for i in ii] for ii in g]
        if h[1]==0:
            if h[0]==0:
                pp.press('down')
            else:
                pp.press('left')
        elif h[0]==size[0]-1:
            pp.press('up')
        elif h[1]==size[1]-1:
            if h[0]&1:
                pp.press('up')
            else:
                pp.press('right')
        elif h[1]==1:
            if h[0]&1:
                pp.press('right')
            else:
                pp.press('down')
        elif h[0]==0:
            pp.press('down')
