import pygame
from pygame.locals import *
import sys



#２次元リストを作成
N = 40  #マス目
size = 20   #正方形の一辺の長さ
cells = [[0]*N for i_ in range(N)]

#ライフゲームのルールを適用させる
def rule(cells):
    dir = ( (-1,-1),(0,-1),(1,-1),
            (-1,0),         (1,0),
            (-1,1),(0,1),(1,1))
    #次世代のセルを定義
    tcells = [[0]*N for i_ in range(N)]

    #一番外側のセル以外にルールを適用
    for y in range(1, N-1):
        for x in range(1, N-1):
            c = 0   #生存セル
            for d in dir:
                if cells[y + d[1]][x + d[0]] == 1:
                    c += 1
            if cells[y][x] == 0 and c == 3:
                tcells[y][x] = 1
            if cells[y][x] == 1:
                if c == 2 or c == 3:
                    tcells[y][x] = 1
                else:
                    tcells[y][x] = 0
    return tcells


#描画する部分
pygame.init()
run = 0     #実行フラグ（0:停止、1:実行）
#サイズを指定して画面を生成
screen = pygame.display.set_mode((800,800))
while True:
    screen.fill((255,255,255))  #背景を白に

    if run == 1:
        cells = rule(cells) #セル更新
        pygame.time.wait(10)

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
        if e.type == KEYDOWN and e.key == pygame.K_RETURN:
            run = 1 - run

    pygame.display.update()
