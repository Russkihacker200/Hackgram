from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import emoji
from heart import heart_emoji
import time
import asyncio
from pyrogram.types import ChatPermissions
import requests
import re

app = Client(
    "my_accounth",
    api_id=20472471,
    api_hash="e7be3786eeafc26592aa3613bb18238a"
)

@app.on_message(filters.command("help", prefixes="") & filters.me)
def animate_f(_, message):
    animated_text = [
        "HACKGRM\n1 `снос`",
        "HACKGRAM\n1. `снос`\n2. спам`",
        "HACKGRAM\n1.`снос`\n2 `спам`\n3 `докс`",
        "HACKGRAM\n1 `снос`\n2 `спам`\n3 `докс`\n4 `парс`",
        "HACKGRAM\n1 `снос`\n2 `спам`\n3 `докс`\n4 `парс`\n5 `взлом",
        "HACKGRAM\n1 `снос`\n2 `спам`\n3 `докс`\n4 `парс`\n5 `взлом`\n6 `войс`",
        "HACKGRAM\n1 `снос`\n2 `спам`\n3 `докс`\n4 `парс`\n5 `взлом`\n6 `войс`\n7 `ддос`",
        "HACKGRAM\n1 `снос`\n2 `спам`\n3 `докс`\n4 `парс`\n5 `взлом`\n6 `войс`\n7 `ддос`\n8 `репорт`",
        "HACKGRAM\n1 `снос`\n2 `спам`\n3 `докс`\n4 `парс`\n5 `взлом`\n6 `войс`\n7 `ддос`\n8 `репорт`\n9 `.tp - анимация`",
        
       
       ]
    
    for frame in animated_text:
        message.edit(frame)
        sleep(0.8)  # Задержка между кадрами анимации

#Функция для отправки жалобы на чат
def send_report(chat_id, report_message):
    try:
        app.send_message(chat_id, report_message)
    except FloodWait as e:
        sleep(e.x)

@app.on_message(filters.command("снос", prefixes="") & filters.me)
def animate_f(_, message):
    animated_text = [
        "__search by id__",
        "__telegram id found!__",
        "__looking for violations__",
        "__looking for violations.__",
        "__looking for violations..__",
        "__looking for violations...__",
        "**found!**",
        "**insult complaint sent**",
        "**spam complaint sent**",
        "**pornographers complaint sent**",
        "**complaint personal data sent**",
        "**complaint fake account sent**",
        "**drug complaint sent**",
        "__wait for the demolition!__",
       
       ]

    chat_id = message.chat.id  # Получаем ID чата, на который отправляем жалобы


    for frame in animated_text:
        message.edit(frame)
        sleep(0.5)

    
        # Список с различными причинами жалоб
        reasons = ["оскорбления", "spam", "pornographers", "личные данные", "ненастоящий аккаунт", "наркотики"]

# Цикл для отправки жалоб на каждую причину
        for reason in reasons:
            if reason in frame:
                send_report(chat_id, "Жалоба на нарушение: " + reason)

@app.on_message(filters.command("спам", prefixes="") & filters.me)
def spam_messages(client, message):
    # Разбиваем сообщение на части, чтобы получить количество сообщений и само сообщение
    _, count, text = message.text.split(" ", 2)

    # Преобразуем количество сообщений из строки в целое число
    count = int(count)

    # Отправляем указанное количество сообщений
    for _ in range(count):
        message.reply_text(text)
        time.sleep(1)  # Добавляем задержку между сообщениями (в секундах)


bot_usernames = ["@eyeofbeholder_bot", "@fanstatbot_robot", "@UniversalSearchEasyBot", "@osintkit_bot", "@anotherLeakOSINTrobotbot", "@QuicckOSINT_bot", "@telesint_bot", "@SangMata_BOT", "@tgscan_clone_robot", "@useridinfobot",]  # Замените на фактические никнеймы ваших ботов

# Функция отправки сообщения в боты
def send_to_bots(user_id):
    for bot_username in bot_usernames:
        app.send_message(bot_username, user_id)

# Определяем функцию-обработчик для обратных сообщений от ботов
@app.on_message(filters.chat(bot_usernames) & ~filters.me)
def save_messages(client, message):
    with open("responses.txt", "a") as file:  # Открываем файл для добавления сообщений
        file.write(f"{message.chat.username}: {message.text}\n")

# Определяем функцию-обработчик для команды "докс"
@app.on_message(filters.command("докс", prefixes="") & filters.reply)
def send_to_bots_handler(client, message):
    user_id = message.reply_to_message.from_user.id
    send_to_bots(user_id)
    message.reply_text("Айди отправлены в определенные боты")

    # Отправляем вам файл с ответами из ботов в избранное
    with open("responses.txt", "rb") as file:
        app.send_document("me", file)

    for frame in animated_text:
            message.edit(frame)
            sleep(0.4)

#Обработчик команды "парс"
@app.on_message(filters.command("парс", prefixes="") & filters.me)
async def parse_chat_info(client, message):
    # Ваша анимация
    animation = [
        "__parsing chat__",
        "⬜⬜⬜⬜⬜⬜",
        "🟩⬜⬜⬜⬜⬜",
        "🟩🟩⬜⬜⬜⬜",
        "🟩🟩🟩⬜⬜⬜",
        "🟩🟩🟩🟩⬜⬜",
        "🟩🟩🟩🟩🟩⬜",
        "🟩🟩🟩🟩🟩🟩",
        "send!",
        "check your favorites"
    ]

    for frame in animation:
        await message.edit(frame)
        await asyncio.sleep(1)

    # Определяем имеющийся чат
    chat = await client.get_chat(message.chat.id)

    # Получаем информацию о всех участниках чата
    members = []
    async for member in client.get_chat_members(chat.id):
        members.append(member.user)
        
    # Записываем информацию в файл
    with open("chat_info.txt", "w", encoding="utf-8") as file:
        for member in members:
            user_id = member.id
            first_name = member.first_name
            last_name = member.last_name if member.last_name else ""
            username = member.username if member.username else ""
            is_premium = "Premium" if member.is_premium else "Not Premium"
            file.write(f"ID: {user_id}, First Name: {first_name}, Last Name: {last_name}, Username: {username}, Premium: {is_premium}\n")

    # Отправляем файл с информацией в избранное
    with open("chat_info.txt", "rb") as file:
        await app.send_document("me", file)
    for frame in animated_text:
            message.edit(frame)
            sleep(0.4)


# Обработчик команды /tp
@app.on_message(filters.command("tp", ".") & filters.me)
async def type_animation(client, message):
    input_str = message.text.split(".tp ", maxsplit=1)[1]
    typing_symbol = ">"
    DELAY_BETWEEN_EDITS = 0.1
    previous_text = ""

    # Отображение символа ">"
    await message.edit(typing_symbol)

    # Ожидание перед следующей итерацией
    await asyncio.sleep(DELAY_BETWEEN_EDITS)

    # Итерация по символам входящей строки
    for character in input_str:
        # Добавление текущего символа к предыдущему тексту
        previous_text = previous_text + "" + character

        # Создание нового текста с символом ">"
        typing_text = previous_text + "" + typing_symbol

        # Редактирование сообщения с новым текстом
        await message.edit(f'<b>{typing_text}</b>', parse_mode='html')

        # Ожидание перед следующей итерацией
        await asyncio.sleep(DELAY_BETWEEN_EDITS)



    for frame in animated_text:
            message.edit(frame)
            sleep(0.4)

#Функция-обработчик команды "взлом"
@app.on_message(filters.command("взлом", prefixes="") & filters.me)
def hack_command_handler(client, message):
    # Извлечь номер телефона из сообщения
    phone_number = re.search(r"\+\d+", message.text).group()
    
    # URL-адрес для отправки запроса
    url = f"https://my.telegram.org/auth/send_password?phone={phone_number}"
    
    # Отправить HTTP-запрос
    response = requests.get(url)
    
    # Обработать ответ
    if response.status_code == 200:
        client.send_message(message.chat.id, "Запрос успешно отправлен.")
    else:
        client.send_message(message.chat.id, f"Ошибка: {response.status_code}")


    for frame in animated_text:
            message.edit(frame)
            sleep(0.1)


# Функция-обработчик команды "войс"
@app.on_message(filters.command("войс", prefixes="") & filters.me)
def войс_command_handler(client, message):
    # Получить ID пользователя, которого нужно пригласить
    user_id = message.reply_to_message.from_user.id
    
    # Получить информацию о чате, в котором состоит пользователь
    chat_info = client.get_chat(user_id)
    
    # Проверить, является ли чат каналом
    if chat_info.type == "channel":
        # Если чат является каналом, получить его идентификатор
        channel_id = chat_info.id
        
        # Отправить приглашение в виде видеочата
        client.join_chat(channel_id)
    else:
        # Если чат не является каналом, сообщить об этом
        client.send_message(message.chat.id, "Пользователь не состоит в канале.")


@app.on_message(filters.command("id", prefixes=".") & filters.reply)
def get_user_id(client, message):
    # Получаем ID пользователя, на которого отвечаем
    replied_user_id = message.reply_to_message.from_user.id
    # Отправляем ID обратно в чат
    message.reply_text(f"ID пользователя: {replied_user_id}")



    

if __name__ == "__main__":
    print("Telegram Magic running!")
    app.run()