import telebot

CHAVE_API = "5040573560:AAFx7xAQL6heWuzCCzsB0WEEdw0zGch8864"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "Eu não faço ideia do que você está falando então não fale nada")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Não reclame comigo eu sou apenas um Bot")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Se você falou algo fofinho então eu amo você(mentira eu nem existo) haha")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Falar qualquer coisa haha
    /opcao2 Reclamar de algo u.u
    /opcao3 Falar algo fofinho :)
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()