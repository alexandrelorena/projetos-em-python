#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Fore
from rich.console import Console
from PIL import Image, ImageDraw
import os
import cores_unificadas

# Inicializa o colorama
init(autoreset=True)

# def imprimir_com_cor(nome_cor, codigo_hex):
#     try:
#         # Obtém a cor formatada
#         cor_formatada = getattr(Fore, nome_cor.upper())
#         # Obtém os valores RGB
#         rgb = tuple(int(codigo_hex[i:i + 2], 16) for i in (1, 3, 5))
#
#         # Imprime o nome da cor com a cor e as informações de hexadecimal e RGB
#         print(f"{cor_formatada}{nome_cor}", end="")
#
#         # Imprime as informações de hexadecimal e RGB usando colorama
#         print(
#             f" - {Fore.YELLOW}Hex:{Fore.RESET} {Fore.CYAN}{codigo_hex}{Fore.RESET} - {Fore.GREEN}RGB:{Fore.RESET} {Fore.CYAN}{rgb}{Fore.RESET}")
#     except AttributeError:
#         # Se a cor não for suportada, imprime apenas o valor hexadecimal e RGB
#         rgb = tuple(int(codigo_hex[i:i + 2], 16) for i in (1, 3, 5))
#         print(f"{nome_cor} não suportada: Hex: {codigo_hex} - RGB: {rgb}")


# Tamanho da imagem
width = 350
height = 20

# Cria o diretório 'images' se ele não existir
os.makedirs("images", exist_ok=True)

# Percorre a lista de cores e salva as imagens
for nome_cor, cor_info in cores_unificadas.cores_unificadas.items():
    cor_rgb = cor_info['rgb']

    # Cria uma imagem em branco com as dimensões corretas
    image = Image.new('RGB', (width, height), color=cor_rgb)

    # Cria um objeto ImageDraw para desenhar na imagem
    draw = ImageDraw.Draw(image)

    # Salva a imagem
    try:
        image.save(f"images/imagem_{nome_cor}.png")
        print(f"Imagem para {nome_cor} salva com sucesso.")
    except FileNotFoundError:
        print(f"O diretório 'images' não existe. Crie o diretório antes de salvar a imagem.")
    except Exception as e:
        print(f"Erro ao salvar a imagem para {nome_cor}: {e}")

# Agora, vamos criar o arquivo HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
<script>
    // Função para escolher uma cor aleatória da lista
    function escolherCorAleatoria() {
        // Obtém todas as células de cor disponíveis
        var colorCells = document.querySelectorAll('.light-text');

        // Lista de cores disponíveis
        var cores = [];

        // Obtém as cores da lista de células
        colorCells.forEach(function(cell) {
            var color = cell.style.color;
            cores.push(color);
        });

        // Escolhe uma cor aleatória da lista
        var corAleatoria = cores[Math.floor(Math.random() * cores.length)];

        // Aplica a cor ao fundo da página
        document.body.style.backgroundColor = corAleatoria;
    }

    // Chama a função ao carregar a página
    window.onload = escolherCorAleatoria;

    // Adiciona um ouvinte de evento para cada célula de cor
    var colorCells = document.querySelectorAll('.light-text');

    colorCells.forEach(function(cell) {
        // Mouseover para mudar a cor do cursor
        cell.addEventListener('mouseover', function() {
            var color = cell.style.color;
            changeMouseColor(color);
        });
        // Mouseout para restaurar a cor padrão do cursor
        cell.addEventListener('mouseout', function() {
            resetMouseColor();
        });

        // Click para mudar a cor de fundo da página
        cell.addEventListener('click', function() {
            var color = cell.style.color;
            changeBackgroundColor(color);
        });
    });

    // Adiciona um ouvinte de evento para cada célula de imagem
    var imageCells = document.querySelectorAll('td img');

    imageCells.forEach(function(cell) {
        // Mouseover para mudar a cor do cursor
        cell.addEventListener('mouseover', function() {
            var color = cell.parentNode.previousElementSibling.style.color;
            changeMouseColor(color);
        });
        // Mouseout para restaurar a cor padrão do cursor
        cell.addEventListener('mouseout', function() {
            resetMouseColor();
        });

        // Click para mudar a cor de fundo da página
        cell.addEventListener('click', function() {
            var color = cell.parentNode.previousElementSibling.style.color;
            changeBackgroundColor(color);
        });
    });

// Função para mudar a cor do cursor
function changeMouseColor(color) {
    document.body.style.cursor = `url("data:image/svg+xml,%3Csvg height='0' width='0' xmlns='http://www.w3.org/2000/svg'%3E%3C/style%3E%3C/svg%3E"), auto`;
    document.body.style.setProperty('--cursor-color', color);
}
    // Função para restaurar a cor padrão do cursor
    function resetMouseColor() {
        document.body.style.cursor = 'auto';
    }

    // Função para mudar a cor de fundo da página
    function changeBackgroundColor(color) {
        document.body.style.backgroundColor = color;
    }
</script>



    <style>
        body {
            background-color: #eeeeee; /* Cor de fundo do corpo da página */
            font-family: Arial, sans-serif;
            letter-spacing: 1px; /* Ajuste o valor conforme necessário */
        }
        
        table {
            font-family: Arial, sans-serif;
            letter-spacing: 1px; /* Ajuste o valor conforme necessário */
            border-collapse: collapse;
            width: 60%; /* Largura da tabela definida para 60% da largura da página */
            margin: 0 auto; /* Centraliza a tabela na página */
            background-color: #ffffff; /* Cor de fundo da tabela */
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2; /* Cor de fundo das células de cabeçalho */
            position: sticky;
            top: 0;
            z-index: 1;
        }
        img {
            width: 100%;
            height: auto;
        }
        .light-text {
            font-weight: lighter;
            text-shadow: 0.7px 0.7px 1px #000000; /* Ajuste os valores conforme necessário */
        }
            /* Adiciona um estilo personalizado para a cor do cursor */
    body {
        cursor: url("data:image/svg+xml,%3Csvg height='0' width='0' xmlns='http://www.w3.org/2000/svg'%3E%3C/style%3E%3C/svg%3E"), auto;
    }

    body:hover {
        cursor: url("data:image/svg+xml,%3Csvg fill='var(--cursor-color)' height='24' width='24' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3C/svg%3E"), auto;
    }
    </style>
</head>
<body>

<table>
    <tr>
        <th style="width: 350px;"><font color="Gray"> :::::::::::::::::::: COR | HEXA | RGB :::::::::::::::::::: </font></th>
        <th><font color="Gray"> :::::::::::::: REPRESENTAÇÃO DA COR :::::::::::::: </font></th>
    </tr>
"""

# Adiciona as linhas da tabela ao HTML
for nome_cor, cor_info in cores_unificadas.cores_unificadas.items():
    cor_rgb = cor_info['rgb']
    cor_hex = '#%02x%02x%02x' % cor_rgb

    # Adicione a classe 'light-text' para adicionar uma borda ao texto
    html_content += f"""
    <tr>
        <td style="font-size: 15px; color: {cor_hex};" class="light-text">{nome_cor} | {cor_hex} | {cor_rgb}</td>
        <td style="width: 350px; height: 20px;"><img src="images/imagem_{nome_cor}.png" alt="{nome_cor}" height="20"></td>
    </tr>
    
"""

# Fecha o HTML
html_content += """
</table>
<!-- Adicione o script JavaScript -->
<script>
    // Adicione um ouvinte de evento para cada célula de cor
    var colorCells = document.querySelectorAll('.light-text');

    colorCells.forEach(function(cell) {
        // Mouseover para mudar a cor do cursor
        cell.addEventListener('mouseover', function() {
            var color = cell.style.color;
            changeMouseColor(color);
        });

        // Click para mudar a cor de fundo da página
        cell.addEventListener('click', function() {
            var color = cell.style.color;
            changeBackgroundColor(color);
        });
    });

    // Adicione um ouvinte de evento para cada célula de imagem
    var imageCells = document.querySelectorAll('td img');

    imageCells.forEach(function(cell) {
        // Mouseover para mudar a cor do cursor
        cell.addEventListener('mouseover', function() {
            var color = cell.parentNode.previousElementSibling.style.color;
            changeMouseColor(color);
        });
        // Mouseout para restaurar a cor padrão do cursor
        cell.addEventListener('mouseout', function() {
            resetMouseColor();
        });
        // Click para mudar a cor de fundo da página
        cell.addEventListener('click', function() {
            var color = cell.parentNode.previousElementSibling.style.color;
            changeBackgroundColor(color);
        });
    });

    // Função para mudar a cor do cursor
    function changeMouseColor(color) {
        document.body.style.cursor = `url("data:image/svg+xml,%3Csvg fill='${color}' height='24' width='24' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3C/svg%3E"), auto`;
    }

    // Função para mudar a cor de fundo da página
    function changeBackgroundColor(color) {
        document.body.style.backgroundColor = color;
    }
</script>
</body>
</html>
"""

# Salva o conteúdo HTML em um arquivo
with open("cores_table.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("Arquivo HTML criado com sucesso.")
