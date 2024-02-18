# OtusHW
***

**Домашнее задание №1:** 
***
**Научиться работать с pull request и использовать линтеры**

***Описание:***

    Зарегистрироваться на github.com
    Создать репозиторий и склонировать его локально
    Создать новую ветку
    Скопировать в репозиторий файл fix_me.py
    Установить один из линтеров - flake8 или pylint (можно оба)
    Запустить проверку файла fix_me.py с помощью установленного линтера
    Изучить ошибки, которые выдаст линтер и устранить их
    Запустить линтер повторно и убедиться, что больше ошибок не возникает
    Добавить в репозиторий файлы README.md и .gitignore
    Оформить pull request и прислать его на проверку

    Итоговые файлы: fix_me.py
***

**Домашнее задание №2:** 
***
**Научиться писать код в ООП стиле**

***Описание:***

    Создать базовый класс геометрической фигуры (Figure)
    Реализовать классы геометрических фигур Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle)
    Каждый класс должен располагаться в отдельном файле с соответствующим названием (например, class Triangle => triangle.py).
    Все файлы с классами должны находиться в директории src/ в корне репозитория.
    Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя, то выбрасывать ошибку raise ValueError.
    Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур (никакого хардкода значений).
    Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур.
    Если в метод передана не геометрическая фигура, то нужно выбрасывать ошибку raise ValueError.
    
    Итоговые файлы: Circle.py, Figure.py, Rectangle.py, Square.py, Triangle.py
***


**Домашнее задание №3:** 
***
**Научиться покрывать код тестами с использованием pytest**

***Описание:***

    Написать тесты с использованием pytest на классы из ДЗ "ООП на практике".
    Глубину покрытия и объем определить самостоятельно, но минимум проверить реализацию всех указанных требований для каждого класса.
    Все тесты должны располагаться в директории tests/ в корне репозитория.
    
    Итоговые файлы: tests/test_classes.py
***

**Домашнее задание №4:** 
***
**Научиться работать с различными типами файлов**

***Описание:***

    Написать скрипт, который из двух файлов (CSV с книгами и JSON с пользователями) будет читать данные и на их основании создаст result.json файл со структурой: 
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": user_books
    Идея в том что нужно раздать все книги из csv файла пользователям из списка. Книги складываются в виде словарей в массив books у каждого пользователя.
    Книг изначально больше чем пользователей, поэтому раздавать нужно по принципу "максимально поровну", т.е. если книг, например 10. а пользователей 3 то распределение будет таким - 4 3 3 (один получит оставшуюся книгу).
    Итоговая структура должна соответствовать стандарту json и парситься соответствующей библиотекой.
  

    Итоговые файлы: result.json
***

**Домашнее задание №5:** 
***
**Потренироваться тестировать API сервисы на основе их документации**

***Описание:***

    Написать тесты для API сервисов
    Реализовать в отдельном модуле (файле) тестовую функцию, которая будет принимать 2 параметра:
    url - значение по умолчанию https://ya.ru
    status_code - значение по умолчанию 200
  
    Итоговые файлы: test_dog_api.py, test_jsonplaceholder_api.py, test_module.py, test_breweries_api.py, conftest.py
***