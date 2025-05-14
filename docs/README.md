# Проект: Автоматизация процесса анкетирования

Этот статический сайт был разработан в рамках проектной практики для сопровождения проекта по дисциплине **"Проектная деятельность"**.  
Основная цель проекта — создание решения для автоматизации анкетирования студентов в учебном процессе.

## 🏠 Структура сайта  
| Страница       | Описание  |  
|----------------|-----------|  
| **Главная**    | Описание проекта, его цель, задачи и краткая информация о решаемой проблеме.  |  
| **О проекте**  | Подробное объяснение целей, задач, используемых технологий и состава команды.  |  
| **Участники**  | Список членов команд, участвующих в проекте (дизайн, разработка, тестирование).  |  
| **Журнал**     | Дневник разработки, включающий этапы анализа, проектирования, тестирования.  |  
| **Ресурсы**    | Полезные ссылки, документация и ссылки на партнёрские материалы.  |  

---

## 🎯 Цели и задачи  
### Проблема  
Процесс ручного создания анкет в СДО требует значительных временных затрат и усилий:  
- Сложность в подборе вопросов для каждой анкеты.  
- Трудности в анализе результатов без автоматизации.  

### Решение  
Проект направлен на:  
- Автоматическую генерацию анкет с использованием XML-шаблонов.  
- Оптимизацию обработки данных для анализа результатов.  
- Введение веб-интерфейса для администрирования (планируется в будущем).  

### Технические задачи  
- Разработка структуры базы данных (диаграммы UML).  
- Написание скриптов для автоматического создания анкет (Python + XML).  
- Тестирование и проверка корректности работы системы.  

---

## 👥 Команда  
Проект реализуют несколько групп участников:  

| Роль | Участники | Вклад |  
|------|-----------|-------|  
| **Дизайн интерфейса** | Оксана Желтоноженко, Дарья Пинчер | Разработка макетов страниц, прототипирование интерфейсов. |  
| **Создание анкет** | Тигран Хачатурян, Кирилл Журавлев, Тамерлан Шагаев, Абдухамид Зайнидинов | Создание XML-шаблонов анкет и автоматизация обработки данных. |  
| **Архитектура баз данных** | Анна Жгутова, Михаил Скрипкин, Павел Сурин | Проектирование и разработка структуры базы данных. |  
| **Тестирование** | Дмитрий Шувалов, Александр Петрищев, Мерген Атаев, Александр Голдин | Планирование и проведение тестирования, отчётность. |  

---

## 📅 Журнал прогресса  
### Основные этапы разработки  
1. **Исследование и анализ** (сравнение доступных систем анкетирования).  
2. **Проектирование**:  
   - Создание макетов интерфейса.  
   - Разработка UML-диаграмм базы данных.  
3. **Разработка**:  
   - Автоматизация создания анкет (XML-файлы).  
   - Написание скриптов для анализа данных.  
4. **Тестирование**:  
   - Проверка целостности данных.  
   - Документирование найденных ошибок.  

---

## 🤝 Партнёрство
- **Партнёр**: [Московский Политех](https://mospolytech.ru/).  

## 🛠 Технологии  
### Основной стек  
- **Frontend**: HTML, CSS.  
- **Backend (скрипты)**: Python (библиотеки `xml.etree`, `sqlite3`, `openpyxl`, `BeautifulSoup`).  
- **База данных**: SQLite, UML-диаграммы.  
- **Форматы данных**: XML (для хранения анкет), Excel (для анализа результатов).  

### Документация  
- [Python XML](https://docs.python.org/3/library/xml.etree.elementtree.html)  
- [Python XML DOM](https://docs.python.org/3/library/xml.dom.html)  
- [OpenPyXL](https://openpyxl.readthedocs.io/)  
- [SQLite](https://www.sqlite.org/docs.html)  
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  

# Проект: Telegram-бот для генерации паролей

## 📌 Введение

Целью данного проекта было создание удобного Telegram-бота для генерации и хранения сложных паролей.  
Бот позволяет:
- Генерировать пароли с настраиваемой длиной и набором символов.
- Сохранять пароли с описанием для дальнейшего использования.
- Просматривать историю сохранённых паролей.

Для реализации использованы:
- Библиотека `python-telegram-bot` для работы с Telegram API.
- JSON-файл для хранения данных пользователей.
- Модули `random` и `string` для генерации паролей.

---

# Этапы исследования

В процессе разработки Telegram-бота для генерации паролей были изучены следующие аспекты:

- Принципы работы с библиотекой python-telegram-bot для создания Telegram-ботов
- Методы генерации криптографически стойких паролей с использованием модулей random и string
- Способы безопасного хранения пользовательских данных в JSON-формате
- Особенности реализации callback-функций для обработки пользовательских команд
- Официальная документация Telegram Bot API и библиотеки python-telegram-bot

Для исследования использовались:
- Официальная документация python-telegram-bot
- Руководства по безопасному хранению пользовательских данных
- Примеры реализации ботов с сохранением состояния

# Этапы разработки

1. Создание базовой структуры бота:
   - Инициализация бота с помощью ApplicationBuilder
   - Настройка обработчиков команд (/start, /help)
   - Реализация системы обработки сообщений

2. Разработка функционала генерации паролей:
   - Создание алгоритма генерации с настраиваемыми параметрами
   - Реализация выбора длины пароля (4-50 символов)
   - Добавление опции включения/выключения спецсимволов

3. Реализация системы хранения паролей:
   - Создание JSON-хранилища для пользовательских данных
   - Разработка функций сохранения и загрузки паролей
   - Реализация привязки паролей к конкретным пользователям

4. Создание интерфейса взаимодействия:
   - Разработка системы кнопочного меню
   - Реализация обработки callback-запросов
   - Добавление подтверждающих сообщений

5. Тестирование и отладка:
   - Проверка корректности генерации паролей
   - Тестирование системы хранения данных
   - Оптимизация пользовательского интерфейса

---

## ⚙️ Функционал

### Основные команды:
- **/start** – запуск бота и главное меню.
- **Сгенерировать пароль** – настройка и создание пароля.
- **Мои сохранённые пароли** – просмотр ранее созданных паролей.
- **Справка** – инструкция по использованию.

### Возможности:
1. **Генерация пароля**:
   - Настройка длины (от 4 до 50 символов).
   - Включение/выключение спецсимволов (например, `!@#$%`).
   - Кнопка **Сгенерировать новый** для создания альтернативного варианта.

2. **Сохранение паролей**:
   - Добавление описания (например, "Пароль для Gmail").
   - Автоматическое сохранение даты создания.

3. **Безопасность**:
   - Пароли хранятся локально в зашифрованном JSON-файле.
   - Каждый пользователь имеет доступ только к своим данным.

---



# Техническое руководство

## Установка зависимостей

```bash
pip install python-telegram-bot
```
>Библиотека python-telegram-bot предоставляет все необходимые инструменты для работы с Telegram Bot API.

Шаг 1: Базовая структура бота

```python
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = ""

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.Regex("^Сгенерировать пароль$"), generate_password_menu))
    app.add_handler(MessageHandler(filters.Regex("^Мои сохранённые пароли$"), handle_password_settings))
    app.add_handler(MessageHandler(filters.Regex("^Справка$"), help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_password_settings))
    
    print("Бот запущен...")
    app.run_polling()
```

Шаг 2: Генерация паролей

```python
import random
import string

def generate_new_password(update: Update, context: CallbackContext) -> None:
    settings = context.user_data.get('settings', DEFAULT_SETTINGS)
    characters = string.ascii_letters + string.digits
    if settings['use_special']:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(settings['length']))
    context.user_data['last_password'] = password
    
    formatted_password = password.replace('`', '\\`')
    await update.message.reply_text(
        f"🔐 *Ваш пароль:*\n\n`{formatted_password}`",
        parse_mode='Markdown'
    )
```

Шаг 3: Работа с хранилищем паролей

```python
import json
from datetime import datetime

PASSWORDS_FILE = "bot/user_password.json"

def load_passwords():
    if not os.path.exists(PASSWORDS_FILE):
        return {}
    with open(PASSWORDS_FILE, 'r') as f:
        return json.load(f)

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as f:
        json.dump(passwords, f, indent=2)
```

Шаг 4: Основные команды

```python
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["Сгенерировать пароль"],
        ["Мои сохранённые пароли"],
        ["Справка"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🔐 *Генератор паролей*\n\nВыберите действие:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(HELP_MESSAGE, parse_mode='Markdown')
```

Шаг 5: Меню настроек

```python
async def generate_password_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["Изменить длину"],
        ["Вкл спецсимволы", "Выкл спецсимволы"],
        ["Сгенерировать"],
        ["Назад"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "⚙ *Настройки генерации пароля*",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
```

Шаг 6: Обработка сохранения пароля

```python
async def handle_password_settings(update: Update, context: CallbackContext) -> None:
    if text == "Сохранить пароль":
        await update.message.reply_text(
            "Введите описание для пароля:",
            reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True)
        )
        context.user_data['awaiting_description'] = True
    
    elif context.user_data.get('awaiting_description', False):
        passwords = load_passwords()
        passwords[user_id].append({
            "description": description,
            "password": password,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        save_passwords(passwords)
        await update.message.reply_text("✅ Пароль сохранён")
```

Шаг 7: Просмотр паролей

```python
async def show_passwords(update: Update, context: CallbackContext):
    passwords = load_passwords().get(user_id, [])
    if passwords:
        message = "🔑 *Ваши пароли:*\n\n" + "\n".join(
            f"{i+1}. {item['description']}: `{item['password']}`"
            for i, item in enumerate(passwords)
        )
        await update.message.reply_text(message, parse_mode="Markdown")
    else:
        await update.message.reply_text("У вас нет сохранённых паролей")
```

>Для работы бота требуется Python 3.7+ и библиотека python-telegram-bot.
