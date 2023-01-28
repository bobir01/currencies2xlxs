import asyncio
from aiogram import types
from data.config import URL
from loader import dp, bot
from datetime import datetime
from pathlib import Path
from utils.date_parser import check_date_format
from utils.main_scrapper import get_data, write_excel

BASE_DIR = Path(__file__).resolve().parent.parent


@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer("Hi there, I am simple bot that sends "
                     "foreign currencies rate based CB Uzbekistan\n"
                     "Just click  <b> /rate </b> to get current rates\n"
                     "Even you can get past rates by long pressing(on mobile) to /rate and enter "
                     "the date you would like to see in format <code>dd-mm-yyyy</code>\n"
                     "For example: <code>/rate 30-12-2021</code>\n"
                     "Disclaimer: Note that the rates may not updated on weekends or holidays "
                     "as well as the column <b>Date</b> represents the date of the last update")


@dp.message_handler(commands='rate')
async def get_rate(msg: types.Message):
    user_date = msg.get_args()
    msg_id = await msg.answer("Please wait...")
    await asyncio.sleep(1)
    await bot.delete_message(msg.from_user.id, msg_id.message_id)
    if user_date:
        date = check_date_format(user_date)

        if date:
            json_data = get_data(URL, date)
            write_excel(json_data)
            with open(BASE_DIR / 'data' / 'currencies.xlsx', 'rb') as excel:
                await msg.answer_document(excel,
                                          caption=f"Here are the rates for {date.strftime('%d-%m-%Y')}")
                excel.close()
        else:
            await msg.answer("Please enter the date in format <code>dd-mm-yyyy</code>")
    else:
        json_data = get_data(URL)
        write_excel(json_data)
        with open(BASE_DIR / 'data' / 'currencies.xlsx', 'rb') as excel:
            await msg.answer_document(excel,
                                      caption=f"Here are the rates for {datetime.now().strftime('%d-%m-%Y')}")
            excel.close()
