from aiogram import types
# from aiogram.dispatcher.filters.builtin import

from loader import dp
try:
    import pyowm
except:
    from PIL import pyowm
from pyowm.utils.config import get_default_config

# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor


config_dict = get_default_config()
config_dict['language'] = 'ru'

# ---------- FREE API KEY examples ---------------------

owm = pyowm.OWM('4838bcc4a7d6f997ba9f521bdfd85706')
mgr = owm.weather_manager()
city = 'Mogilev'


observation = mgr.weather_at_place(city)
w = observation.weather


@dp.message_handler(commands=['weather'])
async def weather_help_command(message: types.Message):
    text = ("Тэмпература сення ад " + str(w.temperature('celsius')["temp_min"])+ "° да " + str(w.temperature('celsius')["temp_max"]) +"°. " +
      "Адчуваецца як " +  str(w.temperature('celsius')["feels_like"]) +"°." + "\n" +
            "Воблачнасць: " + w.detailed_status + "\n" +
            "Вецер: " + str(w.wind()['speed']) + " метраў у секунду" + "\n" +
            'Вільготнасць: ' + str(w.humidity) + '%')

    await message.answer(text)




