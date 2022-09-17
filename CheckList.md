<img src="https://sun9-85.userapi.com/9ox9zxBLEh_CP1RjcVYzvnT0r0e6gdLlJpExTA/ysWI51O5hKY.jpg" width=1000>

<a name="checklist"/>

# CheckList for Telegram Bots

<a name="functional"/>

## Functional

<a name="roles"/>

### Roles :scroll:

- `None` - used `/start`, save just to have `username` and `tg_id` in database
- `Team/Group/Player/etc` - registered user :detective:
- `Admin/Warden/Animator/etc` - organizer/animator/etc :policeman:
- `God` - creator and admins/managers or organizers/animators/etc :prince:

<a name="permissions"/>

### Permissions management :shield:

Can be implemented via custom filters or decorators

**Three types of restrictions:**

- Anyone except banned users - to prevent saving them in database :no_entry:
- Anyone with specific `role` :man_in_tuxedo:
- Anyone who is higher than `role` :prince:

<a name="preprocessing"/>

### Preprocessing messages before handlers :electric_plug:

Can be implemented via middlewares

- `Antispam` `OPTIONAL`
- `Logging` see [Logging](#logging)
- `Auto respond` `OPTIONAL`

<a name="checkers"/>

### Input checkers :ballot_box_with_check:

Can be implemented via custom filters or middlewares

- `message.{field}` `is None`
- `message.{field}` `is not None`
- `message.{field}` `equal to` / `starts with` / `ends with` / `contains`

<a name="config"/>

## Config

<a name="database"/>

## Database

<a name="requirements"/>

## Requirements

<a name="pytelegrambotapi"/>

### PyTelegramBotAPI

<a name="mysql"/>

### MySQL

<a name="postgresql"/>

### PostgresQL

<a name="logging"/>

## Logging

<a name="special"/>

## Special

- **Use synchronous version if possible - makes logic easier + fewer problems with simultaneous requests from users**
- **Split by files for readability, using `pass_bot` parameter**
- **No manual changes in database, only via bot commands / buttons**
