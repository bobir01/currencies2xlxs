import requests as req
import pandas
from datetime import datetime
import logging
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def get_data(url: str, date: datetime=None ) -> req.Response.text:
    """
    Get the JSON data from the CB Uz -> `Response: JSON`
    """
    try:
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d/')
        else:
            date = date.strftime('%Y-%m-%d/')
        response = req.get(url+date)
        if response.status_code == 200:
            return response.text
        else:
            raise req.HTTPError
    except Exception as e:
        logging.error(f"Request was not successfull: {e}")
        raise req.HTTPError



def write_excel(data:str):
    """Writes incoming JSON Response to xlsx file"""
    currencies = pandas.read_json(data, convert_dates=False)
    
    # Little clean up from extra table columns
    currencies['id'] = currencies.index

    currencies.drop(columns=['Code', 'CcyNm_RU', 'CcyNm_UZ', 'CcyNm_UZC', 'Nominal', 'CcyNm_EN'], inplace=True)


    currencies.rename(columns={'id': 'No', 'Ccy': 'CurrencyCode'}, inplace=True)

    currencies.to_excel(BASE_DIR/'data'/ 'currencies.xlsx', index=False)


    