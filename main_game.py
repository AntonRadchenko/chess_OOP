from figure import *

# общий класс для двух игр
class Game:
    """Базовый класс для игр шахматы и шашки."""
    
    def __init__(self):
        """Инициализирует игровую доску и начальные параметры игры."""
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_turn_active = 'white'  # Текущий ход за белыми
        self.turn_count = 0  # Счетчик ходов
        self.coordinates_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}  # Словарь для преобразования букв в индексы

    def display_board(self):
        """Отображает текущее состояние игровой доски в консоли."""
        letters_coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        nums_coords = [i for i in range(1, 9)]
        print()
        print('   ', *letters_coords, sep=' ', end='\n')  # Вывод буквенных координат
        print('  ', '-' * 17)  # Разделительная линия
        for row in range(8):
            print(nums_coords[row], end=' | ')  # Вывод числовых координат
            for col in range(8):
                figure = self.board[row][col]
                print(figure if figure else '.', end=' ')  # Вывод фигуры или точки
            print('|', nums_coords[row], end='\n')  # Завершение строки
        print('  ', '-' * 17)  # Разделительная линия
        print('   ', *letters_coords, sep=' ', end='')  # Вывод буквенных координат
        print()
        
    def get_figure(self, row, col):
        """Возвращает фигуру на указанной позиции.
        
        Args:
            row (int): Номер строки (0-7).
            col (int): Номер столбца (0-7).
            
        Returns:
            Figure or None: Фигура на клетке или None, если клетка пуста или вне доски.
        """
        if 0 <= row <= 7 and 0 <= col <= 7:
            return self.board[row][col]
        return None      
    
    def set_figure(self, row, col, figure):
        """Устанавливает фигуру на указанную позицию.
        
        Args:
            row (int): Номер строки (0-7).
            col (int): Номер столбца (0-7).
            figure (Figure): Фигура для установки.
        """
        if 0 <= row <= 7 and 0 <= col <= 7:
            self.board[row][col] = figure
            
    def play(self):
        """Запускает игровой цикл с вводом ходов игроками."""
        while True:
            self.display_board()
            print(f"\nХод {'белых' if self.white_turn_active == 'white' else 'черных'}")

            try:
                start_coordinate = input("Введите начальную координату: ")
                if start_coordinate.lower() in ['stop', 'exit']:
                    exit() if start_coordinate.lower() == 'stop' else main()
                if len(start_coordinate) != 2:
                    print("\nНекорректный ввод координаты")
                    continue

                start_col = self.coordinates_to_numbers[start_coordinate[0].lower()]
                start_row = int(start_coordinate[1]) - 1

                if self.board[start_row][start_col] is None:
                    print('\nНа данной клетке нет фигуры')
                    continue

                figure = self.board[start_row][start_col]
                if figure.side != self.white_turn_active:
                    print("\nЭта фигура не ваша")
                    continue

                end_coordinate = input("Введите конечную координату: ")
                if end_coordinate.lower() in ['stop', 'exit']:
                    exit() if end_coordinate.lower() == 'stop' else main()
                if len(end_coordinate) != 2:
                    print("\nНекорректный ввод координаты")
                    continue

                end_col = self.coordinates_to_numbers[end_coordinate[0].lower()]
                end_row = int(end_coordinate[1]) - 1

            except (ValueError, KeyError):
                print("\nНекорректный ввод")
                continue

            if not (0 <= start_row < 8 and 0 <= end_row < 8):
                print("\nДанная клетка пустая либо не существует")
                continue

            result = self.move_actions(start_row, start_col, end_row, end_col)
            if result:
                self.white_turn_active = 'black' if self.white_turn_active == 'white' else 'white'
            else:
                print("\nНедопустимый ход!")
     
# класс шахмат   
class ChessBoard(Game):
    """Дочерний класс для игры в шахматы, наследуемый от Game."""
    
    def __init__(self):
        """Инициализирует шахматную доску с расстановкой фигур."""
        Game.__init__(self)
        self.place_figures()
        
    def place_figures(self):
        """Расставляет шахматные фигуры на доске в начальной позиции."""
        # Ладьи
        self.board[0][0] = Rook('black', self, 0, 0)
        self.board[0][7] = Rook('black', self, 0, 7)
        self.board[7][0] = Rook('white', self, 7, 0)
        self.board[7][7] = Rook('white', self, 7, 7)
        
        # Кони
        self.board[0][6] = Night('black', self, 0, 6)
        self.board[0][1] = Night('black', self, 0, 1)
        self.board[7][1] = Night('white', self, 7, 1)
        self.board[7][6] = Night('white', self, 7, 6)
        
        # Слоны
        self.board[0][2] = Bishop('black', self, 0, 2)
        self.board[0][5] = Bishop('black', self, 0, 5)
        self.board[7][2] = Bishop('white', self, 7, 2)
        self.board[7][5] = Bishop('white', self, 7, 5)
        
        # Ферзи
        self.board[0][3] = Queen('black', self, 0, 3)
        self.board[7][3] = Queen('white', self, 7, 3)
        
        # Короли
        self.board[0][4] = King('black', self, 0, 4)
        self.board[7][4] = King('white', self, 7, 4)
        
        # Пешки
        for col in range(8):   
            self.board[1][col] = Pawn('black', self, 1, col)
            self.board[6][col] = Pawn('white', self, 6, col)
            
        # Новые фигуры
        # Лайт-ладьи
        self.board[2][1] = LiteRook('black', self, 2, 1)
        self.board[2][6] = LiteRook('black', self, 2, 6)
        self.board[5][1] = LiteRook('white', self, 5, 1)
        self.board[5][6] = LiteRook('white', self, 5, 6)
        
        # Прыгуны
        self.board[2][3] = Jumpman('black', self, 2, 3)
        self.board[5][3] = Jumpman('white', self, 5, 3)
        
        # Оборотни
        self.board[3][7] = WereWolf('black', self, 3, 7)  # Исправлено: row с 2 на 3
        self.board[4][7] = WereWolf('white', self, 4, 7)  # Исправлено: row с 5 на 4
        
    def find_king(self, side):
        """Находит позицию короля указанной стороны.
        
        Args:
            side (str): Сторона ('white' или 'black').
            
        Returns:
            tuple or None: Кортеж (row, col) с позицией короля или None, если король не найден.
        """
        for row in range(8):
            for col in range(8):
                figure = self.board[row][col]
                if isinstance(figure, King) and figure.side == side:
                    return row, col
        return None
    
    def is_check(self, side):
        """Проверяет, находится ли король указанной стороны под шахом (а также другие фигуры ходящего игрока под угрозой).
        
        Args:
            side (str): Сторона ('white' или 'black').
            
        Returns:
            bool: True, если король под шахом, иначе False.
        """
        king_pos = self.find_king(side)
        if king_pos is None:
            return False

        king_in_check = False
        threatened_figures = []

        for row in range(8):
            for col in range(8):
                figure = self.board[row][col]
                if figure is not None and figure.side == side:
                    for other_figure_row in range(8):
                        for other_figure_col in range(8):
                            other_figure = self.board[other_figure_row][other_figure_col]
                            if other_figure is not None and other_figure.side != side:
                                other_figure_moves = other_figure.get_actions()
                                if (row, col) in other_figure_moves:
                                    threatened_figures.append((row, col, figure))
                                    break

        for row in range(8):
            for col in range(8):
                figure = self.board[row][col]
                if figure is not None and figure.side != side:
                    figure_valid_moves = figure.get_actions()
                    if king_pos in figure_valid_moves:
                        king_in_check = True

        if threatened_figures:
            print(f"\nФигуры {'белых' if side == 'white' else 'черных'} под боем:")
            for row, col, figure in threatened_figures:
                print(f"{figure} на {chr(ord('a') + col)}{row + 1}")

        return king_in_check 
    
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        """Проверяет корректность хода в шахматах.
        
        Args:
            start_row (int): Начальная строка.
            start_col (int): Начальный столбец.
            end_row (int): Конечная строка.
            end_col (int): Конечный столбец.
            
        Returns:
            bool: True, если ход допустим, иначе False.
        """
        figure = self.get_figure(start_row, start_col)
        if figure is None or figure.side != self.white_turn_active:
            return False

        figure_step = self.get_figure(end_row, end_col)

        if isinstance(figure, WereWolf):
            if figure_step is not None and figure_step.side == figure.side:
                return True
            else:
                return False

        if figure_step is not None and figure_step.side == figure.side:
            return False

        valid_moves = figure.get_actions()
        if (end_row, end_col) not in valid_moves:
            return False

        original_start_figure = self.board[start_row][start_col]
        original_end_figure = self.board[end_row][end_col]

        self.board[end_row][end_col] = figure
        self.board[start_row][start_col] = None
        figure.row, figure.col = end_row, end_col

        is_king_in_check = self.is_check(figure.side)

        self.board[start_row][start_col] = original_start_figure
        self.board[end_row][end_col] = original_end_figure
        figure.row, figure.col = start_row, start_col

        if is_king_in_check:
            print('\nКороль под шахом')
            return False

        return True
    
    def move_actions(self, start_row, start_col, end_row, end_col):
        """Выполняет ход в шахматах с учетом всех правил.
        
        Args:
            start_row (int): Начальная строка.
            start_col (int): Начальный столбец.
            end_row (int): Конечная строка.
            end_col (int): Конечный столбец.
            
        Returns:
            bool: True, если ход успешен, иначе False.
        """
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            return False

        figure = self.get_figure(start_row, start_col)
        if figure is None:
            return False

        target_figure = self.get_figure(end_row, end_col)

        if isinstance(figure, WereWolf):
            if target_figure is not None and target_figure.side == figure.side:
                self.board[start_row][start_col] = target_figure
                self.board[end_row][end_col] = figure
                figure.row, figure.col = end_row, end_col
                target_figure.row, target_figure.col = start_row, start_col
        else:
            self.board[end_row][end_col] = figure
            self.board[start_row][start_col] = None
            figure.row, figure.col = end_row, end_col

        if isinstance(figure, Pawn):
            figure.pawn_move(end_row, end_col)
            if (figure.side == 'white' and end_row == 0) or (figure.side == 'black' and end_row == 7):
                self.board[end_row][end_col] = Queen(figure.side, self, end_row, end_col)
                
        if isinstance(figure, LiteRook):
            if (figure.side == 'white' and end_row == 0) or (figure.side == 'black' and end_row == 7):
                self.board[end_row][end_col] = Rook(figure.side, self, end_row, end_col)
                
        self.turn_count += 1
        print('\nХод выполнен успешно!')
        print(f'Кол-во ходов: {self.turn_count}')
        return True
    
# класс шашек
class CheckersBoard(Game):
    """Дочерний класс для игры в шашки, наследуемый от Game."""
    
    def __init__(self):
        """Инициализирует доску для шашек с расстановкой фигур."""
        Game.__init__(self)
        self.place_figures()
        
    def place_figures(self):
        """Расставляет шашки на доске в начальной позиции."""
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = PawnCheckers('black', self, row, col)
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = PawnCheckers('white', self, row, col)
    
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        """Проверяет корректность хода в шашках.
        
        Args:
            start_row (int): Начальная строка.
            start_col (int): Начальный столбец.
            end_row (int): Конечная строка.
            end_col (int): Конечный столбец.
            
        Returns:
            bool: True, если ход допустим, иначе False.
        """
        figure = self.get_figure(start_row, start_col)
        if figure is None or figure.side != self.white_turn_active:
            return False

        figure_step = self.get_figure(end_row, end_col)
        if figure_step is not None and figure_step.side == figure.side:
            return False

        valid_moves = figure.get_actions()
        if (end_row, end_col) not in valid_moves:
            return False

        return True
    
    def move_actions(self, start_row, start_col, end_row, end_col):
        """Выполняет ход в шашках с учетом всех правил.
        
        Args:
            start_row (int): Начальная строка.
            start_col (int): Начальный столбец.
            end_row (int): Конечная строка.
            end_col (int): Конечный столбец.
            
        Returns:
            bool: True, если ход успешен, иначе False.
        """
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            return False

        figure = self.get_figure(start_row, start_col)
        if figure is None:
            return False

        self.board[end_row][end_col] = figure
        self.board[start_row][start_col] = None
        figure.row, figure.col = end_row, end_col

        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 2:
            middle_row = (start_row + end_row) // 2
            middle_col = (start_col + end_col) // 2
            self.board[middle_row][middle_col] = None
            
        if isinstance(figure, KingCheckers):
            direction_row = 1 if end_row > start_row else -1
            direction_col = 1 if end_col > start_col else -1
            row, col = start_row + direction_row, start_col + direction_col
            while row != end_row or col != end_col:
                target_figure = self.get_figure(row, col)
                if target_figure is not None and target_figure.side != figure.side:
                    self.board[row][col] = None
                    break
                row += direction_row
                col += direction_col

        if isinstance(figure, PawnCheckers):
            figure.pawn_checkers_move(end_row, end_col)
            if (figure.side == 'white' and end_row == 0) or (figure.side == 'black' and end_row == 7):
                self.board[end_row][end_col] = KingCheckers(figure.side, self, end_row, end_col)
        
        self.turn_count += 1
        print('\nХод выполнен успешно!')
        print(f'Кол-во ходов: {self.turn_count}')
        return True
    
def main():
    """Запускает выбор игры и инициализирует игровой процесс."""
    print("Выберите игру:")
    print("1. Шахматы")
    print("2. Шашки")
    choice = input("Введите номер: ")

    if choice == '1':
        game = ChessBoard()
    elif choice == '2':
        game = CheckersBoard()
    elif choice.lower() == 'exit':
        exit()
    else:
        print("Некорректный ввод!")
        return
        
    game.play()

if __name__ == "__main__":
    main()
