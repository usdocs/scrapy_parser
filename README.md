# scrapy_parser_pep
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=5fe620)](https://scrapy.org/)

## Парсинг документов PEP
Асинхронный парсер собирающий данные о Python Enhancement Proposals (PEP) с сайта `https://peps.python.org/`.
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет
несколько файлов в формате `.csv` в папке `results/...`:
* Список PEP (номер, название и статус);
* Подсчитывает общее количество каждого статуса и сумму всех статусов.

## Технологии проекта
* Python — высокоуровневый язык программирования.
* Scrapy — популярный фреймворк для парсинга веб сайтов. Особенности:
    * Многопоточность
    * Веб-краулер для перехода от ссылки к ссылке
    * Извлечение данных
    * Проверка данных
    * Сохранение в другой формат/базу данных
    * Многое другое

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:usdocs/scrapy_parser_pep.git
```

Создать и активировать виртуальное окружение:
```
python -m venv env
```

```
source venv/Scripts/activate
```

Обновить менеджер пакетов pip:
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

## Запуск парсера
```
scrapy crawl pep
```

Автор: [Балакин Андрей](https://github.com/usdocs)
