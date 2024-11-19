# Aiogram Example
![Static Badge](https://img.shields.io/badge/aiogram-3.x-blue)
![Static Badge](https://img.shields.io/badge/loguru-0.7.2-green)
![Static Badge](https://img.shields.io/badge/pydantic-2.8.2-cyan)
![Static Badge](https://img.shields.io/badge/pydantic_settings-2.3.4-red)
## Использование
Перед установкой обратите внимание на то что в папке bot/database/db.py есть реализация базы данных на mongodb но она не полная, рекомендуется доделать ее самим, и в bot/updates/base_updates.py есть тоже реализация, как пример, а также в bot/middlwares есть тоже реализвация, которая полностью работает и делает то что нужно (троттлинг).

1. Зависимости:
```
pip install -r requirements.txt
```
2. Создаем файл в основной директории рядом с main.py, называем файл .env и записываем туда переменную BOT_TOKEN="сюда токен телеграм"

3. Запускаем (py main.py) и проверяем через команду ```/start``` в личных сообщениях

##To Do list
--

## Благодарность (credits)

--


## Некоторые нюансы
* Если вы не будете использовать все те модули которые тут есть то используйте venv: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

* Если в директории есть файл delete-me.please то удаляем его, он нужен что бы пустые папки сюда тоже добавлялись
