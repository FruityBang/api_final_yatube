**Проект API Yatube - все для общения через API. Связываем людей, связываем жизни.**

Реализация на основе Django REST Framework с использованием аутентификации по токену
(JWT + Djoser) и ограничением прав доступа.

***Как запустить проект:***

- Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:FruityBang/api_final_yatube.git

cd api_final_yatube

- Cоздать и активировать виртуальное окружение:

python -m venv venv

source venv/Scripts/activate

- Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip

pip install -r requirements.txt

- Выполнить миграции:

python manage.py migrate

- Запустить проект:

python3 manage.py runserver

*Доступные эндпоинты:*

- http://127.0.0.1:8000/api/v1/posts/

- http://127.0.0.1:8000/api/v1/groups/

- http://127.0.0.1:8000/api/v1/follow/

- http://127.0.0.1:8000/api/v1/jwt/


*Запросы:*

- POST http://127.0.0.1:8000/api/v1/posts/
{
"text": "string",
"image": "string",
"group": 0
}

- POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
{
"text": "string"
}

- POST http://127.0.0.1:8000/api/v1/follow/
{
"following": "string"
}
