from pyrogram import Client,Filters



app = Client(
    "mynewfindtruebothj",
    api_id= "988003",
    api_hash="a5a734ad1a84a7e62c21f7c5898831d7",
    bot_token="1115604796:AAFZmGuBEWdeHb66OUOB3zBrT-pSgpTCKYc"
)

@app.on_message(Filters.command(["start"]))
def start(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text=f"Hi {message.from_user.first_name}"
      )
    client.send_message(
           chat_id=message.chat.id,
           text="Enter the number to search"
)
@app.on_message(Filters.text)
def echo(client, message):
    pro = client.send_message(
       chat_id = message.chat.id,
       text = "Searching...",
       reply_to_message_id=message.message_id
        )
    num=message.text

app.run()
