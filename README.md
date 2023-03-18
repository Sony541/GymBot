# Gym Bot

## Usage
To make this bot work for you, you will need to create `Config.py` file with your bot's security token (obtained from https://t.me/BotFather).

Example of `Config.py`:

```python
token = "MySecure12345Token"
```

## Docker-compose

Just add following lines to your `docker-compose.yml` file:

```
version: '3.6'
services:
  tg_robot:
    build: ../AlphaTGRobot/             # Path to this package
    environment:
      TG_ROBOT_TOKEN: "YOUR_SECRET"     # Get it from @BotFather bot in Telegram
    volumes:
      - "$ALPHABOX_RUNTIME_DIRECTORY/tg_robot:/usr/src/app/database"
```
