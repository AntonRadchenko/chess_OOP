# chess_OOP
Задание 1 Семестр 2
---

## Шахматы (и Шашки)

Добро пожаловать в консольную реализацию шахмат и шашек на Python. Этот проект объединяет две настольные игры с добавлением уникальных фигур для шахмат.

Установка:
1. Убедитесь, что у вас установлен Python 3.
2. Клонируйте репозиторий:
   git clone https://github.com/yourusername/chess-and-checkers.git
   cd chess-and-checkers

Использование:
1. Запустите игру:
   python game.py
2. Выберите режим:
   - 1 - Шахматы
   - 2 - Шашки
   - exit - Выход
3. Вводите координаты ходов (например, e2 для начальной позиции, e4 для конечной).
4. Для завершения игры введите stop или exit.

Пример вывода:

<img width="355" alt="Снимок экрана 2025-03-18 в 01 00 49" src="https://github.com/user-attachments/assets/0d937e2f-8e30-4dad-8a73-05efa9d2b4de" />


Ход белых
Введите начальную координату: e2
Введите конечную координату: e4
Ход выполнен успешно!
Кол-во ходов: 1

Структура проекта:
- figure.py: Определения всех фигур (шахматных и шашечных).
- game.py: Логика игры, включая классы ChessBoard и CheckersBoard.

Шахматные фигуры:
- King: Ходит на 1 клетку в любом направлении
- Queen: Ходит на любое расстояние по линиям и диагоналям
- Rook: Ходит на любое расстояние по линиям
- Bishop: Ходит на любое расстояние по диагоналям
- Night (Конь): Ходит буквой "Г" (2+1 или 1+2)
- Pawn: Ходит вперёд, бьёт по диагонали
- LiteRook: Ладья с ходом до 2 клеток
- Jumpman: Прыгает на 2 клетки в любом направлении
- WereWolf: Меняется местами с соседней своей фигурой

Шашечные фигуры:
- PawnCheckers: Ходит вперёд на 1, бьёт через прыжок
- KingCheckers: Ходит по диагонали на любое расстояние

Правила:
- Шахматы: Стандартные правила с добавлением новых фигур. Пешки превращаются в ферзей, LiteRook - в обычные ладьи при достижении края.
- Шашки: Классические правила с превращением шашек в дамки. Взятие через прыжок пока необязательно.

Разработка и улучшения:
Хотите внести вклад? Вот идеи для улучшений:
- Добавить проверку мата и пата в шахматах.
- Сделать взятие в шашках обязательным.
- Реализовать графический интерфейс (например, с Pygame).
- Добавить ИИ для игры против компьютера.

Форкните репозиторий, внесите изменения и отправьте Pull Request!

Лицензия:
Проект распространяется под лицензией MIT. Используйте и модифицируйте код свободно!

Автор:
Создано yourusername. Вопросы и предложения приветствуются в Issues на GitHub!

---

Теперь вы можете скопировать этот текст в файл с расширением `.txt` (например, `README.txt`) и использовать его как документацию к проекту. Для GitHub всё ещё лучше использовать версию с Markdown, но эта версия идеально подойдёт для текстового формата. Замените `yourusername` на ваш логин GitHub, если планируете публиковать проект.
