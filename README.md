# Quebra Tijolo

Jogo estilo Breakout feito em Python com Pygame. Controle a barra, rebata a bola e destrua todos os blocos coloridos sem deixar a bola cair.

Projeto de estudo para praticar Python, lógica de jogos e organização de código.

![Gameplay do Quebra Tijolo](docs/gameplay.gif)

## Funcionalidades

- Bola que quica nas paredes, na barra e nos blocos
- O ângulo da bola muda conforme o ponto da barra em que ela bate
- 40 blocos (8 colunas x 5 linhas) com cores aleatórias
- Pontuação: 10 pontos por bloco destruído
- Os blocos reaparecem quando todos são destruídos
- Tela de Game Over quando a bola cai

## Como rodar

Você precisa do Python 3 instalado.

```bash
git clone https://github.com/7yuri1/Pong.git
cd Pong
pip install pygame
python jogo.py
```

## Controles

| Tecla | Ação |
|-------|------|
| ← | Move a barra para a esquerda |
| → | Move a barra para a direita |

## Tecnologias

- Python 3
- Pygame

## O que aprendi

- Diferença entre ler eventos (`pygame.event`) e ler o estado das teclas (`pygame.key.get_pressed()`) para um movimento contínuo
- Por que testar colisão com um ponto só é frágil, e como o `Rect.colliderect` resolve
- Escopo de variáveis em Python: quando é preciso usar `global` e o que acontece sem ele
- `Rect` guarda coordenadas inteiras, então velocidades decimais precisam ser arredondadas
- Como evitar que a bola "grude" na barra, invertendo a direção apenas quando ela está descendo

## Próximos passos

- [ ] Fixar a velocidade com `Clock().tick(60)`
- [ ] Gerar as cores dos blocos de forma mais simples e sem tons escuros demais
- [ ] Refatorar com classes (`Bola`, `Barra`, `Bloco`)
- [ ] Adicionar vidas e opção de reiniciar após o Game Over
- [ ] Tratar a colisão lateral nos blocos
