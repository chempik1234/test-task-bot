## Что делает?

Получает из БД случайную вакансию (ещё не опубликованную) и публикует,
по расписанию или по нажатию кнопки.

Публикация пока только в телеграм.

## Как запустить?

1. Создать `./config/.env` и `./config/template.txt` на основе примеров в той же папке.
2. В папке с проектом выполнить:

```bash
make upd
```

## Шаблон сообщения с вакансией

| Название поля   | Назначение                         |
|-----------------|------------------------------------|
| `{title}`       | Должность (до 50 символов)         |
| `{company}`     | Название компании (до 50 символов) |
| `{description}` | Описание (неограниченная длина)    |

### Пример:

```txt
🏙 {title}
Компания: {company}

{description}

Будем рады видеть отклики!
```

## Команды makefile

* `make up` - `docker compose up -d`
* `make upd` - `docker compose up -d --build`
* `make updbot` - `docker compose -f ./docker/docker-compose.yaml up -d --build bot1`
* `make down` - `docker compose down`
* `make deldb` - удалить том с БД
* `make freezeb` - `pip freeze` для requirements бота
* `make freezea` - `pip freeze` для requirements админки
* `make mig` - создать миграции (в админке)
* `logsbot` - логи бота
* `logsadmin` - логи админки
* `restart ARGS="admin db"` - рестарт сервисов, указанных в args
