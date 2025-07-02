# YAJ & Mercari Discord Bot

When run, this bot will periodically check Yahoo Auctions and Mercari for user-supplied keywords, alerting the user whenever a new matching item is listed.

This project is loosely based on the [Yahoo Auction and Mercari Discord Bot](https://github.com/vlourme/yahoo-auction-alert-discord-bot) by vlourme - however, the bot has been re-written using discord.py, and various functionality has been added (and removed).

## Installation

This project is compatible with Python 3.8 and above, and has only been tested on Linux.

First, set up a virtual environment for the project:

```bash
python3 -m venv .venv
```

Then, activate the new venv:

```bash
source venv/bin/activate
```

Next, install the required packages with pip:

```bash
pip install -r requirements.txt
```

### Setting Up the Environment Variables

Create a `.env` file in the root directory of the project. This file will store the Discord token and configuration parameters. The `.env` file should look something like this:

```bash
BOT_TOKEN=your-discord-token
CHECK_INTERVAL=60
ENABLE_YAHOO_AUCTION=true
ENABLE_MERCARI=true
```

Replace `your-discord-token` with the actual Discord bot token. The unit of `CHECK_INTERVAL` is seconds, so 60 = 60 seconds.

## Running the Bot

You can start the bot by running the `main.py` script.

```bash
python main.py
```

The bot should now be running and scanning Yahoo Auction and Mercari for new articles.

### Bot Commands

To list current alerts, register a new alert, or delete existing alerts, bot commands can be used within Discord.

Bot commands are as follows:

- register - register a new alert
- unregister - unregister an alert
- alerts - view all configured alerts

## Important Notes

1. This bot relies on ZenMarket as an API to fetch items. Any changes to ZenMarket could break this bot.

2. Keep your Discord token secure - never share it with anyone.

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE](LICENSE) file for details.