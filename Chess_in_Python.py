# Um jogo de Xadrez para dois jogadores desenvolvido em Python através da biblioteca Pygame

# Primeira parte do Código: Declaração das Funções e Variáveis

import pygame
import sys

pygame.init()

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
screen_menu = pygame.display.set_mode([WIDTH, HEIGHT])

color_menu = (206, 162, 119)
color_rect_menu = (205,133,63)

pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('assets/images/white pawn.png'))
font = pygame.font.Font('freesansbold.ttf', pc(16))
medium_font = pygame.font.Font('freesansbold.ttf', pc(32))
big_font = pygame.font.Font('freesansbold.ttf', pc(40))

font_menu = pygame.font.SysFont('Georgia', pc(180))
font_menu_options = pygame.font.SysFont('Georgia', pc(80))

timer = pygame.time.Clock()
fps = 60

# Variáveis do jogo, imagens e seus tamanhos
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []

# Carrega as peças do jogo (rainha, rei, torre, bispo, cavalo, peão) x 2
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (pc(64), pc(64)))
black_queen_small = pygame.transform.scale(black_queen, (pc(36), pc(36)))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (pc(64), pc(64)))
black_king_small = pygame.transform.scale(black_king, (pc(36), pc(36)))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (pc(64), pc(64)))
black_rook_small = pygame.transform.scale(black_rook, (pc(36), pc(36)))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (pc(64), pc(64)))
black_bishop_small = pygame.transform.scale(black_bishop, (pc(36), pc(36)))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (pc(64), pc(64)))
black_knight_small = pygame.transform.scale(black_knight, (pc(36), pc(36)))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (pc(52), pc(52)))
black_pawn_small = pygame.transform.scale(black_pawn, (pc(36), pc(36)))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (pc(64), pc(64)))
white_queen_small = pygame.transform.scale(white_queen, (pc(36), pc(36)))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (pc(64), pc(64)))
white_king_small = pygame.transform.scale(white_king, (pc(36), pc(36)))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (pc(64), pc(64)))
white_rook_small = pygame.transform.scale(white_rook, (pc(36), pc(36)))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (pc(64), pc(64)))
white_bishop_small = pygame.transform.scale(white_bishop, (pc(36), pc(36)))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (pc(64), pc(64)))
white_knight_small = pygame.transform.scale(white_knight, (pc(36), pc(36)))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (pc(52), pc(52)))
white_pawn_small = pygame.transform.scale(white_pawn, (pc(36), pc(36)))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# Imagens das peças no menu
white_knight_menu = pygame.transform.scale(white_knight, (pc(290), pc(290)))
flipped_white_knight_menu = pygame.transform.flip(white_knight_menu, True, False) # Gira a imagem horizontalmente

# Verifica as variáveis / Contador
# check variables/ flashing counter 
counter = 0
winner = ''
game_over = False

def draw_menu():
    # Desenha o título "CHESS"
    screen_menu.blit(font_menu.render('CHESS', True, 'black'), (pc(395), pc(40)))
    
    # Imprime a imagem da peça do cavalo nas laterais da tela
    screen_menu.blit(white_knight_menu, (pc(50), pc(40)))
    
    # Lista de itens do menu e suas posições X
    menu_items = [('START', pc(560)), ('SETTINGS', pc(490)), ('CUSTOM', pc(517))]
    
    # Define o valor fixo para o raio do círculo
    radius = pc(5)
    
    # Calcula as posições Y para os botões do menu (vai mudar com base em 'i')
    for i, (word, x) in enumerate(menu_items):
        # Posição do botão
        y_position = pc(273) + (pc(125) * i)
        
        # Desenha o retângulo do botão
        rect = pygame.draw.rect(screen_menu, color_rect_menu, (pc(406), y_position, pc(550), pc(80)))
        
        # Desenha os círculos nos cantos do retângulo
        pygame.draw.circle(screen_menu, 'black', (rect.left + radius, rect.top + radius), radius)
        pygame.draw.circle(screen_menu, 'black', (rect.right - radius, rect.top + radius), radius)
        pygame.draw.circle(screen_menu, 'black', (rect.left + radius, rect.bottom - radius), radius)
        pygame.draw.circle(screen_menu, 'black', (rect.right - radius, rect.bottom - radius), radius)
        
        # Desenha os retângulos nos lados (bordas arredondadas)
        pygame.draw.rect(screen_menu, 'black', pygame.Rect(rect.left + radius, rect.top, rect.width - pc(2) * radius, radius))  # Topo
        pygame.draw.rect(screen_menu, 'black', pygame.Rect(rect.left + radius, rect.bottom - radius, rect.width - pc(2) * radius, radius))  # Fundo
        pygame.draw.rect(screen_menu, 'black', pygame.Rect(rect.left, rect.top + radius, radius, rect.height - pc(2) * radius))  # Esquerda
        pygame.draw.rect(screen_menu, 'black', pygame.Rect(rect.right - radius, rect.top + radius, radius, rect.height - pc(2) * radius))  # Direita
        
        # Desenha o texto no botão
        screen_menu.blit(font_menu_options.render(word, True, 'black'), (x, y_position - pc(7)))

# Desenha o tabuleiro principal do jogo
# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [pc(763) - (column * pc(160)), row * pc(80), pc(80), pc(80)])
        else:
            pygame.draw.rect(screen, 'light gray', [pc(843) - (column * pc(160)), row * pc(80), pc(80), pc(80)])
        pygame.draw.rect(screen, 'gray', [pc(283), pc(640), WIDTH - pc(566), pc(80)])
        pygame.draw.rect(screen, 'gold', [pc(283), pc(640), WIDTH - pc(566), pc(80)], pc(4))
        pygame.draw.rect(screen, 'gold', [pc(923), 0, pc(160), HEIGHT], pc(4))
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (pc(299), pc(653)))

        for i in range(9):
            pygame.draw.line(screen, 'black', (pc(283), pc(80) * i), (pc(923), pc(80) * i), pc(2))
            pygame.draw.line(screen, 'black', (pc(283) + pc(80) * i, 0), (pc(283) + pc(80) * i, pc(640)), pc(2))
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (pc(933), pc(658)))

# Desenha peças no tabuleiro
# draw pieces onto board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_locations[i][0] * pc(80) + pc(298), white_locations[i][1] * pc(80) + pc(14)))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * pc(80) + pc(292), white_locations[i][1] * pc(80) + pc(8)))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * pc(80) + pc(284), white_locations[i][1] * pc(80) + pc(1),
                                                 pc(80), pc(80)], pc(2))
                
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * pc(80) + pc(298), black_locations[i][1] * pc(80) + pc(18)))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * pc(80) + pc(292), black_locations[i][1] * pc(80) + pc(8)))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * pc(80) + pc(283), black_locations[i][1] * pc(80) + pc(1),
                                                 pc(80), pc(80)], pc(1))

# Função para verificar de todas as opções válidas de peças no tabuleiro
# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# Verifica os movimentos válidos do rei
# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Verifica os movimentos válidos da rainha
# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

# Verifica os movimentos válidos do bispo
# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
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
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
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
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# Verifica os movimentos válidos do cavalo
# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Verifica os movimentos válidos apenas para a peça selecionada
# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# Desenha os movimentos válidos apenas na tela
# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * pc(80) + pc(323), moves[i][1] * pc(80) + pc(40)), pc(4))

# Desenha as peças capturadas no lado direiro da tela
# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (pc(943), pc(4) + pc(40) * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (pc(1023), pc(4) + pc(40) * i))

# Desenha um quadrado vermelho ao redor do rei se ele estiver em cheque
# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * pc(80) + pc(283),
                                                              white_locations[king_index][1] * pc(80) + pc(1), pc(80), pc(80)], pc(4))
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * pc(80) + pc(1),
                                                               black_locations[king_index][1] * pc(80) + pc(1), pc(80), pc(80)], pc(4))

# Desenha o texto de game over
# Draw the game over text
def draw_game_over():
    pygame.draw.rect(screen, 'black', [pc(443), pc(290), pc(320), pc(56)])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (pc(451), pc(298)))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (pc(451), pc(322)))

# Loop principal do jogo
# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
    
run_menu = True
run = True
while run:
    
    while run_menu:
        timer.tick(fps)
        screen_menu.fill(color_menu)
        draw_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[0] >= 406 and event.pos[0] <= 956 and event.pos[1] >= pc(273) and event.pos[1] <= 353:
                    run_menu = False
        
        pygame.display.flip()
                
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = (event.pos[0] - pc(283)) // pc(80) 
            y_coord = event.pos[1] // pc(80)
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
    
pygame.quit()
sys.exit()