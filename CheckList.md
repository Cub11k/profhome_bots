<img src="https://sun9-85.userapi.com/9ox9zxBLEh_CP1RjcVYzvnT0r0e6gdLlJpExTA/ysWI51O5hKY.jpg" width=1000 alt="P R O F H O M E">

# CheckList for Telegram Bots

## Functional

### Roles :scroll:

- `None` - used `/start`, save just to have `username` and `tg_id` in database
- `Team/Group/Player/etc` - registered user :detective:
- `Admin/Warden/Animator/etc` - organizer/animator/etc :policeman:
- `God` - creator and admins/managers or organizers/animators/etc :prince:
---

### Permissions management :shield:

Can be implemented via custom filters or decorators

**Three types of restrictions:**

- Anyone except banned users - to prevent saving them in database :no_entry:
- Anyone with specific `role` :man_in_tuxedo:
- Anyone who is higher than `role` :prince:
---

### Preprocessing messages before handlers :electric_plug:

Can be implemented via middlewares

- [**Logging**](#logging-loudspeaker)
- `Antispam` `OPTIONAL`
- `Autorespond` `OPTIONAL`
---

### Input checkers :ballot_box_with_check:

Can be implemented via custom filters or middlewares

- **Always prevent possible harming input for users, even from yourself**
- `message.{field}` `is None`
- `message.{field}` `is not None`
- `message.{field}` `is numeric`
- `message.{field}` `equal to` / `starts with` / `ends with` / `contains` / `in`

## Config :clipboard:

- Bot Token - `DO NOT WRITE TOKEN IN SOURCE CODE`, use `ENVIRONMENT VARIABLES` and `os.getenv()` instead
- Creator info
- Bot message texts - `should be structured via classes`
  - Messages for everyone
    - Welcome
    - Registration
    - Rules
  - Event specific messages
  - Messages for specific `role`
    - Help
  - Warnings
  - Errors

## Database :file_folder:

`peewee` is a great choice

- Easy to make requests
- Easy to create data models
- Supports `postgreSQL`, `mySQL` and `sqlite3`

But you can use any other, or even pure SQL

`Heroku` supports `postgreSQL` and `Redis`

## Requirements :books:

You should use `>=version`

- `certifi`
- `idna`
- `pip`
- `requests`
- `setuptools`
- `six`
- `urllib3`
- Your telegramAPI lib (`aiogram`, `PyTelegramAPI`, etc.)
- `peewee` or other library for db
- Drivers for db (for example `py-postgresql` and `psycopg2`)

## Logging :loudspeaker:

- `EVERY` message / command / callback / etc. that comes to your bot
- `EVERY` message / button / keyboard / interaction with db / etc. that comes from your bot

## Final testing

- Check `EVERY` command / callback from each `Role`
- Use help of at least 3-5 people as common users to check if db is not corrupted while multitasking

## Others :moyai:

- **Request `LiveLocation` to find anyone in case of emergency / lost team**
- **Use synchronous version if applicable - makes logic easier + fewer problems with simultaneous requests from users**
- **Split by files for readability using classes**
- **Always wrap requests to `API` and `db` with `try except`**
- **No manual changes in database, only via bot commands / buttons**