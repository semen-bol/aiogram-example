# AioGram Example
![Static Badge](https://img.shields.io/badge/aiogram-3.x-blue)
![Static Badge](https://img.shields.io/badge/loguru-0.7.2-green)
![Static Badge](https://img.shields.io/badge/pydantic-2.8.2-cyan)
![Static Badge](https://img.shields.io/badge/pydantic_settings-2.3.4-red)
## Использование
Перед установкой обратите внимание на то что в папке bot/database/db.py нету реализации базы данных, и в bot/updates/base_updates.py нету реализации но есть инструкция для чего и как юзать.

1. Зависимости:
```
pip install -r requirements.txt
```
2. Меняем данные в файле ```.env``` на свои (переменная BOT_TOKEN)

3. Запускаем и проверяем через команду ```/start``` в личных сообщениях
