from gameparts import (
    Board, FieldIndexError, CellOccupiedError
    )


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as score:
        score.write(result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                row = (int(input('Введите номер строки: ')) - 1)
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = (int(input('Введите номер столбца: ')) - 1)
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    f'Значение должно быть от 1 до {game.field_size}.'
                )
                print(
                    'Пожалуйста введите значение для '
                    'строки и столбца заново.'
                )
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для '
                    'строки и столбца заново.'
                    )
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        print('Ход сделан!')

        game.display()

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


if __name__ == '__main__':
    main()
