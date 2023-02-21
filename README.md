# Task_24_2_4
Задание 24.2.4: написать позитивные тесты к приложению Калькулятор

По заданию написано 4 позитивных теста:
1. test_adding_success - тест сложения
2. test_substraction_success - тест вычитания
3. test_div_success - тест деления
4. test_mult_success - тест умножения

В директории /tests располагается файл с тестами test.py

Для тестирования выполните команду pytest tests/test.py

N.B.: Методы setup и teardown были заменены на setup_method и teardown_method, т.к. pytest выдавал варнинги с предложением такой замены.
