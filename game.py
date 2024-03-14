import pygame
from gameparts import Board
from gameparts import draw_figures, draw_lines

pygame.init()

# Здесь определены разные константы, например
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (150, 190, 35)
LINE_COLOR = (23, 145, 135)
X_COLOR = (0, 0, 0)
O_COLOR = (255, 255, 255)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
# Задать размер графического окна для игрового поля.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок окна.
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом.
screen.fill(BG_COLOR)


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as score:
        score.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()

    # В цикле обрабатываются такие события, как
    # нажатие кнопок мыши и закрытие окна.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if clicked_row != ' ' and clicked_col != ' ':
                    game.make_move(clicked_row, clicked_col, current_player)

                    if game.check_win(current_player):
                        result = f'Победили {current_player}.'
                        print(result)
                        save_result(result)
                        running = False
                    elif game.is_board_full():
                        result = 'Ничья!'
                        print(result)
                        save_result(result)
                        running = False

                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)
        # Обновить окно игры
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
