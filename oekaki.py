import pygame
from pygame.locals import *
import sys

pygame.init()
#サイズを指定して画面を生成
screen = pygame.display.set_mode((800,800))
#２次元リストを作成
N = 40  #マス目
size = 20   #正方形の一辺の長さ
cells = [[0]*N for i_ in range(N)]

while True:
    screen.fill((255,255,255))  #背景を白に

    #正方形を描画する
    for y in range(0,N):
        for x in range(0,N):
            if cells[y][x] == 1:
                #正方形を設定
                rect = Rect(x*size, y*size, size, size)
                #正方形を描画
                pygame.draw.rect(screen, (0,255,0), rect)


    #マウス入力
    for e in pygame.event.get():
        if e.type == MOUSEBUTTONDOWN:
            mx, my = int(e.pos[0]/size), int(e.pos[1]/size)
            cells[my][mx] = 1 - cells[my][mx]
        if e.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
