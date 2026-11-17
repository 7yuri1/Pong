import pygame
import random
import time

# start
pygame.init()

tamanho_tela = (1080, 900)
tela = pygame.display.set_mode(tamanho_tela)
titulo = pygame.display.set_caption("Quebra Tijolo")


qtde_blocos_linhas = 8
qtde_linhas_blocos = 5
blocos = qtde_blocos_linhas * qtde_linhas_blocos

tamanho_bola = 20
bola = pygame.Rect(200, 600, tamanho_bola, tamanho_bola)
tamanho_player = 200
player = pygame.Rect(500, 800, tamanho_player, 15)

fim_jogo = False
pontos = 0
movimento_bola = [5, -5]


# criando funções

def movimentar_player():
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        player.x = player.x + 5

    if teclas[pygame.K_LEFT]:
        player.x = player.x - 5

    if player.x < 0:
        player.x = 0

    if player.x >= tamanho_tela[0] - tamanho_player:
        player.x = tamanho_tela[0] - tamanho_player


def movimentar_bola(bola):
    global fim_jogo
    global pontos
    movimento = movimento_bola

    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]

    if bola.y <= 0:
        movimento[1] = - movimento[1]

    if bola.x + tamanho_bola >= tamanho_tela[0]:
        movimento[0] = - movimento[0]

    
        
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        tela_gameover()
        time.sleep(3)
        fim_jogo = True

    if player.colliderect(bola) and movimento[1] > 0:
            movimento[1] = - movimento[1]
            centro_bola = bola.centerx
            centro_player = player.centerx

            diferenca = centro_bola - centro_player
            movimento[0] = round(diferenca / 15)
            bola.bottom = player.top
    
    for bloco, cor in blocos:
        if bloco.colliderect(bola):
            blocos.remove((bloco, cor))
            movimento[1] = - movimento[1]
            pontos += 10
            break

    return movimento

def atualizar_pontuacao(pontos):
    fonte = pygame.font.Font(None, 30)
    text = fonte.render(f"Points: {pontos}", 1, cores["Branco"])
    tela.blit(text, (30, 850))


def tela_gameover():
    fonte = pygame.font.SysFont("arial", 65, bold=True)
    text = fonte.render("Game Over", True, cores["Branco"])
    x = (tamanho_tela[0] - text.get_width()) / 2
    y = 300
    tela.blit(text,(x,y))
    pygame.display.flip()





# desenhos


def criar_blocos(qtde_blocos_linhas, qtde_linhas_blocos):
    largura_tela = tamanho_tela[0]
    altura_tela = tamanho_tela[1]

    distancia_entre_x = 5
    largura_bloco = largura_tela / qtde_blocos_linhas - distancia_entre_x
    altura_bloco = 15
    blocos = []
    distancia_entre_y = altura_bloco + 10

    for y in range(qtde_linhas_blocos):
        for i in range(qtde_blocos_linhas):

            bloco = pygame.Rect(i * (largura_bloco + distancia_entre_x), y * distancia_entre_y, largura_bloco, altura_bloco)
            cor = cores_bloco()
            blocos.append((bloco, cor))
    
    return blocos

def cores_bloco():
    cor = [
        # Vermelhos
        (255, 0, 0), (220, 20, 60), (178, 34, 34),
        (255, 69, 0), (255, 99, 71), (205, 92, 92),
        (240, 128, 128), (250, 128, 114),

        # Laranjas
        (255, 165, 0), (255, 140, 0), (255, 127, 80),
        (255, 160, 122), (255, 69, 0), (210, 105, 30),

        # Amarelos
        (255, 255, 0), (255, 215, 0), (255, 223, 0),
        (238, 232, 170), (240, 230, 140), (255, 250, 205),

        # Verdes
        (0, 255, 0), (0, 128, 0), (34, 139, 34),
        (50, 205, 50), (124, 252, 0), (127, 255, 0),
        (0, 250, 154), (0, 255, 127), (144, 238, 144),
        (152, 251, 152), (46, 139, 87), (85, 107, 47),

        # Cianos
        (0, 255, 255), (0, 206, 209), (64, 224, 208),
        (72, 209, 204), (175, 238, 238), (127, 255, 212),

        # Azuis
        (0, 0, 255), (0, 0, 139), (0, 0, 205),
        (30, 144, 255), (65, 105, 225), (70, 130, 180),
        (100, 149, 237), (135, 206, 235), (135, 206, 250),
        (173, 216, 230), (25, 25, 112), (0, 191, 255),

        # Roxos
        (128, 0, 128), (148, 0, 211), (138, 43, 226),
        (153, 50, 204), (186, 85, 211), (218, 112, 214),
        (221, 160, 221), (238, 130, 238), (255, 0, 255),
        (147, 112, 219), (230, 230, 250),

        # Rosas
        (255, 192, 203), (255, 105, 180), (255, 20, 147),
        (219, 112, 147), (199, 21, 133), (255, 182, 193),
        (255, 228, 225), (255, 240, 245),

        # Marrons
        (139, 69, 19), (160, 82, 45), (210, 105, 30),
        (205, 133, 63), (222, 184, 135), (244, 164, 96),
        (188, 143, 143), (101, 67, 33),

        # Cinzas e neutros
        (0, 0, 0), (105, 105, 105), (128, 128, 128),
        (169, 169, 169), (192, 192, 192), (211, 211, 211),
        (220, 220, 220), (245, 245, 245), (255, 255, 255),

        # Tons especiais
        (255, 250, 205), (255, 228, 181), (255, 218, 185),
        (250, 235, 215), (127, 255, 212), (189, 183, 107),
        (176, 224, 230), (255, 250, 240), (240, 255, 240),
        (245, 255, 250), (240, 248, 255), (248, 248, 255)
    ]

    return random.choice(cor)    

cores = {
    "Branco": (255,255,255),
    "Ciano": (0,255,255),
    "Rosa": (255,192,203),
    "Preto": (2,2,2)
}



def desenhar_inicio_jogo():
    tela.fill(cores["Preto"])
    pygame.draw.rect(tela, cores["Ciano"], player)
    pygame.draw.rect(tela, cores["Branco"], bola)

def desenhar_blocos(blocos):
    for bloco, cor in blocos:
        pygame.draw.rect(tela, cor, bloco)



blocos = criar_blocos(qtde_blocos_linhas, qtde_linhas_blocos)



# loop
while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    atualizar_pontuacao(pontos)
    movimentar_player()

    if not blocos:
        blocos = criar_blocos(qtde_blocos_linhas, qtde_linhas_blocos)


    movimento_bola = movimentar_bola(bola)

    pygame.time.wait(1)
    pygame.display.flip()
pygame.quit()