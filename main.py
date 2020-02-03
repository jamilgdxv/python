#!/usr/bin/python3
#-- coding: utf-8 --

import time
import subprocess
import os
import telebot
import urllib #modulo tratamento urls
import emoji
from emoji import emojize

API_TOKEN= '<TOKEN DO SEU BOT>' #Bot gerado pelo BOTFATHER

bot = telebot.TeleBot(API_TOKEN, threaded=False) #Sumario do telebot funcao que aplica o TOKEN

localtime = time.localtime(time.time())

@bot.message_handler(commands=['cable'])

def send_cable(message):
    msg = bot.reply_to(message, """ Digite o *mac* que deseja consultar: \n Conforme o exemplo: *AA:BB:DD:CC:11:22*
""", parse_mode="markdown") #responde ao comando solicitado /cable
    cid = message.chat.id #paga o id da conversa
    bot.register_next_step_handler(msg,send_cable_step) #armazena a informação digitada e continua

def send_cable_step(message):
    try:
      cid = message.chat.id #paga o id da conversa
      cable = message.text #mensagem digitada
      msg = bot.reply_to(message,  "Só um momento por favor...irei realizar sua *consulta!* para o cable: " + str(cable), parse_mode="markdown")
      dados = os.popen('cable.sh ' + str(cable)).read()
      print (dados)
      bot.send_message(cid,"Seguem dados solicitados: \n" + str(dados))
      bot.send_message(cid,"Tenha um ótimo dia de trabalho!")

    except Exception as e:
        bot.reply_to(message, 'Oops, algo deu errado')
        print(e)

@bot.message_handler(commands=['node'])

def send_node(message):
    msg = bot.reply_to(message, """Digite o *node* que deseja consultar: \n Conforme o exemplo: *SFLCM*
""", parse_mode="markdown") #responde ao comando solicitado /cable
    cid = message.chat.id #paga o id da conversa
    bot.register_next_step_handler(msg,send_node_step) #armazena a informação digitada e continua

def send_node_step(message):
    try:
      cid = message.chat.id #paga o id da conversa
      node = message.text #mensagem digitada
      msg = bot.reply_to(message,  "Só um momento por favor...irei realizar sua *consulta!* para o node: " + str(node), parse_mode="markdown")
      dados = os.popen('buscanode.sh ' + str(node)).read()
      print (dados)
      bot.send_message(cid,"Seguem dados solicitados: \n" + str(dados), parse_mode="markdown")
      bot.send_message(cid,"Tenha um ótimo dia de trabalho!")

    except Exception as e:
        bot.reply_to(message, 'Oops, algo deu errado')
        print(e)


@bot.message_handler(commands=['insere'])

def send_insere(message):
    msg = bot.reply_to(message, """Digite o *cable MAC* que deseja inserir no monitoramento: \n Conforme o exemplo: *AA:BB:DD:CC:EE:00:11*
""", parse_mode="markdown") #responde ao comando solicitado /cable
    cid = message.chat.id #paga o id da conversa
    bot.register_next_step_handler(msg,send_insere_step) #armazena a informação digitada e continua

def send_insere_step(message):
    try:
      cid = message.chat.id #paga o id da conversa
      insere = message.text #mensagem digitada
      msg = bot.reply_to(message,  "Só um momento por favor...irei realizar sua *consulta!* para o node: " + str(insere), parse_mode="markdown")
      dados = os.popen('insere_mon.sh ' + str(insere)).read()
      print (dados)
      bot.send_message(cid,"Seguem dados solicitados: \n" + str(dados), parse_mode="markdown")
      bot.send_message(cid,"Tenha um ótimo dia de trabalho!")

    except Exception as e:
        bot.reply_to(message, 'Oops, algo deu errado')
        print(e)



@bot.message_handler(commands=['monitor'])

def send_monitor(message):
    msg = bot.reply_to(message, """Digite o *cable* que deseja resgatar o monitoramento: \n Conforme o exemplo: *AA:BB:DD:CC:EE:00:11*
""", parse_mode="markdown") #responde ao comando solicitado /cable
    cid = message.chat.id #paga o id da conversa
    bot.register_next_step_handler(msg,send_monitor_step) #armazena a informação digitada e continua

def send_monitor_step(message):
    try:
      cid = message.chat.id #paga o id da conversa
      node_monitor = message.text #mensagem digitada
      msg = bot.reply_to(message,  "Só um momento por favor...irei realizar sua *consulta!* para o node: " + str(node_monitor), parse_mode="markdown")
      dados = os.popen('busca_mon.sh ' + str(node_monitor)).read()
      print (dados)
      bot.send_message(cid,"Seguem dados solicitados: \n" + str(dados), parse_mode="markdown")
      bot.send_message(cid,"Tenha um ótimo dia de trabalho!")

    except Exception as e:
        bot.reply_to(message, 'Oops, algo deu errado')
        print(e)



@bot.message_handler(commands=['ajuda', 'start', 'help'])

def send_node(message):
    msg = bot.reply_to(message, """Olá, sou o *LIA* seu consultor digital!\n
Digite /cable para interação de consulta do *cable* aguarde resposta e informe o *MAC* ex: *AA:BB:DD:CC:FF:11*\n
Digite /node para interação de consulta do *node* aguarde resposta e informe o *nome do node* que deseja consultar ex: *SFLCM*\n
Para informações sobre *versão* e *desenvolvedor* o comando /sobre te trará informações sobre mim
""", parse_mode="markdown") #responde ao comando solicitado /cable
    cid = message.chat.id #paga o id da conversa
    bot.send_message(cid,emojize(":robot:", use_aliases=True))



@bot.message_handler(commands=['sobre'])

def about(message):
    msg = bot.reply_to(message, """Olá, sou o *Lenha Inteligência Artificial* rsrsrsr 
para os mais intimos pode me chamar de *LIA* seu ajudante virtual...
Estou engatinhando ainda minha *versão estável* é rev *0.1.38*
Fui criado pelo Analista *Jamil Walber* e esse projeto foi desenvolvido do zero, isso mesmo não é uma copia foi tudo feito no braço!
caso precise entrar em contato com o desenvolvedor seu email é [jamil.walber@claro.com]
Me use com cautela pois todas informações estão sendo logadas hehehe
""", parse_mode="markdown") #responde ao comando solicitado /cable
    cid = message.chat.id #paga o id da conversa
    img = open("/dados/teste_mod/py/img/img1.png", 'rb')
    bot.send_photo(cid, img)
    bot.send_message(cid, """Minhas técnicas de consulta são feitas com *Shell Script* e *Python*!
Favor reportar *falhas* nas *consultas* ou erros meu pai é o *Jamil* então ja sabe para quem reclamar rsrsrs\n
Time de desenvolvimento *Datacenter Claro PR*
*Todos os direitos são reservados* ®
""", parse_mode="markdown")


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling(none_stop=True)
