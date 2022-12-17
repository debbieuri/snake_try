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
b=[[0 for _ in range(size[1])] for _ in range(size[0])]
for x in range(size[0]):
    for y in range(size[1]):
        a=z.getpixel((s[0]+x*ss,s[1]+y*ss))
        if a==(0,255,0):
            b[x][y]=1
        if a==(255,0,0):
            b[x][y]=2
pp.press('down')
d=[0,1]
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
        print(h)
        if f[0]<h[0]:
            pp.press('left')
        if f[0]>h[0]:
            pp.press('right')
        if f[1]<h[1]:
            pp.press('up')
        if f[1]>h[1]:
            pp.press('down')
    else:
        print('aaaa')
