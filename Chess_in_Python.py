# Um jogo de Xadrez para dois jogadores desenvolvido em Python através da biblioteca Pygame

# Primeira parte do Código: Declaração das Funções e Variáveis

import pygame
import sys
from PIL import Image
import random
import io
import os
import time
import soundfile as sf

pygame.init()
pygame.mixer.init()

info = pygame.display.Info() # Função para adaptar a tela á direntes máquinas

height_screen_proportion = info.current_h / (112 / 9)
width_screen_proportion = info.current_w / (1366 / 800)

# Função para calcular a proporção para diferentes máquinas
def proportion_calculation(number):
    proportion = width_screen_proportion / (800/number) 

    return int(proportion)

pc = proportion_calculation

WIDTH = info.current_w
HEIGHT = info.current_h - height_screen_proportion
screen = pygame.display.set_mode([WIDTH, HEIGHT])

color_menu = (206, 162, 119)
color_rect_menu = (205,133,63)
first_color_square = (205,133,63)
second_color_square = (240, 217, 181)
color_rect_captured_pieces = (181, 136, 99)
color_bars_captured_pieces = 'gold'

pygame.display.set_caption('Chess')

def resize_images_with_pillow(image_path, width, height):
    pill_image = Image.open(image_path)
    pill_image_resized = pill_image.resize((width, height), Image.Resampling.LANCZOS)
    
    image_bytes = io.BytesIO()
    pill_image_resized.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    
    pygame_image = pygame.image.load(image_bytes)
    
    return pygame_image

pygame.display.set_icon(resize_images_with_pillow('assets/images/black knight.png', pc(64), pc(64)))
font = pygame.font.Font('freesansbold.ttf', pc(16))
smaller_font = pygame.font.Font('freesansbold.ttf', pc(28))
medium_font = pygame.font.Font('freesansbold.ttf', pc(32))
big_font = pygame.font.Font('freesansbold.ttf', pc(40))

font_180 = pygame.font.SysFont('Georgia', pc(180))
font_170 = pygame.font.SysFont('Georgia', pc(170))
font_140 = pygame.font.SysFont('Georgia', pc(140))
font_80 = pygame.font.SysFont('Georgia', pc(80))
font_90 = pygame.font.SysFont('Georgia', pc(90))
font_70 = pygame.font.SysFont('Georgia', pc(70))
font_60 = pygame.font.SysFont('Georgia', pc(60))
font_55 = pygame.font.SysFont('Georgia', pc(55))
font_50 = pygame.font.SysFont('Georgia', pc(50))
font_45 = pygame.font.SysFont('Georgia', pc(45))
font_40 = pygame.font.SysFont('Georgia', pc(40))

language_items = [('ENGLISH'), ('PORTUGUÊS'), ('ESPAÑOL')]

timer = pygame.time.Clock()
fps = 60
audio = True

english = True
portuguese = False
spanish = False

def increase_audio_volume(audio_file, output_folder):
    # Garantir que a pasta de saída existe
    os.makedirs(output_folder, exist_ok=True)

    # Carregar o áudio
    audio, sr = sf.read(audio_file)

    # Aumentar o volume (multiplicar o sinal)
    louder_audio = audio * 1.5  # Ajuste o fator conforme necessário

    # Gerar o caminho completo do arquivo de saída
    output_file = os.path.join(output_folder, "louder_audio.wav")

    # Salvar o áudio ajustado
    sf.write(output_file, louder_audio, sr)
    
    # Retornar o caminho do arquivo salvo
    return output_file

sound_button = pygame.mixer.Sound(increase_audio_volume('audio/button click song.mp3', 'audio'))
movie_piece_song_1 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 1.mp3', 'audio'))
movie_piece_song_2 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 2.mp3', 'audio'))
movie_piece_song_3 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 3.mp3', 'audio'))
movie_piece_song_4 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 4.mp3', 'audio'))
movie_piece_song_5 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 5.mp3', 'audio'))
movie_piece_song_6 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 6.mp3', 'audio'))
movie_piece_song_7 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 7.wav', 'audio'))
movie_piece_song_8 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 8.wav', 'audio'))
movie_piece_song_9 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 9.wav', 'audio'))
movie_piece_song_10 = pygame.mixer.Sound(increase_audio_volume('audio/piece movie song 10.wav', 'audio'))
win_game_song = pygame.mixer.Sound(increase_audio_volume('audio/win game song.wav', 'audio'))
captured_piece_song_1 = pygame.mixer.Sound(increase_audio_volume('audio/captured piece song 1.mp3', 'audio'))
captured_piece_song_2 = pygame.mixer.Sound(increase_audio_volume('audio/captured piece song 2.mp3', 'audio'))
captured_piece_song_3 = pygame.mixer.Sound(increase_audio_volume('audio/captured piece song 3.mp3', 'audio'))
captured_piece_song_4 = pygame.mixer.Sound(increase_audio_volume('audio/captured piece song 4.mp3', 'audio'))
start_game_song = pygame.mixer.Sound(increase_audio_volume('audio/start game song.mp3', 'audio'))

# Variáveis do jogo, imagens e seus tamanhos
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

white_pieces_one_player = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                           'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations_one_player = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                              (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces_one_player = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                           'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations_one_player = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                              (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []
captured_pieces_white_one_player = []
captured_pieces_black_one_player = []

prior_white_locations = white_locations
prior_black_locations = black_locations
prior_white_locations_one_player = white_locations_one_player
prior_black_locations_one_player = black_locations_one_player

save_prior_captured_piece = False
save_prior_captured_piece_one_player = False

prior_captured_white_pieces = []
prior_captured_black_pieces = []
prior_captured_white_pieces_one_player = []
prior_captured_black_pieces_one_player = []

last_captured_piece_black = None
last_captured_piece_white = None
last_captured_piece_black_one_player = None
last_captured_piece_white_one_player = None

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
turn_step_one_player = 0
selection = 100
selection_one_player = 100
valid_moves = []
valid_moves_one_player = []
no_undo = False
no_undo_one_player = False
no_undo_one_player = False
possible_locations_to_play = []
possible_pieces_to_play = []

# Carrega as peças do jogo (rainha, rei, torre, bispo, cavalo, peão) x 2
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
# Redimensionando as imagens com pillow

black_queen = resize_images_with_pillow('assets/images/black queen.png', pc(64), pc(64))
black_queen_small = resize_images_with_pillow('assets/images/black queen.png', pc(36), pc(36))
black_king = resize_images_with_pillow('assets/images/black king.png', pc(64), pc(64))
black_king_small = resize_images_with_pillow('assets/images/black king.png', pc(36), pc(36))
black_rook = resize_images_with_pillow('assets/images/black rook.png', pc(64), pc(64))
black_rook_small = resize_images_with_pillow('assets/images/black rook.png', pc(36), pc(36))
black_bishop = resize_images_with_pillow('assets/images/black bishop.png', pc(64), pc(64))
black_bishop_small = resize_images_with_pillow('assets/images/black bishop.png', pc(36), pc(36))
black_knight = resize_images_with_pillow('assets/images/black knight.png', pc(64), pc(64))
black_knight_small = resize_images_with_pillow('assets/images/black knight.png', pc(36), pc(36))
black_pawn = resize_images_with_pillow('assets/images/black pawn.png', pc(52), pc(52))
black_pawn_small = resize_images_with_pillow('assets/images/black pawn.png', pc(36), pc(36))
white_queen = resize_images_with_pillow('assets/images/white queen.png', pc(64), pc(64))
white_queen_small = resize_images_with_pillow('assets/images/white queen.png', pc(36), pc(36))
white_king = resize_images_with_pillow('assets/images/white king.png', pc(64), pc(64))
white_king_small = resize_images_with_pillow('assets/images/white king.png', pc(36), pc(36))
white_rook = resize_images_with_pillow('assets/images/white rook.png', pc(64), pc(64))
white_rook_small = resize_images_with_pillow('assets/images/white rook.png', pc(36), pc(36))
white_bishop = resize_images_with_pillow('assets/images/white bishop.png', pc(64), pc(64))
white_bishop_small = resize_images_with_pillow('assets/images/white bishop.png', pc(36), pc(36))
white_knight = resize_images_with_pillow('assets/images/white knight.png', pc(64), pc(64))
white_knight_small = resize_images_with_pillow('assets/images/white knight.png', pc(36), pc(36))
white_pawn = resize_images_with_pillow('assets/images/white pawn.png', pc(52), pc(52))
white_pawn_small = resize_images_with_pillow('assets/images/white pawn.png', pc(36), pc(36))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

black_knight_menu = resize_images_with_pillow('assets/images/white knight.png', pc(443), pc(443))
white_knight_menu = resize_images_with_pillow('assets/images/black knight.png', pc(443), pc(443))

big_white_rook = resize_images_with_pillow('assets/images/white rook.png', pc(400), pc(400))
gear_image = resize_images_with_pillow('assets/images/gear_image.png', pc(128), pc(128))
check_ok_icon = resize_images_with_pillow('assets/images/check ok icon.png', pc(64), pc(64))
red_x_icon = resize_images_with_pillow('assets/images/red x icon.png', pc(64), pc(64))

big_black_bishop_language = resize_images_with_pillow('assets/images/black bishop.png', pc(400), pc(400))
big_white_king = resize_images_with_pillow('assets/images/white king.png', pc(500), pc(500))
big_black_queen = resize_images_with_pillow('assets/images/black queen.png', pc(500), pc(500))
big_white_pawn = resize_images_with_pillow('assets/images/white pawn.png', pc(80), pc(80))
big_black_pawn = resize_images_with_pillow('assets/images/black pawn.png', pc(80), pc(80))

default_image_board_0 = resize_images_with_pillow('assets/images/Image Boards/default_image_board_0.png', pc(225), pc(216))
increased_default_image_board_0 = resize_images_with_pillow('assets/images/Image Boards/default_image_board_0.png', pc(250), pc(240))
image_board_1 = resize_images_with_pillow('assets/images/Image Boards/image_board_1.png', pc(225), pc(216))
increased_image_board_1 = resize_images_with_pillow('assets/images/Image Boards/image_board_1.png', pc(250), pc(240))
image_board_2 = resize_images_with_pillow('assets/images/Image Boards/image_board_2.png', pc(225), pc(216))
increased_image_board_2 = resize_images_with_pillow('assets/images/Image Boards/image_board_2.png', pc(250), pc(240))
image_board_3 = resize_images_with_pillow('assets/images/Image Boards/image_board_3.png', pc(225), pc(216))
increased_image_board_3 = resize_images_with_pillow('assets/images/Image Boards/image_board_3.png', pc(250), pc(240))
image_board_4 = resize_images_with_pillow('assets/images/Image Boards/image_board_4.png', pc(225), pc(216))
increased_image_board_4 = resize_images_with_pillow('assets/images/Image Boards/image_board_4.png', pc(250), pc(240))
image_board_5 = resize_images_with_pillow('assets/images/Image Boards/image_board_5.png', pc(225), pc(216))
increased_image_board_5 = resize_images_with_pillow('assets/images/Image Boards/image_board_5.png', pc(250), pc(240))
image_board_6 = resize_images_with_pillow('assets/images/Image Boards/image_board_6.png', pc(225), pc(216))
increased_image_board_6 = resize_images_with_pillow('assets/images/Image Boards/image_board_6.png', pc(250), pc(225))
image_board_7 = resize_images_with_pillow('assets/images/Image Boards/image_board_7.png', pc(225), pc(216))
increased_image_board_7 = resize_images_with_pillow('assets/images/Image Boards/image_board_7.png', pc(250), pc(225))

check_ok_radio = {"check_ok_1": "True",
                  "check_ok_2": "False",
                  "check_ok_3": "False",
                  "check_ok_4": "False",
                  "check_ok_5": "False",
                  "check_ok_6": "False",
                  "check_ok_7": "False",
                  "check_ok_8": "False"}

# Verifica as variáveis / Contador
# check variables/ flashing counter 
counter = 0
counter_one_player = 0
winner = ''
winner_one_player = ''
game_over = False
game_over_one_player = False
one_time_action = True
one_time_word = True

def play_audio(audio_file, x):
    if audio == True:
        audio_file.set_volume(1)
        audio_file.play()
    
    pygame.time.wait(x)
    
def play_piece_movie_audio():
    n = random.randint(1, 10)
    if n == 1:
        play_audio(movie_piece_song_1, 0)
    elif n == 2:
        play_audio(movie_piece_song_2, 0)
    elif n == 3:
        play_audio(movie_piece_song_3, 0)
    elif n == 4:
        play_audio(movie_piece_song_4, 0)
    elif n == 5:
        play_audio(movie_piece_song_5, 0)
    elif n == 6:
        play_audio(movie_piece_song_6, 8)
    elif n == 7:
        play_audio(movie_piece_song_7, 0)
    elif n == 8:
        play_audio(movie_piece_song_8, 0)
    elif n == 9:
        play_audio(movie_piece_song_9, 0)
    else:
        play_audio(movie_piece_song_10, 0)

def play_captured_movie_audio():
    n = random.randint(1, 4)
    if n == 1:
        play_audio(captured_piece_song_1, 0)
    elif n == 2:
        play_audio(captured_piece_song_2, 0)
    elif n == 3:
        play_audio(captured_piece_song_3, 0)
    else:
        play_audio(captured_piece_song_4, 0)

def draw_rounded_rects(x_position, y_position, rect_width, rect_height):
    radius = pc(5)
    rect = pygame.draw.rect(screen, color_rect_menu, (x_position, y_position, rect_width, rect_height))
    
    pygame.draw.circle(screen, 'black', (rect.left + radius, rect.top + radius), radius)
    pygame.draw.circle(screen, 'black', (rect.right - radius, rect.top + radius), radius)
    pygame.draw.circle(screen, 'black', (rect.left + radius, rect.bottom - radius), radius)
    pygame.draw.circle(screen, 'black', (rect.right - radius, rect.bottom - radius), radius)
        
    # Desenha os retângulos nos lados (bordas arredondadas)
    pygame.draw.rect(screen, 'black', pygame.Rect(rect.left + radius, rect.top, rect.width - pc(2) * radius, radius))  # Topo
    pygame.draw.rect(screen, 'black', pygame.Rect(rect.left + radius, rect.bottom - radius, rect.width - pc(2) * radius, radius))  # Fundo
    pygame.draw.rect(screen, 'black', pygame.Rect(rect.left, rect.top + radius, radius, rect.height - pc(2) * radius))  # Esquerda
    pygame.draw.rect(screen, 'black', pygame.Rect(rect.right - radius, rect.top + radius, radius, rect.height - pc(2) * radius))  # Direita

def print_word_in_the_middle(x_coord, y_coord, width, height, font, word, between_rect, color):
    text_surface = font.render(word, True, color)
    text_width, text_height = text_surface.get_size()
    
    if between_rect == True:
        x_blit = int(width / 2 - text_width / 2) + x_coord
        y_blit = int(height / 2 - text_height / 2) + y_coord
    else:
        x_blit = int(width / 2 - text_width / 2)
        y_blit = y_coord
    
    screen.blit(text_surface, (x_blit, y_blit))

pwm = print_word_in_the_middle
    
def font_size_by_language_for_buttons(default_font_increased, default_font, alternative_font_increased, alternative_font):
    if portuguese or spanish:
        font_language_increased = alternative_font_increased
        font_language = alternative_font
    else:
        font_language_increased = default_font_increased
        font_language = default_font
    
    return font_language_increased, font_language

def get_coord_and_rect(image, x_position, y_position):
    image_rect = image.get_rect()
    image_rect.topleft = (pc(x_position), pc(y_position))
    
    return image_rect

def increase_button(initial_y_position, height_between_buttons, initial_x_position, width_rect, height_rect, font_increased, font, font_increased_alternative, font_alternative, alternative_words, words, color_main, alternative_color, mouse_x, mouse_y):
    
    # Calcula as posições Y para os botões do menu (vai mudar com base em 'i')
    for i, word in enumerate(words):
        # Posição do botão
        y_position = initial_y_position + (height_between_buttons * i)

        # Determinar se o mouse está sobre o botão
        if initial_x_position <= mouse_x <= initial_x_position + width_rect and y_position <= mouse_y <= y_position + height_rect:
            draw_rounded_rects(initial_x_position - 10, pc(y_position - 10), width_rect + 20, height_rect + 20)
            # Determinar a fonte com base na lista `alternative_words`
            font_to_use = font_increased_alternative if word in alternative_words else font_increased
            color_to_use = alternative_color if word in alternative_words else color_main
            pwm(initial_x_position - 10, pc(y_position - 10), width_rect + 20, height_rect + 20, font_to_use, word, True, color_to_use)
        else:
            draw_rounded_rects(initial_x_position, y_position, width_rect, height_rect)
            # Determinar a fonte com base na lista `alternative_words`
            font_to_use = font_alternative if word in alternative_words else font
            color_to_use = alternative_color if word in alternative_words else color_main
            pwm(initial_x_position, y_position, width_rect, height_rect, font_to_use, word, True, color_to_use)

def increase_image(image, increased_image, x_position, y_position, mouse_x, mouse_y):
    # Obter a largura e altura da imagem
    image_rect = get_coord_and_rect(image, x_position, y_position)
    check_ok_icon_rect = get_coord_and_rect(check_ok_icon, x_position, y_position)

    # Verifica se o mouse está sobre a imagem
    if image_rect.collidepoint(mouse_x, mouse_y):
        screen.blit(increased_image, (pc(x_position - 10), pc(y_position - 10)))
    else:
        screen.blit(image, (pc(x_position), pc(y_position)))
    
def change_board(first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces):
    play_audio(sound_button, 200)
    first_color_square = first_color_square
    second_color_square = second_color_square
    color_rect_captured_pieces = color_rect_captured_pieces
    color_bars_captured_pieces = color_bars_captured_pieces
    
    return first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces

def set_radio_button(dicionario, chave_ativa):
    for chave in dicionario:
        if chave == chave_ativa:
            dicionario[chave] = "True"  # Definir como True a chave específica
        else:
            dicionario[chave] = "False"  # Definir como False as outras
            
def language_option(key_translate):
    # Mapeamento dos textos por idioma
    texts = {
        "english": {
            "menu_items": ['PLAY', 'SETTINGS', 'CUSTOM'],
            "settings_items": ['AUDIO', 'LANGUAGE'],
            "title": 'CHESS',
            "settings": 'SETTINGS',
            "language": 'LANGUAGE',
            "turn_step": 'White: Select a Piece to Move!',
            "turn_step_2": 'Black: Select a Piece to Move!',
            "forfeit": 'FORFEIT',
            "white_winner": 'White',
            "black_winner": 'Black',
            "win_message": 'won the game!',
            "restart_message": 'Press ENTER to Restart!',
            "menu_items_continue": ['CONTINUE', 'SETTINGS', 'CUSTOM'],
            "options_buttons": ['MENU', 'FORFEIT', 'UNDO'],
            "undo": 'UNDO',
            "game_mode": ['One Player', 'Two Players'],
            "mode": ['GAME MODE'],
            "black_or_white": ['WHITE', 'BLACK'],
            "white": 'WHITE',
        },
        "portuguese": {
            "menu_items": ['JOGAR', 'AJUSTES', 'CUSTOMIZAR'],
            "settings_items": ['AUDIO', 'IDIOMA'],
            "title": 'XADREZ',
            "settings": 'AJUSTES',
            "language": 'IDIOMA',
            "turn_step": 'Branco: Selecione uma Peça para Mover!',
            "turn_step_2": 'Preto: Selecione uma Peça para Mover!',
            "forfeit": 'DESISTIR',
            "white_winner": 'Branca',
            "black_winner": 'Preta',
            "win_message": 'venceu o jogo!',
            "restart_message": 'Pressione ENTER para reiniciar',
            "menu_items_continue": ['CONTINUAR', 'AJUSTES', 'CUSTOMIZAR'],
            "options_buttons": ['MENU', 'DESISTIR', 'VOLTAR'],
            "undo": 'VOLTAR',
            "game_mode": ['Um Jogador', 'Dois Jogadores'],
            "mode": ['MODO DE JOGO'],
            "black_or_white": ['BRANCAS', 'PRETAS'],
            "white": 'BRANCAS',
        },
        "spanish": {
            "menu_items": ['JUGAR', 'AJUSTES', 'CUSTOMIZAR'],
            "settings_items": ['AUDIO', 'IDIOMA'],
            "title": 'AJEDREZ',
            "settings": 'AJUSTES',
            "language": 'IDIOMA',
            "turn_step": 'Blanco: ¡Selecciona una Pieza para Mover!',
            "turn_step_2": 'Negro: ¡Seleccione una Pieza para Moverla!',
            "forfeit": "DESISTIR",
            "white_winner": '¡Blanca',
            "black_winner": '¡Negra',
            "win_message": 'ganó el partido!',
            "restart_message": 'Pulse ENTER para reiniciar',
            "menu_items_continue": ['CONTINUAR', 'AJUSTES', 'CUSTOMIZAR'],
            "options_buttons": ['MENU', 'DESISTIR', 'VOLVER'],
            "undo": 'VOLVER',
            "game_mode": ['Un Jugador', 'Dos Jugadores'],
            "mode": ['MODO DE JUEGO'],
            "black_or_white": ['BLANCAS', 'NEGRAS'],
            "white": 'BLANCAS',
        },
    }

    # Determinar o idioma ativo
    lang = "english" if english else "portuguese" if portuguese else "spanish"

    # Retornar a tradução diretamente
    return texts[lang].get(key_translate, "Tradução não encontrada")

def font_size_by_language(default_font_size, other_font_size):
    if portuguese or spanish:
        font_language = other_font_size
    else:
        font_language = default_font_size
    
    return font_language

def draw_menu(mouse_x, mouse_y, first_button_word):
    # Desenha o título "CHESS"
    pwm(0, pc(40), WIDTH, 0, font_size_by_language(font_180, font_170), language_option("title"), False, 'black')
    
    # Imprime a imagem da peça do cavalo nas laterais da tela
    screen.blit(pygame.transform.flip(black_knight_menu, True, False), ((pc(-30)), pc(140)))
    screen.blit(white_knight_menu, (pc(940), pc(140)))
    
    # Lista de itens do menu e suas posições X
    
    increase_button(pc(273), pc(125), pc(406), pc(550), pc(80), font_90, font_80, font_80, font_70, 'CUSTOMIZAR', language_option(first_button_word), 'black', 'black', mouse_x, mouse_y)
    
def draw_settings(mouse_x, mouse_y):
    # Desenha a tela de configurações - settings
    pwm(0, pc(40), WIDTH, 0, font_140, language_option("settings"), False, 'black')
    
    increase_button(pc(20), 0, pc(20), pc(240), pc(80), font_70, font_60, 0, 0, (''), [('MENU')], 'black', 'black',mouse_x, mouse_y)     
    
    #big pawn image
    screen.blit(big_white_rook, (pc(-30), pc(200)))
    
    # Gear image
    screen.blit(gear_image, (pc(1050), pc(57)))
    
    increase_button(pc(273), pc(125), pc(406), pc(550), pc(80), font_90, font_80, 0, 0, (''), language_option("settings_items"), 'black', 'black', mouse_x, mouse_y)     
    
    if audio == True:
        screen.blit(check_ok_icon, (pc(976), pc(283)))
    else:
        screen.blit(red_x_icon, (pc(976), pc(283)))
        
def draw_language(mouse_x, mouse_y, english, portuguese):
    pwm(0, pc(40), WIDTH, 0, font_140, language_option("language"), False, 'black')
    increase_button(pc(20), 0, pc(20), pc(240), pc(80), font_50, font_40, 0, 0, (''), [(language_option("settings"))], 'black', 'black', mouse_x, mouse_y)
    increase_button(pc(233), pc(150), pc(406), pc(550), pc(100), font_90, font_80, 0, 0, (''), language_items, 'black', 'black', mouse_x, mouse_y)
    screen.blit(big_black_bishop_language, (pc(-30), pc(200)))
    
    if english == True:
        screen.blit(check_ok_icon, (pc(976), pc(248)))
    elif portuguese == True:
        screen.blit(check_ok_icon, (pc(976), pc(398)))
    else:
        screen.blit(check_ok_icon, (pc(976), pc(548)))

def draw_custom(mouse_x, mouse_y):
    increase_button(pc(20), 0, pc(20), pc(240), pc(80), font_70, font_60, 0, 0, (''), [('MENU')], 'black', 'black', mouse_x, mouse_y)
    
    images = [
    (default_image_board_0, increased_default_image_board_0, pc(40), pc(140)),
    (image_board_1, increased_image_board_1, pc(364), pc(140)),
    (image_board_2, increased_image_board_2, pc(688), pc(140)),
    (image_board_3, increased_image_board_3, pc(1032), pc(140)),
    (image_board_4, increased_image_board_4, pc(40), pc(417)),
    (image_board_5, increased_image_board_5, pc(364), pc(417)),
    (image_board_6, increased_image_board_6, pc(688), pc(417)),
    (image_board_7, increased_image_board_7, pc(1032), pc(417))
    ]
    
    for index, (image, increased_image, x, y) in enumerate(images):
        increase_image(image, increased_image, x, y, mouse_x, mouse_y)
        image_rect = get_coord_and_rect(image, x, y)
        check_ok_icon_rect = get_coord_and_rect(check_ok_icon, x, y)
        middle = ((image_rect.height / 2) + y) - (check_ok_icon_rect.height / 2)
    
        # Verifica qual "check_ok_radio" está ativo e usa o índice para buscar as coordenadas certas
        if check_ok_radio[f"check_ok_{index+1}"] == "True":
            screen.blit(check_ok_icon, (pc(x + 240), pc(middle)))  # Exibe o ícone na posição calculada

def draw_game_mode(mouse_x, mouse_y):
    increase_button(pc(20), 0, pc(20), pc(240), pc(80), font_70, font_60, 0, 0, (''), [('MENU')], 'black', 'black', mouse_x, mouse_y)
    
    increase_button(pc(184), pc(160), pc(403), pc(600), pc(120), font_90, font_80, font_80, font_70, ['Dois Jogadores', 'Dos Jugadores'], language_option('game_mode'), 'black', 'black', mouse_x, mouse_y)
    
    screen.blit(big_white_king, (pc(925), pc(134)))
    screen.blit(big_black_queen, (pc(-50), pc(134)))

def draw_black_or_white(mouse_x, mouse_y):
    increase_button(pc(20), 0, pc(20), pc(360), pc(80), font_45, font_40, 0, 0, '', language_option("mode"), 'black', 'black', mouse_x, mouse_y)
    
    increase_button(pc(184), pc(160), pc(403), pc(600), pc(120), font_90, font_80, font_80, font_70, language_option("white"), language_option("black_or_white"), "black", "white", mouse_x, mouse_y)
    
    screen.blit(big_white_pawn, (pc(1023), pc(204)))
    screen.blit(big_black_pawn, (pc(1023), pc(364)))
    
# Desenha o tabuleiro principal do jogo
# draw main game board
def draw_board(first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces, turn_step_main):
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, first_color_square, [pc(763) - (column * pc(160)), row * pc(80), pc(80), pc(80)])
            pygame.draw.rect(screen, second_color_square, [((pc(763) - (column * pc(160))) + pc(80)), row * pc(80), pc(80), pc(80)])
        else:
            pygame.draw.rect(screen, first_color_square, [pc(843) - (column * pc(160)), row * pc(80), pc(80), pc(80)])
            pygame.draw.rect(screen, second_color_square, [(pc(843) - (column * pc(160)) - pc(80)), row * pc(80), pc(80), pc(80)])
            
        pygame.draw.rect(screen, color_rect_captured_pieces, [pc(283), pc(640), WIDTH - pc(566), pc(67)])
        pygame.draw.rect(screen, color_bars_captured_pieces, [pc(283), pc(640), WIDTH - pc(566), pc(67)], pc(4))
        pygame.draw.rect(screen, color_bars_captured_pieces, [pc(923), 0, pc(160), HEIGHT], pc(7))
        pygame.draw.rect(screen, color_rect_captured_pieces, [pc(927), pc(4), pc(152), HEIGHT - pc(7)])
        
        status_text = [language_option("turn_step"), language_option("turn_step"),
                       language_option("turn_step_2"), language_option("turn_step_2")]
        screen.blit(font_size_by_language(big_font, smaller_font).render(status_text[turn_step_main], True, black_and_white_text(turn_step_main)), (pc(299), pc(653)))

        for i in range(9):
            pygame.draw.line(screen, 'black', (pc(283), pc(80) * i), (pc(923), pc(80) * i), pc(2))
            pygame.draw.line(screen, 'black', (pc(283) + pc(80) * i, 0), (pc(283) + pc(80) * i, pc(640)), pc(2))
        
def draw_options(mouse_x, mouse_y):
    increase_button(pc(20), pc(125), pc(20), pc(240), pc(80), font_70, font_60, font_55, font_45, (language_option('forfeit'), language_option("undo")), language_option("options_buttons"), "black", "black", mouse_x, mouse_y)

# Desenha peças no tabuleiro
# draw pieces onto board
def draw_pieces(white_piece_list_locations, black_piece_list_locations, white_piece_list, black_piece_list, selection_main, turn_step_main):
    for i in range(len(white_piece_list)):
        index = piece_list.index(white_piece_list[i])
        if white_piece_list[i] == "pawn":
            screen.blit(white_pawn, (white_piece_list_locations[i][0] * pc(80) + pc(298), white_piece_list_locations[i][1] * pc(80) + pc(14)))
        else:
            screen.blit(white_images[index], (white_piece_list_locations[i][0] * pc(80) + pc(292), white_piece_list_locations[i][1] * pc(80) + pc(8)))
        if turn_step_main < 2:
            if selection_main == i:
                pygame.draw.rect(screen, 'red', [white_piece_list_locations[i][0] * pc(80) + pc(284), white_piece_list_locations[i][1] * pc(80) + pc(1),
                                                 pc(80), pc(80)], pc(2))
                
    for i in range(len(black_piece_list)):
        index = piece_list.index(black_piece_list[i])
        if black_piece_list[i] == 'pawn':
            screen.blit(black_pawn, (black_piece_list_locations[i][0] * pc(80) + pc(298), black_piece_list_locations[i][1] * pc(80) + pc(18)))
        else:
            screen.blit(black_images[index], (black_piece_list_locations[i][0] * pc(80) + pc(292), black_piece_list_locations[i][1] * pc(80) + pc(8)))
        if turn_step_main >= 2:
            if selection_main == i:
                pygame.draw.rect(screen, 'blue', [black_piece_list_locations[i][0] * pc(80) + pc(283), black_piece_list_locations[i][1] * pc(80) + pc(1),
                                                 pc(80), pc(80)], pc(1))

# Função para verificar de todas as opções válidas de peças no tabuleiro
# function to check all pieces valid options on board
def check_options(pieces, locations, turn, white_piece_list_locations, black_piece_list_locations):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn, white_piece_list_locations, black_piece_list_locations)
        elif piece == 'rook':
            moves_list = check_rook(location, turn, white_piece_list_locations, black_piece_list_locations)
        elif piece == 'knight':
            moves_list = check_knight(location, turn, white_piece_list_locations, black_piece_list_locations)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn, white_piece_list_locations, black_piece_list_locations)
        elif piece == 'queen':
            moves_list = check_queen(location, turn, white_piece_list_locations, black_piece_list_locations)
        elif piece == 'king':
            moves_list = check_king(location, turn, white_piece_list_locations, black_piece_list_locations)
        all_moves_list.append(moves_list)
    return all_moves_list

# Verifica os movimentos válidos do rei
# check king valid moves
def check_king(position, color, white_piece_list_locations, black_piece_list_locations):
    moves_list = []
    if color == 'white':
        enemies_list = black_piece_list_locations
        friends_list = white_piece_list_locations
    else:
        friends_list = black_piece_list_locations
        enemies_list = white_piece_list_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Verifica os movimentos válidos da rainha
# check queen valid moves
def check_queen(position, color, white_piece_list_locations, black_piece_list_locations):
    moves_list = check_bishop(position, color, white_piece_list_locations, black_piece_list_locations)
    second_list = check_rook(position, color, white_piece_list_locations, black_piece_list_locations)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

# Verifica os movimentos válidos do bispo
# check bishop moves
def check_bishop(position, color, white_piece_list_locations, black_piece_list_locations):
    moves_list = []
    if color == 'white':
        enemies_list = black_piece_list_locations
        friends_list = white_piece_list_locations
    else:
        friends_list = black_piece_list_locations
        enemies_list = white_piece_list_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# Verifica os movimentos válidos da torre
# check rook moves
def check_rook(position, color, white_piece_list_locations, black_piece_list_locations):
    moves_list = []
    if color == 'white':
        enemies_list = black_piece_list_locations
        friends_list = white_piece_list_locations
    else:
        friends_list = black_piece_list_locations
        enemies_list = white_piece_list_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# Verifica os movimentos válidos do peão
# check valid pawn moves
def check_pawn(position, color, white_piece_list_locations, black_piece_list_locations):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_piece_list_locations and \
                (position[0], position[1] + 1) not in black_piece_list_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_piece_list_locations and \
                (position[0], position[1] + 2) not in black_piece_list_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_piece_list_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_piece_list_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_piece_list_locations and \
                (position[0], position[1] - 1) not in black_piece_list_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_piece_list_locations and \
                (position[0], position[1] - 2) not in black_piece_list_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_piece_list_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_piece_list_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# Verifica os movimentos válidos do cavalo
# check valid knight moves
def check_knight(position, color, white_piece_list_locations, black_piece_list_locations):
    moves_list = []
    if color == 'white':
        enemies_list = black_piece_list_locations
        friends_list = white_piece_list_locations
    else:
        friends_list = black_piece_list_locations
        enemies_list = white_piece_list_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Verifica os movimentos válidos apenas para a peça selecionada
# check for valid moves for just selected piece
def check_valid_moves(white_options_main, black_options_main, turn_step_main, selection_main):
    if turn_step_main < 2:
        options_list = white_options_main
    else:
        options_list = black_options_main
    valid_options = options_list[selection_main]
    return valid_options

# Desenha os movimentos válidos apenas na tela
# draw valid moves on screen
def draw_valid(moves, turn_step_main):
    if turn_step_main < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * pc(80) + pc(323), moves[i][1] * pc(80) + pc(40)), pc(4))

# Desenha as peças capturadas no lado direiro da tela
# draw captured pieces on side of screen
def draw_captured(captured_pieces_white_main, captured_pieces_black_main):
    for i in range(len(captured_pieces_white_main)):
        captured_piece = captured_pieces_white_main[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (pc(943), pc(4) + pc(40) * i))
    for i in range(len(captured_pieces_black_main)):
        captured_piece = captured_pieces_black_main[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (pc(1023), pc(4) + pc(40) * i))

# Desenha um quadrado vermelho ao redor do rei se ele estiver em cheque
# draw a flashing square around king if in check
def draw_check(white_piece_list_locations, black_piece_list_locations, white_piece_list, black_piece_list, counter_main, turn_step_main, white_options_main, black_options_main):
    if turn_step_main < 2:
        if 'king' in white_piece_list:
            king_index = white_piece_list.index('king')
            king_location = white_piece_list_locations[king_index]
            for i in range(len(black_options_main)):
                if king_location in black_options_main[i]:
                    if counter_main < 15:
                        pygame.draw.rect(screen, 'dark red', [white_piece_list_locations[king_index][0] * pc(80) + pc(283),
                                                              white_piece_list_locations[king_index][1] * pc(80) + pc(1), pc(80), pc(80)], pc(4))
    else:
        if 'king' in black_piece_list:
            king_index = black_piece_list.index('king')
            king_location = black_piece_list_locations[king_index]
            for i in range(len(white_options_main)):
                if king_location in white_options_main[i]:
                    if counter_main < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_piece_list_locations[king_index][0] * pc(80) + pc(283),
                                                               black_piece_list_locations[king_index][1] * pc(80) + pc(1), pc(80), pc(80)], pc(4))

def black_and_white_text(turn_step_main):
    if turn_step_main <= 1:
        color_text = 'white'
    else:
        color_text = 'black'
    return color_text

# Desenha o texto de game over
# Draw the game over text
def draw_game_over(winner_main):
    pygame.draw.rect(screen, 'black', [pc(443), pc(290), pc(320), pc(56)])
    screen.blit(font.render(f'{winner_main} {language_option("win_message")}', True, 'white'), (pc(451), pc(298)))
    screen.blit(font.render(language_option("restart_message"), True, 'white'), (pc(451), pc(322)))

def one_time_action_(action):
    global one_time_action
    
    while True:
        if one_time_action == True:
            action()
        one_time_action = False
        break

# Loop principal do jogo
# main game loop

def menu_screen_run(screen):
    global one_time_word
    while True:
        timer.tick(fps)
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if one_time_word == True:
            first_button_word = "menu_items"
        else:
            first_button_word = "menu_items_continue"
        draw_menu(mouse_x, mouse_y, first_button_word)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Garantir que o programa termine ao sair da tela do menu
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(273) and event.pos[1] <= pc(353):
                    play_audio(sound_button, 200)
                    scene = "scene_game_mode" # Sai do menu e entra no jogo principal
                    one_time_word = False
                    return scene
                elif event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(398) and event.pos[1] <= pc(478):
                    play_audio(sound_button, 200)
                    scene = "scene_settings"
                    return scene
                elif event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(523) and event.pos[1] <= pc(603):
                    play_audio(sound_button, 0)
                    scene = "scene_custom"
                    return scene  
        
        pygame.display.flip()
        
def settings_screen_run(screen):
    global audio, music
    while True:
        timer.tick(fps)
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_settings(mouse_x, mouse_y)     

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(273) and event.pos[1] <= pc(353):
                    play_audio(sound_button, 200)
                    audio = not audio
                elif event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(398) and event.pos[1] <= pc(478):
                    play_audio(sound_button, 200)
                    scene = 'scene_language'
                    return scene
                elif event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_menu"
                    return scene
    
        pygame.display.flip()

def language_screen_run(screen):
    global english, portuguese, spanish
    while True:
        timer.tick(fps)
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_language(mouse_x, mouse_y, english, portuguese)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_settings"
                    return scene
                elif event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(233) and event.pos[1] <= pc(333):
                    english = True
                    portuguese = False
                    spanish = False
                elif event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(383) and event.pos[1] <= pc(483):
                    english = False
                    portuguese = True
                    spanish = False
                elif event.pos[0] >= pc(406) and event.pos[0] <= pc(956) and event.pos[1] >= pc(533) and event.pos[1] <= pc(633):
                    english = False
                    portuguese = False
                    spanish = True
        
        pygame.display.flip()

def custom_screen_run(screen, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces):
    # Lista de regiões de clique com as respectivas configurações
    regions = [
        ((pc(40), pc(265), pc(140), pc(356)), (205,133,63), (240, 217, 181), (181, 136, 99), 'gold'),
        ((pc(364), pc(589), pc(140), pc(356)), (118, 150, 86), (238, 238, 210), (181, 136, 99), 'gold'),
        ((pc(688), pc(913), pc(140), pc(356)), (123,158,178), (211, 223, 228), (199, 193, 172), (139,69,19)),
        ((pc(1032), pc(1257), pc(140), pc(356)), (255,182,193), (255, 255, 255), (199, 193, 172), (139,69,19)),
        ((pc(40), pc(265), pc(417), pc(733)), (255,255,51), (255, 255, 204), (240, 230, 140), 'orange'),
        ((pc(364), pc(589), pc(417), pc(733)), (178,34,34), (255, 192, 146), (240, 230, 140), 'orange'),
        ((pc(688), pc(913), pc(417), pc(733)), (108,104,98), (199, 194, 172), (122,133,147), (128,0,0)),
        ((pc(1032), pc(1257), pc(417), pc(733)), (51,104,75), (236, 235, 232), (122,133,147), (128,0,0)),
        ]
    
    while True:
        timer.tick(fps)
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_custom(mouse_x, mouse_y)
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Iterando sobre as regiões e verificando o clique
                for index, ((x1, x2, y1, y2), color1, color2, color3, color4) in enumerate(regions):
                    if x1 <= event.pos[0] <= x2 and y1 <= event.pos[1] <= y2:
                        first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces = change_board(color1, color2, color3, color4)
                        set_radio_button(check_ok_radio, f"check_ok_{index+1}")
                        break  # Sai do loop após encontrar a região clicada
       
                if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_menu"
                    return scene, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces
        
        pygame.display.flip()

def game_mode_screen_run(screen):
    while True:
        timer.tick(fps)
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_game_mode(mouse_x, mouse_y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
                if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_menu"
                    return scene
                elif pc(403) <= event.pos[0] <= pc(1003) and pc(184) <= event.pos[1] <= pc(304):
                    play_audio(sound_button, 200)
                    scene = "scene_black_or_white"
                    return scene
                elif pc(403) <= event.pos[0] <= pc(1003) and pc(344) <= event.pos[1] <= pc(464):
                    play_audio(sound_button, 200)
                    scene = "scene_game"
                    return scene
        
        pygame.display.flip()
         
def choose_black_or_white_screen_run(screen):
    global white_piece_ai, black_piece_ai
    while True:
        timer.tick(fps)
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_black_or_white(mouse_x, mouse_y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
                if event.pos[0] >= pc(20) and event.pos[0] <= pc(380) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_game_mode"
                    black_piece_ai = False
                    white_piece_ai = False
                    return scene, white_piece_ai, black_piece_ai
                elif pc(403) <= event.pos[0] <= pc(1003) and pc(184) <= event.pos[1] <= pc(304):
                    play_audio(sound_button, 200)
                    black_piece_ai = True
                    white_piece_ai = False
                    scene = "scene_game_one_player"
                    return scene, black_piece_ai, white_piece_ai
                elif pc(403) <= event.pos[0] <= pc(1003) and pc(344) <= event.pos[1] <= pc(464):
                    play_audio(sound_button, 200)
                    white_piece_ai = True
                    black_piece_ai = False
                    scene = "scene_game_one_player"
                    return scene, white_piece_ai, black_piece_ai
                
        pygame.display.flip()

black_options = check_options(black_pieces, black_locations, 'black', white_locations, black_locations) 
white_options = check_options(white_pieces, white_locations, 'white', white_locations, black_locations)

def main_screen_run(screen, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces):
    global black_options, white_options, counter, winner, game_over, selection, turn_step
    global valid_moves, white_locations, black_locations, black_pieces, white_pieces, captured_pieces_black, captured_pieces_white, prior_white_locations, prior_black_locations, no_undo, prior_captured_white_pieces, prior_captured_black_pieces, save_prior_captured_piece, last_captured_piece_black, last_captured_piece_white
    
    while True:
        
        timer.tick(fps)
        if counter < 30:
            counter += 1
        else:
            counter = 0
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_board(first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces, turn_step)
        draw_pieces(white_locations, black_locations, white_pieces, black_pieces, selection, turn_step)
        draw_captured(captured_pieces_white, captured_pieces_black)
        draw_check(white_locations, black_locations, white_pieces, black_pieces, counter, turn_step, white_options, black_options)
        draw_options(mouse_x, mouse_y)
        if selection != 100:
            valid_moves = check_valid_moves(white_options, black_options, turn_step, selection)
            draw_valid(valid_moves, turn_step)
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_game_mode"
                    return scene
                elif event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(270) and event.pos[1] <= pc(350) and not game_over:
                        play_audio(sound_button, 200)
                        if no_undo == True:
                            if turn_step <= 1:  # Se for o turno do branco
                                turn_step = 2  # Passa para o turno do preto
                                black_locations = prior_black_locations
                                black_pieces = prior_black_pieces
                                 # Restaurar peça capturada
                                if save_prior_captured_piece == True:
                                    captured_pieces_black = prior_captured_black_pieces.copy()
                                    if last_captured_piece_white:
                                        piece, position = last_captured_piece_white
                                        white_pieces.append(piece)
                                        white_locations.append(position)
                                black_options = check_options(black_pieces, black_locations, 'black', white_locations, black_locations) 
                                white_options = check_options(white_pieces, white_locations, 'white', white_locations, black_locations)
                            elif turn_step > 1:  # Se for o turno do preto
                                turn_step = 0  # Passa para o turno do branco
                                white_locations = prior_white_locations
                                white_pieces = prior_white_pieces
                                if save_prior_captured_piece == True:
                                    captured_pieces_white = prior_captured_white_pieces.copy()
                                     # Restaurar peça capturada
                                    if last_captured_piece_black:
                                        piece, position = last_captured_piece_black
                                        black_pieces.append(piece)
                                        black_locations.append(position)
                                white_options = check_options(white_pieces, white_locations, 'white', white_locations, black_locations)
                                black_options = check_options(black_pieces, black_locations, 'black', white_locations, black_locations) 
                            no_undo = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                x_coord = (event.pos[0] - pc(283)) // pc(80) 
                y_coord = event.pos[1] // pc(80)
                click_coords = (x_coord, y_coord)
                if turn_step <= 1:
                    # Copiar a localização das peças antes de mudar
                    prior_white_locations = white_locations.copy()
                    prior_white_pieces = white_pieces.copy()
                    if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(145) and event.pos[1] <= pc(225):
                        play_audio(win_game_song, 0)
                        winner = language_option("black_winner")
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        play_piece_movie_audio()

                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            play_captured_movie_audio()
                            prior_captured_white_pieces = captured_pieces_white.copy()
                            black_piece = black_locations.index(click_coords)
                            last_captured_piece_black = (black_pieces[black_piece], black_locations[black_piece])  # Salvar peça e posição
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                play_audio(win_game_song, 0)
                                winner = language_option("white_winner")
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                            save_prior_captured_piece = True
                        black_options = check_options(black_pieces, black_locations, 'black', white_locations, black_locations) 
                        white_options = check_options(white_pieces, white_locations, 'white', white_locations, black_locations)
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                        no_undo = True
                if turn_step > 1:
                    prior_black_locations = black_locations.copy()
                    prior_black_pieces = black_pieces.copy()
                    if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(145) and event.pos[1] <= pc(225):
                        play_audio(win_game_song, 0)
                        winner = language_option("white_winner")
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        play_piece_movie_audio()
                        
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            play_captured_movie_audio()
                            prior_captured_black_pieces = captured_pieces_black.copy()
                            white_piece = white_locations.index(click_coords)
                            last_captured_piece_white = (white_pieces[white_piece], white_locations[white_piece])  # Salvar peça e posição
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                play_audio(win_game_song, 0)
                                winner = language_option("black_winner")
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                            save_prior_captured_piece = True
                        black_options = check_options(black_pieces, black_locations, 'black', white_locations, black_locations) 
                        white_options = check_options(white_pieces, white_locations, 'white', white_locations, black_locations)
                        turn_step = 0
                        selection = 100
                        valid_moves = []
                        no_undo = True
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    winner = ''
                    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    prior_white_pieces = white_pieces
                    prior_white_locations = white_locations
                    prior_black_pieces = black_pieces
                    prior_black_locations = black_locations
                    
                    captured_pieces_white = []
                    captured_pieces_black = []
                    prior_captured_white_pieces = []
                    prior_captured_black_pieces = []
                    
                    last_captured_piece_white = None
                    last_captured_piece_black = None
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    black_options = check_options(black_pieces, black_locations, 'black', white_locations, black_locations) 
                    white_options = check_options(white_pieces, white_locations, 'white', white_locations, black_locations)
                    no_undo = False
                    play_audio(start_game_song, 0)

        if winner != '':
            game_over = True
            draw_game_over(winner)

        one_time_action_(lambda: play_audio(start_game_song, 0))
        pygame.display.flip()
        
def main_screen_run_one_player(screen, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces):
    global black_options_one_player, white_options_one_player, counter_one_player, winner_one_player, game_over_one_player, selection_one_player, turn_step_one_player
    global valid_moves_one_player, white_locations_one_player, black_locations_one_player, black_pieces_one_player, white_pieces_one_player, captured_pieces_black_one_player, captured_pieces_white_one_player, prior_white_locations_one_player, prior_black_locations_one_player, no_undo_one_player, prior_captured_white_pieces_one_player, prior_captured_black_pieces_one_player, save_prior_captured_piece_one_player, last_captured_piece_black_one_player, last_captured_piece_white_one_player, white_piece_ai, black_piece_ai
    
    count = 0
    while True:
        count += 1
        
        black_options_one_player = check_options(black_pieces_one_player, black_locations_one_player, 'black', white_locations_one_player, black_locations_one_player)
        white_options_one_player = check_options(white_pieces_one_player, white_locations_one_player, 'white', white_locations_one_player, black_locations_one_player)
        
        timer.tick(fps)
        if counter_one_player < 30:
            counter_one_player += 1
        else:
            counter_one_player = 0
        screen.fill(color_menu)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_board(first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces, turn_step_one_player)
        draw_pieces(white_locations_one_player, black_locations_one_player, white_pieces_one_player, black_pieces_one_player, selection_one_player, turn_step_one_player)
        draw_captured(captured_pieces_white_one_player, captured_pieces_black_one_player)
        draw_check(white_locations_one_player, black_locations_one_player, white_pieces_one_player, black_pieces_one_player, counter_one_player, turn_step_one_player, white_options_one_player, black_options_one_player)
        draw_options(mouse_x, mouse_y)
        if selection_one_player != 100:
            valid_moves_one_player = check_valid_moves(white_options_one_player, black_options_one_player, turn_step_one_player, selection_one_player)
            draw_valid(valid_moves_one_player, turn_step_one_player)
        
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(20) and event.pos[1] <= pc(100):
                    play_audio(sound_button, 200)
                    scene = "scene_game_mode"
                    return scene
                elif event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(270) and event.pos[1] <= pc(350) and not game_over_one_player:
                        play_audio(sound_button, 200)
                        if no_undo_one_player == True:
                                white_locations_one_player = prior_white_locations_one_player
                                white_pieces_one_player = prior_white_pieces
                                black_locations_one_player = prior_black_locations_one_player
                                black_pieces_one_player = prior_black_pieces
                                
                                if save_prior_captured_piece_one_player == True:
                                    captured_pieces_white_one_player = prior_captured_white_pieces_one_player.copy()
                                    captured_pieces_black_one_player = prior_captured_black_pieces_one_player.copy()
                                     # Restaurar peça capturada
                                    if last_captured_piece_black_one_player:
                                        piece, position = last_captured_piece_black_one_player
                                        black_pieces_one_player.append(piece)
                                        black_locations_one_player.append(position)
                                    
                                    if last_captured_piece_white_one_player:
                                        piece, position = last_captured_piece_white_one_player
                                        white_pieces_one_player.append(piece)
                                        white_locations_one_player.append(position)
                                white_options_one_player = check_options(white_pieces_one_player, white_locations_one_player, 'white', white_locations_one_player, black_locations_one_player)
                                black_options_one_player = check_options(black_pieces_one_player, black_locations_one_player, 'black', white_locations_one_player, black_locations_one_player)
                                no_undo_one_player = False
            if not game_over_one_player and count >= 3:
                if white_piece_ai and turn_step_one_player == 0:
                    prior_white_locations_one_player = white_locations_one_player.copy()
                    prior_white_pieces = white_pieces_one_player.copy()
                    # Filtrando as posições válidas diretamente
                    possible_locations_to_play = [pos for pos in white_options_one_player if pos]

                    # Seleção aleatória de peça e movimento
                    random_piece = random.choice(possible_locations_to_play)
                    random_move = random.choice(random_piece)

                    # Atualizando a posição da peça
                    index_piece = white_options_one_player.index(random_piece)
                    time.sleep(0.5)
                    white_locations_one_player[index_piece] = random_move
                    play_piece_movie_audio()

                    # Verificando captura de peça
                    if random_move in black_locations_one_player:
                        play_captured_movie_audio()
                        prior_captured_white_pieces_one_player = captured_pieces_white_one_player.copy()
                        black_piece = black_locations_one_player.index(random_move)
                        last_captured_piece_black_one_player = (black_pieces_one_player[black_piece], black_locations_one_player[black_piece])
                        
                        captured_pieces_white_one_player.append(black_pieces_one_player[black_piece])
                        if black_pieces_one_player[black_piece] == 'king':
                            play_audio(win_game_song, 0)
                            winner_one_player = language_option("white_winner")
                        black_pieces_one_player.pop(black_piece)
                        black_locations_one_player.pop(black_piece)
                        save_prior_captured_piece_one_player = True

                    # Avançando para o próximo turno
                    turn_step_one_player = 2
                    continue
                
                if black_piece_ai == True and turn_step_one_player == 2:
                    prior_black_locations_one_player = black_locations_one_player.copy()
                    prior_black_pieces = black_pieces_one_player.copy()
                    # Filtrando as posições válidas diretamente
                    possible_locations_to_play = [pos for pos in black_options_one_player if pos]

                    # Seleção aleatória de peça e movimento
                    random_piece = random.choice(possible_locations_to_play)
                    random_move = random.choice(random_piece)

                    # Atualizando a posição da peça
                    index_piece = black_options_one_player.index(random_piece)
                    time.sleep(0.5)
                    black_locations_one_player[index_piece] = random_move
                    play_piece_movie_audio()

                    # Verificando captura de peça
                    if random_move in white_locations_one_player:
                        play_captured_movie_audio()
                        prior_captured_black_pieces_one_player = captured_pieces_black_one_player.copy()
                        white_piece = white_locations_one_player.index(random_move)
                        last_captured_piece_white_one_player = (white_pieces_one_player[white_piece], white_locations_one_player[white_piece])
                        
                        captured_pieces_black_one_player.append(white_pieces_one_player[white_piece])
                        if white_pieces_one_player[white_piece] == 'king':
                            play_audio(win_game_song, 0)
                            winner_one_player = language_option("black_winner")
                        white_pieces_one_player.pop(white_piece)
                        white_locations_one_player.pop(white_piece)
                        save_prior_captured_piece_one_player = True
                    
                    turn_step_one_player = 0    
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x_coord = (event.pos[0] - pc(283)) // pc(80) 
                    y_coord = event.pos[1] // pc(80)
                    click_coords = (x_coord, y_coord)
                        
                    if turn_step_one_player <= 1:
                        # Copiar a localização das peças antes de mudar
                        prior_white_locations_one_player = white_locations_one_player.copy()
                        prior_white_pieces = white_pieces_one_player.copy()
                        if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(145) and event.pos[1] <= pc(225):
                            play_audio(win_game_song, 0)
                            winner_one_player = language_option("black_winner")
                        if click_coords in white_locations_one_player:
                            selection_one_player = white_locations_one_player.index(click_coords)
                            if turn_step_one_player == 0:
                                turn_step_one_player = 1
                        if click_coords in valid_moves_one_player and selection_one_player != 100:
                            play_piece_movie_audio()
                            white_locations_one_player[selection_one_player] = click_coords
                            if click_coords in black_locations_one_player:
                                play_captured_movie_audio()
                                prior_captured_white_pieces_one_player = captured_pieces_white_one_player.copy()
                                black_piece = black_locations_one_player.index(click_coords)
                                last_captured_piece_black_one_player = (black_pieces_one_player[black_piece], black_locations_one_player[black_piece])  # Salvar peça e posição
                                captured_pieces_white_one_player.append(black_pieces_one_player[black_piece])
                                if black_pieces_one_player[black_piece] == 'king':
                                    play_audio(win_game_song, 0)
                                    winner_one_player = language_option("white_winner")
                                black_pieces_one_player.pop(black_piece)
                                black_locations_one_player.pop(black_piece)
                                save_prior_captured_piece_one_player = True
                            black_options_one_player = check_options(black_pieces_one_player, black_locations_one_player, 'black', white_locations_one_player, black_locations_one_player)
                            white_options_one_player = check_options(white_pieces_one_player, white_locations_one_player, 'white', white_locations_one_player, black_locations_one_player)
                            turn_step_one_player = 2
                            selection_one_player = 100
                            valid_moves_one_player = []
                            no_undo_one_player = True
    
                    if turn_step_one_player > 1 and count >= 3:
                        prior_black_locations_one_player = black_locations_one_player.copy()
                        prior_black_pieces = black_pieces_one_player.copy()
                        if event.pos[0] >= pc(20) and event.pos[0] <= pc(260) and event.pos[1] >= pc(145) and event.pos[1] <= pc(225):
                            play_audio(win_game_song, 0)
                            winner_one_player = language_option("white_winner")
                        if click_coords in black_locations_one_player:
                            selection_one_player = black_locations_one_player.index(click_coords)
                            if turn_step_one_player == 2:
                                turn_step_one_player = 3
                        if click_coords in valid_moves_one_player and selection_one_player != 100:
                            play_piece_movie_audio()
                            black_locations_one_player[selection_one_player] = click_coords
                            if click_coords in white_locations_one_player:
                                play_captured_movie_audio()
                                prior_captured_black_pieces_one_player = captured_pieces_black_one_player.copy()
                                white_piece = white_locations_one_player.index(click_coords)
                                last_captured_piece_white_one_player = (white_pieces_one_player[white_piece], white_locations_one_player[white_piece])  # Salvar peça e posição
                                captured_pieces_black_one_player.append(white_pieces_one_player[white_piece])
                                if white_pieces_one_player[white_piece] == 'king':
                                    play_audio(win_game_song, 0)
                                    winner_one_player = language_option("black_winner")
                                white_pieces_one_player.pop(white_piece)
                                white_locations_one_player.pop(white_piece)
                                save_prior_captured_piece_one_player = True
                            black_options_one_player = check_options(black_pieces_one_player, black_locations_one_player, 'black', white_locations_one_player, black_locations_one_player)
                            white_options_one_player = check_options(white_pieces_one_player, white_locations_one_player, 'white', white_locations_one_player, black_locations_one_player)
                            turn_step_one_player = 0
                            selection_one_player = 100
                            valid_moves_one_player = []
                            no_undo_one_player = True
            if event.type == pygame.KEYDOWN and game_over_one_player:
                if event.key == pygame.K_RETURN:
                    game_over_one_player = False
                    winner_one_player = ''
                    white_pieces_one_player = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    white_locations_one_player = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    black_pieces_one_player = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                    black_locations_one_player = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    prior_white_pieces = white_pieces_one_player
                    prior_white_locations_one_player = white_locations_one_player
                    prior_black_pieces = black_pieces_one_player
                    prior_black_locations_one_player = black_locations_one_player
                    
                    captured_pieces_white_one_player = []
                    captured_pieces_black_one_player = []
                    prior_captured_white_pieces_one_player = []
                    prior_captured_black_pieces_one_player = []
                    
                    last_captured_piece_white_one_player = None
                    last_captured_piece_black_one_player = None
                    turn_step_one_player = 0
                    selection_one_player = 100
                    valid_moves_one_player = []
                    black_options_one_player = check_options(black_pieces_one_player, black_locations_one_player, 'black', white_locations_one_player, black_locations_one_player)
                    white_options_one_player = check_options(white_pieces_one_player, white_locations_one_player, 'white', white_locations_one_player, black_locations_one_player)
                    no_undo_one_player = False
                    play_audio(start_game_song, 0)

        if winner_one_player != '':
            game_over_one_player = True
            draw_game_over(winner_one_player)

        one_time_action_(lambda: play_audio(start_game_song, 0))
        pygame.display.flip()

def main(first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces):
    global white_piece_ai, black_piece_ai
    scene = "scene_menu"
    while True:
        if scene == "scene_menu":
            scene = menu_screen_run(screen)
        elif scene == "scene_game":
            scene = main_screen_run(screen, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces)
        elif scene == "scene_game_one_player":
            scene  = main_screen_run_one_player(screen, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces)
        elif scene == "scene_settings":
            scene = settings_screen_run(screen)
        elif scene == "scene_language":
            scene = language_screen_run(screen)
        elif scene == "scene_custom":
            scene, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces = custom_screen_run(screen, first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces)
        elif scene == "scene_game_mode":
            scene = game_mode_screen_run(screen)
        elif scene == "scene_black_or_white":
            scene, white_piece_ai, black_piece_ai = choose_black_or_white_screen_run(screen)
            
if __name__ == "__main__":
    main(first_color_square, second_color_square, color_rect_captured_pieces, color_bars_captured_pieces)

pygame.quit()
sys.exit()