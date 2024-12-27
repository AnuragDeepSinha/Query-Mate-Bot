import telebot

API_KEY = "7820245598:AAHRzq3AWP0JvsjKW9LBEVVvYZ1kWdWWlV0"

bot = telebot.TeleBot(API_KEY)

# Predefined FAQs for Query Mate
faq = {
    "What services does Query Mate offer?": "Query Mate offers backend development, cloud infrastructure management, custom software solutions, and IT consulting services.",
    "What industries does Query Mate serve?": "We specialize in serving industries such as finance, e-commerce, healthcare, logistics, and education with tailored digital solutions.",
    "Can Query Mate help with legacy system modernization?": "Yes, we help businesses modernize their legacy systems by making them scalable, secure, and performance-optimized for current demands.",
    "What is your approach to project management?": "We follow agile methodologies to ensure iterative progress, quick delivery, flexibility, and close collaboration with stakeholders for successful project completion.",
    "How does Query Mate ensure data security?": "We implement best practices for data security, including encryption, multi-factor authentication, secure data storage, and regular vulnerability testing.",
    "Do you provide cloud services?": "Yes, Query Mate provides cloud solutions, including infrastructure setup, scaling, management, and optimization on platforms like AWS, Google Cloud, and Microsoft Azure.",
    "Can Query Mate build a custom API for my project?": "Yes, we specialize in designing secure and scalable custom APIs to meet the specific needs of your business operations.",
    "How do you handle project modifications or feature enhancements?": "We approach project modifications by refactoring existing code, adding new features, and ensuring smooth integration without disrupting current operations.",
    "What technologies do you specialize in?": "We specialize in technologies like Node.js, Python (Django, Flask), Java, Ruby on Rails, React, and databases like MySQL, PostgreSQL, and MongoDB.",
    "How can I get in touch with Query Mate?": "You can contact us via email at support@querymate.com, phone at +1234567890, or visit our website at www.querymate.com.",
    "What is your pricing model?": "We offer flexible pricing depending on the project's scope, complexity, and duration. We work with both fixed-rate and hourly pricing models.",
    "Does Query Mate offer ongoing maintenance and support?": "Yes, we offer ongoing maintenance and support services to keep your systems running smoothly and up-to-date with the latest technologies."
}

# List of commands
commands = {
    "/start": "Start interaction with the bot.",
    "/help": "List available commands and FAQs.",
    "/faq": "View frequently asked questions.",
    "/contact": "Get contact information.",
    "/projects": "Learn about the projects we've worked on and how we can help.",
    "/modifications": "Learn how we can assist with modifications to your existing projects."
}

# Function to handle /start command
@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = (
        "Welcome to Query Mate! We're here to provide innovative backend solutions and help you achieve your business goals.\n\n"
        "Use /help to see available commands."
    )
    bot.reply_to(message, welcome_message)

# Function to handle /help command
@bot.message_handler(commands=['help'])
def help(message):
    help_text = "Here are the available commands:\n"
    for cmd, desc in commands.items():
        help_text += f"{cmd} - {desc}\n"
    bot.reply_to(message, help_text)

# Function to handle /faq command
@bot.message_handler(commands=['faq'])
def faq_command(message):
    faq_text = "Here are some frequently asked questions about Query Mate:\n"
    for question in faq.keys():
        faq_text += f"- {question}\n"
    faq_text += "\nReply with the question to get an answer."
    bot.reply_to(message, faq_text)

# Function to handle /contact command
@bot.message_handler(commands=['contact'])
def contact_command(message):
    contact_info = (
        "You can reach us at:\n"
        "- Email: querymate@gmail.com\n"
        "- Phone: +1324659087\n"
        "- Website: www.querymate.com"
    )
    bot.reply_to(message, contact_info)

# Function to handle /projects command
@bot.message_handler(commands=['projects'])
def projects_command(message):
    projects_info = (
        "Query Mate has worked on several impactful projects, including:\n"
        "- Backend solutions for e-commerce platforms\n"
        "- Cloud infrastructure management for fintech companies\n"
        "- Custom API development for logistics and supply chain management\n"
        "- Legacy system modernization for healthcare providers\n"
        "Contact us to discuss how we can help with your project!"
    )
    bot.reply_to(message, projects_info)

# Function to handle /modifications command
@bot.message_handler(commands=['modifications'])
def modifications_command(message):
    modifications_info = (
        "Query Mate helps businesses with modifications to existing systems, including:\n"
        "- Code refactoring for performance optimization\n"
        "- Adding new features to enhance business operations\n"
        "- Upgrading legacy systems to newer technologies\n"
        "- Cloud infrastructure scaling and optimization\n"
        "Reach out to us to get your systems updated with the latest features!"
    )
    bot.reply_to(message, modifications_info)

# Function to handle FAQs
@bot.message_handler(func=lambda message: message.text in faq)
def handle_faq(message):
    response = faq.get(message.text, "I'm not sure about that. Please contact support for more details.")
    bot.reply_to(message, response)

# Function to handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    reply_text = (
        "Thank you for your message. If you have a specific query, "
        "please use one of the available commands or ask an FAQ."
    )
    bot.reply_to(message, reply_text)

# Main function to run the bot
if __name__ == "__main__":
    print("Bot is up and running...")
    bot.polling()
