from bot import telegramChatBot

bot = telegramChatBot("config.cfg")
update_id = None


def make_reply(msg):
    if msg is not None:
        reply = "Ok"
    return reply

while True:
    print("...")
    updates = bot.get_updates(offset = update_id)
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                massage = item["massage"]["text"]
            except:
                massage = None
            from_ = item["massage"]["from"]["id"]
            reply =  make_reply(massage)
            bot.send_massage(reply, from_)


