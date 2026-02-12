import telebot
import random
import os
from io import BytesIO

TOKEN = os.environ.get('AAEIamU8nSW-bKFdsPknUDrjHcK4cV26QA0')  # Token Railway'den alınacak
bot = telebot.TeleBot(TOKEN)

def gen_patch(lib):
    return f'MemoryPatch::createWithHex("lib{lib}.so", 0x{random.randint(0, 0xFFFFFF):X}, "{random.randint(0, 255):X} {random.randint(0, 255):X} {random.randint(0, 255):X} {random.randint(0, 255):X}").Modify();'

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "/bypass yaz ve olacakları gör amk🥶")

@bot.message_handler(commands=['bypass'])
def bypass(m):
    libs = ["anogs", "gcloud", "UE4"]
    kod = ""
    for lib in libs:
        kod += f"// lib{lib}.so\n"
        for _ in range(50):
            kod += gen_patch(lib) + "\n"
        kod += "\n"
    
    txt_file = BytesIO(kod.encode('utf-8'))
    txt_file.name = 'bypass_patch.txt'
    bot.send_document(m.chat.id, txt_file)
    bot.reply_to(m, "✅ Bypassın Hazır yarram")

print("Bot çalışıyor - Token:", TOKEN[:10] + "...")
bot.infinity_polling()