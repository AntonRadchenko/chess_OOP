class Figure:
    """Базовый класс для всех шахматных фигур."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует фигуру с указанной стороной, доской и позицией.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски, на которой находится фигура.
            row (int): Номер строки (0-7).
            col (int): Номер столбца (0-7).
        """
        self.side = side
        self.board = board
        self.row = row
        self.col = col

    def is_valid_pos(self, row, col):
        """Проверяет, находится ли позиция в пределах шахматной доски.
        
        Args:
            row (int): Номер строки для проверки.
            col (int): Номер столбца для проверки.
            
        Returns:
            bool: True, если позиция в пределах доски, иначе False.
        """
        return 0 <= row < 8 and 0 <= col < 8
    
    def __str__(self):
        """Возвращает строковое представление фигуры.
        
        Returns:
            str: Заглавная буква названия класса для белых фигур, строчная для черных.
        """
        return self.__class__.__name__[0].upper() if self.side == 'white' else self.__class__.__name__[0].lower()
        
class King(Figure):
    """Класс, представляющий короля в шахматах."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует короля.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
    
    def get_actions(self):
        """Возвращает список возможных ходов короля.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0)]
        
        for move_row, move_col in directions:
            row2 = self.row + move_row
            col2 = self.col + move_col
            
            if not self.is_valid_pos(row2, col2):
                continue
            result.append((row2, col2))
        return result
    
class Bishop(Figure):
    """Класс, представляющий слона в шахматах."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует слона.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список возможных ходов слона.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        for move_row, move_col in directions:
            mul = 0
            while True:
                mul += 1
                row2 = self.row + move_row * mul
                col2 = self.col + move_col * mul
                if not self.is_valid_pos(row2, col2):
                    break
                result.append((row2, col2))
                
                if self.board.get_figure(row2, col2) is not None:
                    break
        return result
                    
class Rook(Figure):
    """Класс, представляющий ладью в шахматах."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует ладью.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список возможных ходов ладьи.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        
        for move_row, move_col in directions:
            mul = 0
            while True:
                mul += 1
                row2 = self.row + move_row * mul
                col2 = self.col + move_col * mul
                if not self.is_valid_pos(row2, col2):
                    break
                result.append((row2, col2))
                
                if self.board.get_figure(row2, col2) is not None:
                    break
        return result
    
class Night(Figure):
    """Класс, представляющий коня в шахматах."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует коня.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
    
    def get_actions(self):
        """Возвращает список возможных ходов коня.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
        
        for move_row, move_col in directions:
            row2 = self.row - move_row
            col2 = self.col + move_col
            target_figure = self.board.get_figure(row2, col2)
            if target_figure is None or target_figure.side != self.side:
                result.append((row2, col2))  
        return result
    
class Pawn(Figure):
    """Класс, представляющий пешку в шахматах."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует пешку.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)    
        self.is_first_move = True
    
    def get_actions(self):
        """Возвращает список возможных ходов пешки.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        if self.side == 'white':
            self.direction = -1
        else:
            self.direction = 1
        
        row2 = self.row + self.direction
        col2 = self.col
        if self.is_valid_pos(row2, col2) and self.board.get_figure(row2, col2) is None:
            result.append((row2, col2))
            
            if self.is_first_move:
                row3 = self.row + self.direction * 2
                col3 = self.col
                if self.is_valid_pos(row3, col3) and self.board.get_figure(row3, col3) is None:
                    result.append((row3, col3))
        
        for diag_cell in [-1, 1]:
            row2 = self.row + self.direction
            col2 = self.col + diag_cell   
            if self.is_valid_pos(row2, col2):
                figure = self.board.get_figure(row2, col2)
                if figure is not None and figure.side != self.side:
                    result.append((row2, col2))
        return result
        
    def pawn_move(self, row, col):
        """Перемещает пешку на новую позицию и сбрасывает флаг первого хода.
        
        Args:
            row (int): Новая строка.
            col (int): Новый столбец.
        """
        self.row = row
        self.col = col
        self.is_first_move = False
    
class Queen(Figure):
    """Класс, представляющий ферзя в шахматах."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует ферзя.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список возможных ходов ферзя.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0)]
        
        for move_row, move_col in directions:
            mul = 0
            while True:
                mul += 1
                row2 = self.row + move_row * mul
                col2 = self.col + move_col * mul
                if not self.is_valid_pos(row2, col2):
                    break
                result.append((row2, col2))
                
                if self.board.get_figure(row2, col2) is not None:
                    break
        return result
    
class LiteRook(Figure):
    """Класс, представляющий лайт-ладью (облегченную ладью) с ходом максимум на 2 клетки."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует облегченную ладью.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список возможных ходов облегченной ладьи.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями (до 2 клеток).
        """
        result = []
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        
        for move_row, move_col in directions:
            mul = 0
            while True:
                mul += 1
                row2 = self.row + move_row * mul
                col2 = self.col + move_col * mul
                if not self.is_valid_pos(row2, col2):
                    break
                result.append((row2, col2))
                
                if self.board.get_figure(row2, col2) is not None or mul >= 2:
                    break
        return result
    
class Jumpman(Figure):
    """Класс, представляющий фигуру 'Прыгун', которая прыгает на 2 клетки в любую сторону."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует Прыгуна.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список возможных ходов Прыгуна.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(0, 2), (2, 2), (2, 0), (2, -2), (0, -2), (-2, -2), (-2, 0)]
        
        for move_row, move_col in directions:
            row2 = self.row - move_row
            col2 = self.col + move_col
            target_figure = self.board.get_figure(row2, col2)
            if target_figure is None or target_figure.side != self.side:
                result.append((row2, col2))  
        return result

class WereWolf(Figure):
    """Класс, представляющий Оборотня, который меняется местами с соседней фигурой своей стороны."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует Оборотня.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список позиций, с которыми Оборотень может поменяться местами.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        
        for move_row, move_col in directions:
            row2 = self.row + move_row  # Исправлено: было '=' вместо '+'
            col2 = self.col + move_col  # Исправлено: было '=' вместо '+'
        
            if not self.is_valid_pos(row2, col2):
                continue
            
            target_figure = self.board.get_figure(row2, col2)
            if target_figure is not None and target_figure.side == self.side:
                result.append((row2, col2))
        return result
    
    def swap(self, row, col):
        """Меняет местами Оборотня с фигурой на указанной позиции.
        
        Args:
            row (int): Строка целевой фигуры.
            col (int): Столбец целевой фигуры.
            
        Returns:
            bool: True, если обмен успешен, иначе False.
        """
        target_figure = self.board.get_figure(row, col)    

        if target_figure is None or target_figure.side != self.side:
            return False
        
        current_row, current_col = self.row, self.col
        
        self.board.set_figure(current_row, current_col, target_figure)
        self.board.set_figure(row, col, self)
        
        self.row, self.col = row, col
        target_figure.row, target_figure.col = current_row, current_col
        
        return True
    
class PawnCheckers(Figure):
    """Класс, представляющий шашку в игре шашки."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует шашку.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
    
    def get_actions(self):
        """Возвращает список возможных ходов шашки.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        if self.side == 'white':
            direction = -1
        else:
            direction = 1

        for diag_cell in [-1, 1]:
            row2 = self.row + direction
            col2 = self.col + diag_cell
            if self.is_valid_pos(row2, col2) and self.board.get_figure(row2, col2) is None:
                result.append((row2, col2))
                
        for diag_cell in [-1, 1]:
            row2 = self.row + direction * 2
            col2 = self.col + diag_cell * 2
            if self.is_valid_pos(row2, col2) and self.board.get_figure(row2, col2) is None:
                middle_row = self.row + direction
                middle_col = self.col + diag_cell
                middle_figure = self.board.get_figure(middle_row, middle_col)
                if middle_figure is not None and middle_figure.side != self.side:
                    result.append((row2, col2))
                    
        for diag_cell in [-1, 1]:
            row2 = self.row - direction * 2
            col2 = self.col + diag_cell * 2
            if self.is_valid_pos(row2, col2) and self.board.get_figure(row2, col2) is None:
                middle_row = self.row - direction
                middle_col = self.col + diag_cell
                middle_figure = self.board.get_figure(middle_row, middle_col)
                if middle_figure is not None and middle_figure.side != self.side:
                    result.append((row2, col2))
        return result

    def pawn_checkers_move(self, row, col):
        """Перемещает шашку на новую позицию.
        
        Args:
            row (int): Новая строка.
            col (int): Новый столбец.
        """
        self.row = row
        self.col = col

class KingCheckers(Figure):
    """Класс, представляющий дамку в игре шашки."""
    
    def __init__(self, side, board, row, col):
        """Инициализирует дамку.
        
        Args:
            side (str): Сторона фигуры ('white' или 'black').
            board (Board): Объект доски.
            row (int): Номер строки.
            col (int): Номер столбца.
        """
        Figure.__init__(self, side, board, row, col)
        
    def get_actions(self):
        """Возвращает список возможных ходов дамки.
        
        Returns:
            list: Список кортежей (row, col) с доступными позициями.
        """
        result = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for move_row, move_col in directions:
            mul = 1
            found_enemy = False
            while True:
                row2 = self.row + move_row * mul
                col2 = self.col + move_col * mul
                if not self.is_valid_pos(row2, col2):
                    break
                
                figure_step = self.board.get_figure(row2, col2)
                if figure_step is None:
                    if not found_enemy:
                        result.append((row2, col2))
                    else:
                        result.append((row2, col2))
                        break
                else:
                    if figure_step.side == self.side:
                        break
                    else:
                        if found_enemy:
                            break
                        else:
                            found_enemy = True
                mul += 1    
        return result 