#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
banner_linkedin
"""
# from PIL import Image, ImageDraw, ImageFont
#
# # Tamanho recomendado para o banner do LinkedIn
# banner_width = 1584
# banner_height = 396
#
# # Criando uma imagem em branco
# banner = Image.new('RGB', (banner_width, banner_height), color='white')
# draw = ImageDraw.Draw(banner)
#
# # Adicionando um texto ao banner
# font_size = 40
# font = ImageFont.load_default()  # Usando a fonte padrão, você pode ajustar conforme necessário
# text = "Alexandre Lorena\nDesenvolvedor Java | Python"
# text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]  # Ajuste aqui
#
# text_position = ((banner_width - text_width) // 2, (banner_height - text_height) // 2)
# draw.text(text_position, text, fill='black', font=font)
#
# # Salvando a imagem
# banner.save("linkedin_banner.png")
#
from PIL import Image, ImageDraw, ImageFont

# Tamanho recomendado para o banner do LinkedIn
banner_width = 1584
banner_height = 396

# Carregando a imagem de fundo
background_image = Image.open("images/banner-python.png")

# Redimensionando a imagem de fundo para as dimensões do banner
background_image = background_image.resize((banner_width, banner_height))

# Criando uma imagem em branco
banner = Image.new('RGB', (banner_width, banner_height), color='white')

# Colando a imagem de fundo no banner
banner.paste(background_image, (0, 0))

draw = ImageDraw.Draw(banner)

# Adicionando a frase no espaço vazio no canto direito
font_size_name = 40
font_size_job = 25

# Carregando uma fonte do sistema com os tamanhos especificados
font_path = "C:/Windows/Fonts/arial.ttf"  # Substitua pelo caminho da fonte desejada
font_name = ImageFont.truetype(font_path, font_size_name)
font_job = ImageFont.truetype(font_path, font_size_job)

name_text = "Alexandre Lorena"
job_text = "Developer (Java | Python)"

# Ajustando as coordenadas X e Y para o canto direito
name_text_position = (
    banner_width - draw.textbbox((30, 40), name_text, font=font_name)[2],
    (banner_height - draw.textbbox((0, 0), name_text, font=font_name)[3]) // 2 - 30  # Ajuste para descer mais o texto
)

job_text_position = (
    banner_width - draw.textbbox((30, 40), job_text, font=font_job)[2],
    name_text_position[1] + draw.textbbox((0, 0), name_text, font=font_name)[3] + 10  # Ajuste para reduzir a distância
)

draw.text(name_text_position, name_text, fill='darkgrey', font=font_name)
draw.text(job_text_position, job_text, fill='grey', font=font_job)

# Salvando a imagem
banner.save("linkedin_banner_com_fundo_dividido_canto_direito.png")













# from PIL import Image, ImageDraw, ImageFont
# from io import BytesIO
# from rich.console import Console
#
# # Tamanho recomendado para o banner do LinkedIn
# banner_width = 1584
# banner_height = 396
#
# # Criando uma imagem em branco com um fundo
# background_image_path = "images/banner8.jpg"  # Substitua pelo caminho da sua imagem de fundo
# background_image = Image.open(background_image_path)
# banner = Image.new('RGB', (banner_width, banner_height), color='white')
# banner.paste(background_image, (0, 0))
#
# draw = ImageDraw.Draw(banner)
#
# # Adicionando a mensagem "Eu sou programador Python" ao banner
# message = "I am a Python programmer"
# font_size = 40
# font = ImageFont.load_default()  # Usando a fonte padrão, você pode ajustar conforme necessário
# text_width, text_height = draw.textbbox((0, 0), message, font=font)[2:]  # Ajuste aqui
#
# text_position = ((banner_width - text_width) // 2, (banner_height - text_height) // 2)
# draw.text(text_position, message, fill='black', font=font)
#
# # Criando um objeto Console para obter a saída formatada
# console = Console()
#
# # Capturando a saída do console.print
# with console.capture() as capture:
#     console.print("[black]with open('filmes.csv', 'w', encoding='utf-8') as arquivo:\n"
#                   "    escritor_csv = writer(arquivo)\n    filme = None\n    escritor_csv.writerow"
#                   "(['Título', 'Gênero', 'Duração'])  [white]# este método trabalha com lista\n"
#                   "[black]    while filme != 'sair':\n        filme = input('Informe o nome do filme: ')\n"
#                   "        if filme != 'sair':\n            genero = input('Informe o gênero do filme: ')\n"
#                   "            duracao = input('Informe a duração do filme: ')\n"
#                   "            escritor_csv.writerow([filme, genero, duracao])\n\n")
#
# # Obtendo a saída do console após o término do bloco `with`
# console_output = capture.get()
#
# # Adicionando o texto do console.print à imagem
# console_text_width, console_text_height = draw.textbbox((0, 0), console_output, font=font)[2:]
# console_text_position = ((banner_width - console_text_width) // 2, (banner_height - console_text_height) // 2 + text_height + 20)
# draw.text(console_text_position, console_output, fill='black', font=font)
#
# # Salvando a imagem
# banner.save("linkedin_banner_python_programmer.png")

