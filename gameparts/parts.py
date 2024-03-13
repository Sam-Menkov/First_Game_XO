# Объявить класс
class Board:
    """Класс который описывает игровое поле."""

    # Новый атрибут.
    field_size = 3

    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы это пустые клетки.
    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    # Метод проверки пустых ячеек для продолжения игры
    # или объявления ничьей.
    def is_board_full(self):
        for row in range(self.field_size):
            for column in range(self.field_size):
                if self.board[row][column] == ' ':
                    return False
        return True

    # Метод определения победы.
    def check_win(self, player):
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

    # Переопределение метода __str__.
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
