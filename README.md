# cb2excel
💵Provides Central Bank 🏦 of Uzbekistan currency exchange rates in Excel format📊.  
Used packages/lib:
- [requests](https://pypi.org/project/requests/) - for making request to `API`
- [openpyxl](https://pypi.org/project/openpyxl/) - for creating Excel file as engine writer `pandas DataFrame`
- [pandas](https://pypi.org/project/pandas/) - for creating `DataFrame` and cleaning up extra information
- [aiogram](https://pypi.org/project/aiogram/) - for creating Telegram bots based on `asyncio`
- [environs](https://pypi.org/project/environs/) - for loading `.env` variables


## Installation and Usage
### Requirements
```bash
pip3 install -r requirements.txt # for UnixBased OS
```
`Plesae note:` You need to provide .env variables such as `BOT_TOKEN` and `ADMINS`.

### Run
```bash
python3 app.py
```