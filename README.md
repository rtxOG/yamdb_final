# CI и CD проекта api_yamdb.

![CI/CD api_yamdb](https://github.com/rtxog/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание
Настроены для приложения Continuous Integration и Continuous Deployment: автоматический запуск тестов, обновление образов на Docker Hub, автоматический деплой на боевой сервер при пуше в главную ветку main.

Проект Yamdb_final создан для демонстрации методики DevOps (Development Operations) и идеи Continuous Integration (CI),
суть которых заключается в интеграции и автоматизации следующих процессов:
* синхронизация изменений в коде
* сборка, запуск и тестерование приложения в среде, аналогичной среде боевого сервера
* деплой на сервер после успешного прохождения всех тестов
* уведомление об успешном прохождении всех этапов

Само приложение взято из проекта api_yamdb, который представляет собой API сервиса отзывов о фильмах, книгах и музыке.
Зарегистрированные пользователи могут оставлять отзывы (Review) на произведения (Title).
Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка». 
Список категорий может быть расширен администратором. Приложение сделано с помощью Django REST Framework.

Для Continuous Integration в проекте используется облачный сервис GitHub Actions.
Для него описана последовательность команд (workflow), которая будет выполняться после события push в репозиторий.

## Как запустить проект на сервере с Ubuntu

Склонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/rtxog/yamdb_final.git

```

Выполните вход на свой удаленный сервер

Установите docker на сервер:

```
sudo apt install docker.io
```

Установите docker-compose на сервер:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Запустите docker-compose:

```
docker-compose up -d --build
```

Соберите файлы статики, и запустите миграции командами:

```
docker-compose exec web python3 manage.py makemigrations
```
```
docker-compose exec web python3 manage.py migrate
```
```
docker-compose exec web python3 manage.py collectstatic --no-input
```

Создайте суперпользователя командой:

```
docker-compose exec web python3 manage.py createsuperuser
```

Команда по загрузке файла fixtures в БД
```
docker-compose exec web python3 manage.py dumpdata > fixtures.json
```

Остановить можно командой:

```
docker-compose down -v
```
