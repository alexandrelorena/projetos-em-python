#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
game-linkedin
"""

import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Configurações da animação
CODE_SPEED = 5  # Velocidade de queda do código
NEW_LINE_INTERVAL = 30  # Intervalo para adicionar nova linha de código

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Code Animation")
clock = pygame.time.Clock()

# Fonte para o código
font = pygame.font.Font(None, 36)

# Lista de partes de código
code_lines = []

# Função para criar uma nova linha de código
def create_code_line():
    code_line_text = "<html>"  # Substitua pelo código desejado
    code_line = font.render(code_line_text, True, GREEN)
    code_lines.append({
        'surface': code_line,
        'rect': code_line.get_rect(center=(random.randint(50, WIDTH - 50), 0))
    })

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Adiciona uma nova linha de código em intervalos regulares
    if random.randint(0, NEW_LINE_INTERVAL) == 0:
        create_code_line()

    # Move as linhas de código para baixo
    for code_line in code_lines:
        code_line['rect'].move_ip(0, CODE_SPEED)

    # Remove as linhas que caíram abaixo da tela
    code_lines = [code_line for code_line in code_lines if code_line['rect'].top < HEIGHT]

    # Preenche a tela com a cor branca
    screen.fill(WHITE)

    # Desenha as linhas de código na tela
    for code_line in code_lines:
        screen.blit(code_line['surface'], code_line['rect'])

    pygame.display.flip()
    clock.tick(FPS)
