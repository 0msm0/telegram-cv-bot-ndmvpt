# Telegram CV Bot

A simple Telegram bot that serves as an interactive CV/resume.

## Quick Start

1. Download or Clone the repository:
   git clone https://github.com/0msm0/telegram-cv-bot-ndmvpt.git
   cd telegram-cv-bot

2. Create virtual environment with `python -m venv venv`

3. Activate venv with `venv\Scripts\activate` from root folder

4. Install requirements:

   `pip install python-telegram-bot`

   `pip install python-dotenv`

5. Create a bot token from https://web.telegram.org/k/#@BotFather 

6. Add your Telegram Bot Token to `.env` file (create file manually):
   BOT_TOKEN = 'your_bot_token_here'

7. [Optional] Update personal information in `main.py`.

8. Run the bot:
   python main.py

## Working Commands

- `/start`: Welcome message
- `/help`: List all commands
- `/skills`: View key skills
- `/experience`: See work experience
- `/education`: Check education
- `/projects`: View projects
- `/contact`: Get contact info

## License

MIT