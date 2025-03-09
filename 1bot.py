from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Habilitando logs para o bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Função de início
def start(update, context):
    update.message.reply_text('Olá! Eu sou seu bot de sinais de operações.')

# Função para capturar sinais
def capture_signal(update, context):
    signal_message = update.message.text
    # Aqui você pode adicionar lógica para analisar os sinais enviados
    update.message.reply_text(f'Sinal capturado: {signal_message}')

def main():
    # Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot do Telegram
    updater = Updater('SEU_TOKEN_AQUI', use_context=True)
    dispatcher = updater.dispatcher
    
    # Comandos
    dispatcher.add_handler(CommandHandler('start', start))
    
    # Captura as mensagens (sinais) do Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, capture_signal))
    
    # Iniciar o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
