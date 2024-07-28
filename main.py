from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
load_dotenv()
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}! Welcome to my CV bot. Use /help to see available commands.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Available commands:
/skills - View my key skills
/experience - See my work experience
/education - Check my educational background
/projects - View my notable projects
/contact - Get my contact information
    """
    await update.message.reply_text(help_text)

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    skills_text = """
My Key Skills:
- Python Development
- Chatbot Creation
- Machine Learning
- Data Analysis
- Web Development
    """
    await update.message.reply_text(skills_text)

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    experience_text = """
Work Experience:
1. Senior Python Developer at TechCorp (2020-Present)
2. Machine Learning Engineer at AI Solutions (2018-2020)
3. Junior Developer at WebTech (2016-2018)
    """
    await update.message.reply_text(experience_text)

async def education(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    education_text = """
Education:
- MSc in Computer Science, Tech University (2016)
- BSc in Software Engineering, Code College (2014)
    """
    await update.message.reply_text(education_text)

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    projects_text = """
Notable Projects:
1. Developed an AI-powered chatbot for customer service
2. Created a machine learning model for stock price prediction
3. Built a web application for task management using Django
    """
    await update.message.reply_text(projects_text)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact_text = """
Contact Information:
Email: your.email@example.com
LinkedIn: linkedin.com/in/yourprofile
GitHub: github.com/yourusername
    """
    await update.message.reply_text(contact_text)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("skills", skills))
app.add_handler(CommandHandler("experience", experience))
app.add_handler(CommandHandler("education", education))
app.add_handler(CommandHandler("projects", projects))
app.add_handler(CommandHandler("contact", contact))

print('Bot is running...')
app.run_polling()
