# Homework

## Задания

### 1. Числа и арифметические выражения

- circle
- pizza_delivery

### 2. Логические выражения, `bool`, `if`/`elif`/`else`

- coins
- leap_year
- lessons

### 3. Строки

- str_remove_fragment
- password_checker
- chess_fen
- atbash_cipher

### 4. Iterable

- hamming_distance
- polygon
- bible

## Краткая инструкция

1. Установите git и `pytest`

    ```sh
    pip install pytest
    ```

2. Сделайте fork данного репозитория (т.е. https://github.com/intyamo/homework)

   Через кнопку `fork` и `git clone`:

    ```sh
    git clone https://github.com/<github_username>/homework.git
    # ssh
    git clone git@github.com:<github_username>/homework.git
    ```

   Или через [GitHub CLI](https://github.com/cli/cli#installation):

    ```
    gh repo fork intyamo/homework
    ```

3. Создайте отделную ветку для текущего ДЗ

    ```sh
    git checkout -b dz_1
    # или
    git switch --create dz_1
    ```

4. Решите задание

   Каждое задание находится в отдельной папке:

    ```sh
    circle
    ├── circle          # само задание
    └── test_circle.py  # а это тесты
    ```

5. Проверьте тесты

    ```sh
    # из корневой папки
    pytest <папка_с_заданием>

    # или непосредственно из папки с заданием, например
    cd circle
    pytest
    ```

6. Commit, push

   Рекомендуется перед коммитом отформатировать код

    - через PyCharm (`Code -> Reformat code`)
    - или [`black`](https://github.com/psf/black)

    ```sh
    pip install black
    black circle/circle.py
    ```

7. Открыть pull request (PR)
