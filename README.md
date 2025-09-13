## Что делает?

Получает из БД случайную вакансию (ещё не опубликованную) и публикует,
по расписанию или по нажатию кнопки.

Публикация пока только в телеграм.

## Как запустить?

1. Создать на основе примеров в той же папке:
   1. `./config/.env`
   2. `./config/templates/template.jinja`
   3. `./config/config.json` и `./config/debug_config.json`
2. В папке с проектом выполнить:

```bash
make upd
```

## Команды makefile

* `make up` - `docker compose up -d`
* `make upd` - `docker compose up -d --build`
* `make updbot` - `docker compose -f ./docker/docker-compose.yaml up -d --build bot1`
* `make down` - `docker compose down`
* `make deldb` - удалить том с БД
* `make freezeb` - `pip freeze` для requirements бота
* `logsbot` - логи бота
* `restart ARGS="bot1 db"` - рестарт сервисов, указанных в args
