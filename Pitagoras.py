import pygame
from pygame.locals import *
from math import sqrt, pi

pygame.init()

#Definindo janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Esferas')

#Esfera Principal
raio = 15
posX = largura / 2
posY = altura / 2
cor = (255, 200, 0)
colidir = 'Não'

#Esfera secundária
raio2 = 15
pos_x = posX + 30
pos_y = posY - 30
cor2 = (255, 255, 255)

#Cores - Linhas
cor_hi = (255, 0, 0)
cor_ca = (0, 255, 0)
cor_co = (0, 0, 255)

#Clock da janela
clock = pygame.time.Clock()

def checar_colisao(x1, x2, y1, y2, r1, r2):
    distancia_x = x1 - x2
    distancia_y = y1 - y2
    distancia = sqrt((distancia_x ** 2) + (distancia_y ** 2))
    if distancia <= r1 + r2:
        return True
    else:
        return False

#Fonte para textos
fonte = pygame.font.SysFont('Arial', 20, True, False)

#Loop do programa
while True:
    h = sqrt(((posX - pos_x) ** 2) + ((posY - pos_y) ** 2))
    c1 = sqrt((posX - pos_x) ** 2)
    c2 = sqrt((posY - pos_y) ** 2)
    hipotenusa = f'Hipotenusa: {h:.2f}'
    cateto1 = f'Cateto(O): {c1:.2f}'
    cateto2 = f'Cateto(A): {c2:.2f}'
    raiop = f'Raio(P): {raio}'
    raios = f'Raio(S): {raio2}'
    Colisao = 'Colisão: ' + colidir

    clock.tick(60)
    janela.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            exit()

    #paredes
    if posX < raio / 3:
        posX = largura - raio / 3 - 1
    elif posX > largura - raio / 3:
        posX = raio / 3 + 1
    elif posY < raio / 3:
        posY = altura - raio / 3 - 1
    elif posY > altura - raio / 3:
        posY = raio / 3 + 1

    if pos_x < raio2 / 3:
        pos_x = largura - raio2 / 3 - 1
    elif pos_x > largura - raio2 / 3:
        pos_x = raio2 / 3 + 1
    elif pos_y < raio2 / 3:
        pos_y = altura - raio2 / 3 - 1
    elif pos_y > altura - raio2 / 3:
        pos_y = raio2 / 3 + 1

    #Movimentação - primária
    if pygame.key.get_pressed()[K_w]:
        posY = posY - 2
    elif pygame.key.get_pressed()[K_s]:
        posY = posY + 2
    elif pygame.key.get_pressed()[K_d]:
        posX = posX + 2
    elif pygame.key.get_pressed()[K_a]:
        posX = posX - 2

    #Movimentação - secundária
    if pygame.key.get_pressed()[K_UP]:
        pos_y = pos_y - 2
    elif pygame.key.get_pressed()[K_DOWN]:
        pos_y = pos_y + 2
    elif pygame.key.get_pressed()[K_RIGHT]:
        pos_x = pos_x + 2
    elif pygame.key.get_pressed()[K_LEFT]:
        pos_x = pos_x - 2
    
    if pygame.key.get_pressed()[K_1]:
        raio += 1
    elif pygame.key.get_pressed()[K_2]:
        raio -= 1
    elif pygame.key.get_pressed()[K_3]:
        raio2 += 1
    elif pygame.key.get_pressed()[K_4]:
        raio2 -= 1

    #Objetos da tela
    esfera = pygame.draw.circle(janela, cor, (posX, posY), raio)
    esfera2 = pygame.draw.circle(janela, cor2, (pos_x, pos_y), raio2)

    #linhas
    hipotenusa_linha = pygame.draw.line(janela, cor_hi, (posX, posY), (pos_x, pos_y), 5)
    cateto1_linha = pygame.draw.line(janela, cor_ca, (posX, posY), (posX, pos_y), 5)
    cateto2_linha = pygame.draw.line(janela, cor_co, (pos_x, pos_y), (posX, pos_y), 5)

    #Verificando colisões
    if checar_colisao(posX, pos_x, posY, pos_y, raio, raio2):
        colidir = 'Sim'
    else:
        colidir = 'Não'

    #Placar
    hi = fonte.render(hipotenusa, True, (255, 255, 255))
    co = fonte.render(cateto1, True, (255, 255, 255))
    ca = fonte.render(cateto2, True, (255, 255, 255))
    rp = fonte.render(raiop, True, (255, 255, 255))
    rs = fonte.render(raios, True, (255, 255, 255))
    estado = fonte.render(Colisao, True, (255, 255, 255))
    janela.blit(hi, (610, 30))
    janela.blit(ca, (610, 60))
    janela.blit(co, (610, 90))
    janela.blit(rp, (610, 120))
    janela.blit(rs, (610, 150))
    janela.blit(estado, (610, 180))
    pygame.display.update()