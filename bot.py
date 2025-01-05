import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# OpenAI API Key set koro
openai.api_key = "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"

# Website URL (Replace with your actual website's search URL)
BASE_URL = "https://mhbd.Xyz/search?q="

# OpenAI GPT Response Generate Korar Function
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # "gpt-4" use korte chaile change koro
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Start Command Handle Kora
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Ami tomar ChatGPT-powered bot. Tomar kono question thakle jiggesh koro!")

# Group Message Handle Kora
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()

    # Check if the message contains movie-related keywords
    if "movie" in user_message or "film" in user_message or "tv show" in user_message:
        # Extract the requested movie/show name
        requested_title = user_message.replace("movie", "").replace("film", "").replace("tv show", "").strip()
        if requested_title:
            # Generate the movie link
            movie_link = f"{BASE_URL}{requested_title.replace(' ', '+')}"
            update.message.reply_text(f"Tomar requested movie/TV show er jonno visit koro: {movie_link}")
        else:
            update.message.reply_text("Please specify the movie or TV show name.")
    else:
        # General ChatGPT Response
        bot_response = generate_response(user_message)
        update.message.reply_text(bot_response)

# Main Function
def main():
    # Telegram Bot API Token
    TELEGRAM_API_TOKEN = "7039335183:AAHdML6Xry7-fqyaISdOpp4mE52gRgqeo-Q"

    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start))

    # Group Message Handler
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
