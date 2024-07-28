# Telegram CV Bot

A simple Telegram bot that serves as an interactive CV/resume.

## Quick Start

1. Clone the repository:
   git clone https://github.com/yourusername/telegram-cv-bot.git
   cd telegram-cv-bot

2. Create virtual environment with `python -m venv venv` 

2. Install requirements:

   `pip install python-telegram-bot`

   `pip install python-dotenv`

3. Add your Telegram Bot Token to `.env` file (create it manually):
   BOT_TOKEN = 'your_bot_token_here'

4. [Optional] Update personal information in `maing.py`.

5. Run the bot:
   python main.py

## Commands

- `/start`: Welcome message
- `/help`: List all commands
- `/skills`: View key skills
- `/experience`: See work experience
- `/education`: Check education
- `/projects`: View projects
- `/contact`: Get contact info

## License

MIT