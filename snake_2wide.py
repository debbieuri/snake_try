import pygame,random
pygame.init()

size=[20,20]
sizer=20
dd=pygame.display.set_mode([size[0]*sizer,size[1]*sizer])
d=2
od=2
f=[5,5]
s=[[[0,0],[1,0]],[[0,1],[1,1]],[[0,2],[1,2]]]
ways=[[0,-1],[1,0],[0,1],[-1,0]]
def q():
    x=[[s[-1][i][0]+ways[d][0],s[-1][i][1]+ways[d][1]] for i in range(2)]
    for i in s[-1]:
        if i in x:
            x.remove(i)
    for i in s[:-1]:
        for ii in i:
            for iii in x:
                if iii == ii:
                    if od!=d:
                        return od
                    else:
                        pygame.quit()
    return d
while True:
    od=d
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_UP and od!=2:
                d=0
            if e.key==pygame.K_DOWN and od!=0:
                d=2
            if e.key==pygame.K_LEFT and od!=1:
                d=3
            if e.key==pygame.K_RIGHT and od!=3:
                d=1
        elif e.type==pygame.QUIT:
            pygame.quit()
            herring
    w=s.pop(0)
    d=q()
    if od==d:
        s.append([[s[-1][i][0]+ways[d][0],s[-1][i][1]+ways[d][1]] for i in range(2)])
    else:
        if (d-od)%4==1:
            x=[[s[-1][-1][0]+ways[d][0]+i*ways[d-1][0],s[-1][-1][1]+ways[d][1]+i*ways[d-1][1]] for i in range(2)]
        else:
            x=[[s[-1][0][0]+ways[d][0]+i*ways[(d+1)%4][0],s[-1][0][1]+ways[d][1]+i*ways[(d+1)%4][1]] for i in range(2)]
        if [x[0][0]-x[1][0],x[0][1]-x[1][1]]==ways[(d-1)%4]:##carefule if length is 1?
            x.reverse()
        s.append(x)
    if f in s[-1]:
        s.insert(0,w)
        x=[[a,b] for a in range(size[0]) for b in range(size[1])]
        x.remove([0,0])
        x.remove([size[0]-1,0])
        x.remove([0,size[1]-1])
        x.remove([size[0]-1,size[1]-1])#thick snake can't get corner... ?? :(
        for ii in s:
            for i in ii:
                if i in x:
                    x.remove(i)
        f=random.choice(x)
    for i in range(2):
        if s[-1][i][0]<0 or s[-1][i][1]<0 or s[-1][i][0]==size[0] or s[-1][i][1]==size[1]:
            pygame.quit()
    dd.fill((0,0,0))
    for xx in s:
        for x in xx:
            pygame.draw.rect(dd,(0,255,0),(x[0]*sizer,x[1]*sizer,sizer-2,sizer-2))
    pygame.draw.rect(dd,(255,0,0),(f[0]*sizer,f[1]*sizer,sizer-2,sizer-2))
    pygame.display.update()
    pygame.time.delay(150)
