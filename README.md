# Описание

Программа использует API сервисы крупнейших российских компаний интернет-рекрутмента: [HH](https://hh.ru/) и [Superjob](https://www.superjob.ru/) для
поиска вакансий по самым распространенным языкам программирования, данные выводит в консоль в удобном формате.
Описание API находится по адресу: [API HH](https://github.com/hhru/api) и [API SuperJob]https://api.superjob.ru/  соответственно.

# Требования к окружению

Для работы программы необходим установленный Python.
Проверялось на следующей конфигурации:
Windows 10, Python 3.9.

# Как установить

Для корректной работы необходимо установить библиотеки.
Используйте pip для установки зависимостей:

```
pip install -r requirements.txt
```

# Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
API HH работает без токена, но для площадки SuperJob требуется SECRET_KEY.
'SECRET_KEY' - токен можно получить после регистрации на сайте (https://api.superjob.ru/info/).

# Как запустить программу

Программу необходимо запускать из командной строки:

```
python main.py
```



# Цель проекта

Демонстрация возможнойстей api сервисов в учебных целях.

