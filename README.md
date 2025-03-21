# Шахматы: объектно-ориентированная версия
---

Добро пожаловать в консольную реализацию шахмат и шашек на Python. Этот проект объединяет две настольные игры с добавлением уникальных фигур для шахмат.

<img width="261" alt="Снимок экрана 2025-03-18 в 01 05 27" src="https://github.com/user-attachments/assets/065d4d9d-8985-44a4-8540-d08715f83f6c" />

### Установка:
1. Убедитесь, что у вас установлен Python 3.
2. Клонируйте репозиторий:
   git clone https://github.com/AntonRadchenko/chess_OOP.git
3. Перейдите в папку:
   cd chess_OOP

### Использование:
1. Запустите игру:
   python main_game.py
2. Выберите режим:
   - 1 - Шахматы
   - 2 - Шашки
   - exit - Выход
3. Вводите координаты ходов (например, e2 для начальной позиции, e4 для конечной).
4. Для завершения игры введите stop или exit.

### Пример вывода:

<img width="355" alt="Снимок экрана 2025-03-18 в 01 00 49" src="https://github.com/user-attachments/assets/0d937e2f-8e30-4dad-8a73-05efa9d2b4de" />

### Структура проекта:
- figure.py: Определения всех фигур (шахматных и шашечных), включая общий класс фигур Figure.
- main_game.py: Логика игры, включая классы ChessBoard и CheckersBoard и их родительский класс Game, имеющий общие методы.

### Шахматные фигуры:
- King: Ходит на 1 клетку в любом направлении
- Queen: Ходит на любое расстояние по линиям и диагоналям
- Rook: Ходит на любое расстояние по линиям
- Bishop: Ходит на любое расстояние по диагоналям
- Night (Конь): Ходит буквой "Г" (2+1 или 1+2)
- Pawn: Ходит вперёд, бьёт по диагонали
- LiteRook: Ладья с ходом до 2 клеток
- Jumpman: Прыгает на 2 клетки в любом направлении
- WereWolf: Меняется местами с соседней своей фигурой

### Шашечные фигуры:
- PawnCheckers: Ходит вперёд на 1, бьёт через прыжок
- KingCheckers: Ходит по диагонали на любое расстояние

### Дополнительные задания:
#### Реализовано 4 дополнительных задания:
1. (Сложность 1): Вывод фигур ходящего игрока, находящиеся под угрозой + шах короля

<img width="356" alt="Снимок экрана 2025-03-18 в 01 17 38" src="https://github.com/user-attachments/assets/488ef81a-3e57-4afd-85dd-8e0fdeebd0b1" />
<img width="359" alt="Снимок экрана 2025-03-18 в 01 18 11" src="https://github.com/user-attachments/assets/3bd45505-ac67-4912-9154-824f111ae947" />


2. (Сложность 1): Реализация 3-х новых фигур: LiteRook, Jumpman и Werewolf

<img width="254" alt="Снимок экрана 2025-03-18 в 01 21 46" src="https://github.com/user-attachments/assets/da5c11aa-90da-4171-87f3-137a963f1f1a" />

(LiteRook также имеет усложнение: превращение в Rook при достижении противоположного края игрового поля)

3. (Сложность 1): Сложные правила для пешки: на картинке демострация одного из них (превращение пешки в другую фигуру при достижении противоположного края игрового поля):

![CleanShot 2025-03-18 at 01 25 48@2x](https://github.com/user-attachments/assets/323d7532-36fa-415d-9e61-751c2ccf5b60)

4. (Сложность 2): Реализация игры в Шашки (модификация шахмат)

<img width="353" alt="Снимок экрана 2025-03-18 в 01 27 53" src="https://github.com/user-attachments/assets/6faba14b-d066-4c50-8cf3-f2740edd2f85" />

### Правила:
- Шахматы: Стандартные правила с добавлением новых фигур. Пешки превращаются в ферзей, LiteRook - в обычные ладьи при достижении края.
- Шашки: Классические правила с превращением шашек в дамки. Взятие через прыжок пока необязательно.
___

#### Автор проекта:
AntonRadchenko.
