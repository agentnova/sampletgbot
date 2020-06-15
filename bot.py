from pyrogram import Client,Filters

app = Client(
    "mybot",
    api_id= "",
    api_hash="",
    bot_token=""
)

@app.on_message(Filters.command(["start"]))
def start(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text=f"Hi {message.from_user.first_name}"
      )
@app.on_message(Filters.text)
def echo(client, message):
    client.send_message(
       chat_id = message.chat.id,
       text = "where are you from"
        )
    place=message.text
    client.send_message(
        chat_id = message.chat.id, 
        text = "you are from"+place
)

app.run()
