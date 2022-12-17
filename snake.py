
import pygame,random
pygame.init()


size=[10,10]
sizer=20
dd=pygame.display.set_mode([size[0]*sizer,size[1]*sizer])
d=[0,0]
nd=[0,0]
f=[5,5]
s=[[0,0],[0,1],[0,2]]
while True:
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN:
            nd=d.copy()
            if e.key==pygame.K_UP and d[1]!=1:
                nd=[0,-1]
            if e.key==pygame.K_DOWN and d[1]!=-1:
                nd=[0,1]
            if e.key==pygame.K_LEFT and d[0]!=1:
                nd=[-1,0]
            if e.key==pygame.K_RIGHT and d[0]!=-1:
                nd=[1,0]
        elif e.type==pygame.QUIT:
            pygame.quit()
            herring
    d=nd.copy()
    if d!=[0,0]:
        s.append([s[-1][0]+d[0],s[-1][1]+d[1]])
        if f!=s[-1]:
            s.pop(0)
        else:
            x=[[a,b] for a in range(size[0]) for b in range(size[1])]
            for i in s:
                x.remove(i)
            f=random.choice(x)
        if s[-1][0]<0 or s[-1][1]<0 or s[-1][0]==size[0] or s[-1][1]==size[1]:
            pygame.quit()
        if s[-1] in s[:-1]:
            pygame.quit()
    dd.fill((0,0,0))
    for x in s:
        pygame.draw.rect(dd,(0,255,0),(x[0]*sizer,x[1]*sizer,sizer-2,sizer-2))
    pygame.draw.rect(dd,(255,0,0),(f[0]*sizer,f[1]*sizer,sizer-2,sizer-2))
    pygame.display.update()
    pygame.time.delay(200)
