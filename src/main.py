import os
import random
import string
import json
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters
)

TOKEN = "8004240677:AAF8SUKjOA5cZ8Z92XGyT6N2yRppxPnS3Ns"

# Сообщения
START_MESSAGE = """🔐 *Генератор паролей*

Выберите действие:
- Сгенерировать пароль
- Мои сохранённые пароли
- Справка"""

HELP_MESSAGE = """📚 *Справка*

*Как пользоваться ботом:*
1. Нажмите "Сгенерировать пароль"
2. Укажите длину пароля
3. Выберите, нужны ли спецсимволы
4. Нажмите "Сгенерировать"
5. Сохраните пароль с описанием (по желанию)

*Советы по безопасности:*
- Используйте пароли длиной не менее 12 символов
- Включайте спецсимволы для надёжности
- Не используйте один пароль для разных сервисов
- Регулярно меняйте важные пароли"""

# Настройки по умолчанию
DEFAULT_SETTINGS = {
    'length': 12,
    'use_special': True
}

# Файл для хранения паролей
PASSWORDS_FILE = "bot/user_password.json"

def load_passwords():
    if not os.path.exists(PASSWORDS_FILE):
        return {}
    with open(PASSWORDS_FILE, 'r') as f:
        return json.load(f)

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as f:
        json.dump(passwords, f, indent=2)

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["Сгенерировать пароль"],
        ["Мои сохранённые пароли"],
        ["Справка"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        START_MESSAGE,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(HELP_MESSAGE, parse_mode='Markdown')

async def generate_password_menu(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    context.user_data.setdefault('settings', DEFAULT_SETTINGS.copy())
    
    keyboard = [
        ["Изменить длину"],
        ["Вкл спецсимволы", "Выкл спецсимволы"],
        ["Сгенерировать"],
        ["Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    settings = context.user_data['settings']
    message = (
        f"⚙ *Текущие настройки:*\n"
        f"• Длина: {settings['length']} символов\n"
        f"• Спецсимволы: {'включены' if settings['use_special'] else 'отключены'}\n\n"
        "Измените настройки или нажмите *Сгенерировать*"
    )
    
    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def generate_new_password(update: Update, context: CallbackContext) -> None:
    settings = context.user_data.get('settings', DEFAULT_SETTINGS)
    characters = string.ascii_letters + string.digits
    if settings['use_special']:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(settings['length']))
    context.user_data['last_password'] = password
    
    keyboard = [
        ["Сохранить пароль"],
        ["Сгенерировать новый"],
        ["Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # Форматируем пароль для легкого копирования
    formatted_password = password.replace('`', '\\`')  # Экранируем обратные кавычки
    await update.message.reply_text(
        f"🔐 *Ваш пароль:*\n\n`{formatted_password}`\n\n"
        "Вы можете сохранить его или сгенерировать новый",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def handle_password_settings(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    user_id = str(update.message.from_user.id)
    
    if text == "Назад":
        await start(update, context)
        return
    
    if text == "Изменить длину":
        await update.message.reply_text(
            "Введите длину пароля (от 4 до 50 символов):",
            reply_markup=ReplyKeyboardMarkup([["Назад"]], resize_keyboard=True)
        )
        context.user_data['awaiting_length'] = True
        return
    
    if context.user_data.get('awaiting_length', False):
        try:
            length = int(text)
            if length < 4:
                await update.message.reply_text("Минимальная длина - 4 символа")
                return
            if length > 50:
                await update.message.reply_text("Максимальная длина - 50 символов")
                return
            
            context.user_data['settings']['length'] = length
            context.user_data['awaiting_length'] = False
            await update.message.reply_text(f"✅ Длина установлена: {length} символов")
            await generate_password_menu(update, context)
            return
        except ValueError:
            await update.message.reply_text("Пожалуйста, введите число (например: 12)")
            return
    
    if text in ["Вкл спецсимволы", "Выкл спецсимволы"]:
        context.user_data['settings']['use_special'] = text == "Вкл спецсимволы"
        status = "включены" if text == "Вкл спецсимволы" else "отключены"
        await update.message.reply_text(f"✅ Спецсимволы {status}")
        await generate_password_menu(update, context)
        return
    
    if text == "Сгенерировать":
        await generate_new_password(update, context)
        return
    
    if text == "Сгенерировать новый":
        await generate_new_password(update, context)
        return
    
    if text == "Сохранить пароль":
        await update.message.reply_text(
            "Введите описание для этого пароля (например: 'Пароль для почты'):",
            reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True)
        )
        context.user_data['awaiting_description'] = True
        return
    
    if context.user_data.get('awaiting_description', False):
        if text == "Отмена":
            context.user_data['awaiting_description'] = False
            await generate_password_menu(update, context)
            return
        
        description = text
        password = context.user_data.get('last_password')
        
        if not password:
            await update.message.reply_text("Ошибка: пароль не найден")
            return
        
        passwords = load_passwords()
        if user_id not in passwords:
            passwords[user_id] = []
        
        passwords[user_id].append({
            "description": description,
            "password": password,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_passwords(passwords)
        
        context.user_data['awaiting_description'] = False
        await update.message.reply_text(
            f"✅ Пароль сохранён с описанием: '{description}'",
            reply_markup=ReplyKeyboardMarkup([["Назад"]], resize_keyboard=True)
        )
        return
    
    if text == "Мои сохранённые пароли":
        passwords = load_passwords().get(user_id, [])
        
        if not passwords:
            await update.message.reply_text(
                "У вас пока нет сохранённых паролей",
                reply_markup=ReplyKeyboardMarkup([["Назад"]], resize_keyboard=True)
            )
            return
        
        message = "🔑 *Ваши сохранённые пароли:*\n\n"
        for idx, item in enumerate(passwords, 1):
            # Экранируем специальные символы для Markdown
            safe_password = item['password'].replace('`', '\\`')
            message += (
                f"{idx}. *{item['description']}*\n"
                f"Пароль: `{safe_password}`\n"
                f"Создан: {item['date']}\n\n"
            )
        
        await update.message.reply_text(
            message,
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup([["Назад"]], resize_keyboard=True)
        )
        return
    
    await update.message.reply_text("Пожалуйста, используйте кнопки меню")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.Regex("^Сгенерировать пароль$"), generate_password_menu))
    app.add_handler(MessageHandler(filters.Regex("^Мои сохранённые пароли$"), handle_password_settings))
    app.add_handler(MessageHandler(filters.Regex("^Справка$"), help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_password_settings))
    
    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()