import io
import logging
import asyncio
import traceback
import html
import json
from datetime import datetime

import telegram
from telegram import (
    Update,
    User,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    AIORateLimiter,
    filters
)
from telegram.constants import ParseMode, ChatAction

import config
import database

import base64

db = database.Database()
logger = logging.getLogger(__name__)

HELP_MESSAGE = """Commands:
⚪ /start – To start using the bot
⚪ /menu – To See Main Menu
⚪ /profile – About Your Stutes
⚪ /withdraw – To withdraw your mony
⚪ /createAd– To create new Ad for TG channals
⚪ /addchannel – To Add your channel
⚪ /tasks – To create your task
⚪ /setting – set your profile

"""

async def handle_contact(update: Update, context: CallbackContext):
    # Get the contact information from the message
    contact = update.message.contact
    if contact:
        phone_number = contact.phone_number
        await update.message.reply_text(f"Thanks! Your phone number is: {phone_number}")
    else:
        await update.message.reply_text("No contact information received.")

async def register_user_if_not_exists(update: Update, context: CallbackContext, user: User):
    if not db.check_if_user_exists(user.id):
        db.add_new_user(
            user.id,
            update.message.chat_id,
            username=user.username,
            first_name=user.first_name,
            last_name= user.last_name,
            phonenumber= update.message.contact,
            balance= 0,
            channels= "None",
            posts= "None",
            totalwithdraw= 0
        )


async def error_handle(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    try:
        # collect error message
        tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
        tb_string = "".join(tb_list)
        update_str = update.to_dict() if isinstance(update, Update) else str(update)
        message = (
            f"An exception was raised while handling an update\n"
            f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
            "</pre>\n\n"
            f"<pre>{html.escape(tb_string)}</pre>"
        )

        # split text into multiple messages due to 4096 character limit
        for message_chunk in split_text_into_chunks(message, 4096):
            try:
                await context.bot.send_message(update.effective_chat.id, message_chunk, parse_mode=ParseMode.HTML)
            except telegram.error.BadRequest:
                # answer has invalid characters, so we send it without parse_mode
                await context.bot.send_message(update.effective_chat.id, message_chunk)
    except:
        await context.bot.send_message(update.effective_chat.id, "Some error in error handler")

async def terms_of_service_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())

async def settings_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())

async def create_task_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())


async def addchannel_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())


async def createAd_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())

    text = 'choose channel type'
    text += '\n\n'

    channel_type_btn = []

    for type_btn in config.models["available_text_models"]:
        title = config.models[type_btn]
        channel_type_btn.append(
            InlineKeyboardButton(title, callback_data=f"set_settings|{type_btn}")
        )
    reply_markup = InlineKeyboardMarkup([channel_type_btn])

    return text, reply_markup

async def manual_withdraw_handel(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())

    u = str(u)
    try:
        amount = int(message.text)
        bal = int(db.get_user_attribute.balance)
    except:
        await update.message.reply_text(
                u, "*❗️ Invalid amount send positive number and without decimals. Numbers only*", parse_mode="markdown")
        return withdraw_handle()

    if amount > float(bal):
        await update.message.reply_text(u, "❗️ *Amount is bigger than your balance*",parse_mode="markdown")
        return withdraw_handle()

    Payer = "@Eyosafitelias"
    username = str(Bot.info().username)
    #u = str(u)
    amount = str(amount)
    currency = "ETB"  # Enter your currency instead of None
    balance = bal-float(amount)
    name = db.get_user_attribute.username

    if Payer != "None":
        await update.message.reply_text(chat_id=Payer,
            text=f"""✅ New Withdrawal
            User Name: {name}
            Amount   : {amount}
            Number   : {number}""",
            parse_mode="html"
            )
        await update.message.reply_text(f'''⏳ Withdraw Prosesing 
            You will get your mony soon in tellebirr.
            ⚠️The withdrawal day is Monday,Wednesday and Friday only
            ⚠️And when you get your withdrawal dont forget to post in our 
            public group''',parse_mode="markdown")


async def withdraw_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())

    wallet = db.get_user_attribute.phone
    balance = db.get_user_attribute.balance

    Mini_Withdraw = "250"

    if wallet == None:
        text = "First Share your telebirr account phone number"
        reply_markup = InlineKeyboardMarkup("Share Phone", callback_data=f"set_settings|")

        return text, reply_markup
    if balance >= 250:
        share_amount = "<b>⚠️Enter amount to withdraw</b>"
        return manual_withdraw_handel()
        

    else:
        lessAmount = f"<i>❌ Your balance is low you should have at least "+Mini_Withdraw+" (ETB) to Withdraw</i>"
        await update.message.reply_text(lessAmount)
        return withdraw_handle()




async def unsupport_message_handle(update: Update, context: CallbackContext, message=None):
    error_text = f"I don't know how to read files, videos or picture in normal mode."
    logger.error(error_text)
    await update.message.reply_text(error_text)
    return

async def profile_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())

    user_name = db.get_user_attribute.username
    your_channel = db.get_user_attribute.channels
    balance = db.get_user_attribute.balance
    stutes = db.get_user_attribute.stutes
    wallet = db.get_user_attribute.phone

    Profile = """
    🙅 <b>User</b>: {user_name}
    💳 <b>Wallet</b>: <code>{wallet}</code>
    💵 <b>Balance</b>: {balance} <i>ETB</i>
    📊 <b>Stutes</b>: {stutes}
    🔰 <b>Channels<b/>: {your_channel}
    """
    await update.message.reply_text(Profile, parse_mode=ParseMode.HTML)


async def help_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id
    db.set_user_attribute(user_id, "last_interaction", datetime.now())
    await update.message.reply_text(HELP_MESSAGE, parse_mode=ParseMode.HTML)

async def start_handle(update: Update, context: CallbackContext):
    await register_user_if_not_exists(update, context, update.message.from_user)
    user_id = update.message.from_user.id

    reply_text = "Hello We Are <b>Nothing</b> We Interconnect The Addvertisers To Channel Owners 🤖\n\n"
    reply_text += HELP_MESSAGE


    #button = KeyboardButton("Share Contact", request_contact=True)
    #keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True)
    await update.message.reply_text(reply_text, parse_mode="markdown")

async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("/start", "Star"),
        BotCommand("/menu", "Main Menu"),
        BotCommand("/profile", "See about yourselfe"),
        BotCommand("/withdraw", "Ask For Withdraw"),
        BotCommand("/createad", "Create Ad For T.G Channels"),
        BotCommand("/addchannel", "Add your Channels"),
        BotCommand("/tasks", "Create your own task"),
        BotCommand("/settings", "Add your Channels"),
    ])

def run_bot() -> None:
    application = (
        ApplicationBuilder()
        .token(config.telegram_token)
        .concurrent_updates(True)
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .post_init(post_init)
        .build()
    )

    # add handlers
    user_filter = filters.ALL
    if len(config.allowed_telegram_usernames) > 0:
        usernames = [x for x in config.allowed_telegram_usernames if isinstance(x, str)]
        any_ids = [x for x in config.allowed_telegram_usernames if isinstance(x, int)]
        user_ids = [x for x in any_ids if x > 0]
        group_ids = [x for x in any_ids if x < 0]
        user_filter = filters.User(username=usernames) | filters.User(user_id=user_ids) | filters.Chat(chat_id=group_ids)

    application.add_handler(CommandHandler("start", start_handle, filters=user_filter))
    application.add_handler(CommandHandler("menu", help_handle, filters=user_filter))
    application.add_handler(CommandHandler("profile", profile_handle, filters=user_filter))

    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND & user_filter, unsupport_message_handle))
    application.add_handler(MessageHandler(filters.VIDEO & ~filters.COMMAND & user_filter, unsupport_message_handle))
    application.add_handler(MessageHandler(filters.Document.ALL & ~filters.COMMAND & user_filter, unsupport_message_handle))
    application.add_handler(CommandHandler("withdraw", withdraw_handle, filters=user_filter))
    application.add_handler(CommandHandler("createAd", createAd_handle, filters=user_filter))
    application.add_handler(CommandHandler("addchannel", addchannel_handle, filters=user_filter))

    application.add_handler(MessageHandler(filters.VOICE & user_filter, unsupport_message_handle))

    application.add_handler(CommandHandler("tasks", create_task_handle, filters=user_filter))

    application.add_handler(CommandHandler("settings", settings_handle, filters=user_filter))

    application.add_handler(CommandHandler("Termsofsevice", terms_of_service_handle, filters=user_filter))

    application.add_error_handler(error_handle)

    # start the bot
    application.run_polling()


if __name__ == "__main__":
    run_bot()