import telebot
import json

token = "5166841243:AAHaXKmJMn-F48ydRM3ailWukKSaPxXlbNI"
bot = telebot.TeleBot(token)


def schedule():
    f = open('Schedule.json', encoding='utf-8')
    return json.loads(f.read())


def schedule_control(message_user):
    try:
        find_date = schedule()
        user_schedule = find_date[message_user]
        return user_schedule
    except KeyError:
        return (f'Невірна дата {message_user}, перевірте правильність вводу дати та спробуйте ще раз.')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, волонтер Filter!\nВведіть дату розклад якої вас цікавить.')


@bot.message_handler(content_types=['text'])
def message_reply(message):
    text = message.text.split()
    if len(text) == 1 and len(text[0]) == 5 and text[0][2] == '.':
        bot.send_message(message.chat.id, schedule_control(text[0]))
    if len(text) != 1:
        pass



bot.polling(none_stop=True, interval=0)
