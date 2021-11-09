import time
import threading
import requests
import json
from pathlib import Path
import datetime

# Подключение файла настроек
BASE_DIR = Path(__file__).resolve().parent.parent
try:
    with open('local/config.json') as handle:
        config = json.load(handle)
except IOError:
    config = {
        'url': 'http://127.0.0.1:8000',
    }

url = config['url']

print(f"""

░██████╗░███████╗░█████╗░██╗░░██╗░█████╗░
██╔════╝░██╔════╝██╔══██╗██║░██╔╝██╔══██╗
██║░░██╗░█████╗░░██║░░╚═╝█████═╝░██║░░██║
██║░░╚██╗██╔══╝░░██║░░██╗██╔═██╗░██║░░██║
╚██████╔╝███████╗╚█████╔╝██║░╚██╗╚█████╔╝
░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░

    Информация о worker:
URL-адрес для API: {config.get('url')}
Папка проекта: {BASE_DIR}
©nicstim
    """)

headers = {
    'authority': 'scanner.tradingview.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'accept': 'text/plain, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://ru.tradingview.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://ru.tradingview.com/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.739777081.1635834298; _sp_ses.cf1a=*; _gid=GA1.2.901648321.1636207091; _sp_id.cf1a=7b15c69c-dab5-4b8b-94e0-cfb5d7215b9b.1635834298.6.1636207306.1636076544.ac3849df-5cdd-4fa7-9b7c-b193d8fde30c; _gat_gtag_UA_24278967_1=1',
}


def parser(rsi: str, papers: list, timeout: int, period: str, ):
    d_data = '{"filter":[{"left":"market_cap_basic","operation":"nempty"},{"left":"type","operation":"in_range","right":["stock","dr","fund"]},{"left":"subtype","operation":"in_range","right":["common","foreign-issuer","","etf","etf,odd","etf,otc","etf,cfd"]},{"left":"exchange","operation":"in_range","right":["AMEX","NASDAQ","NYSE"]},{"left":"RSI","operation":"less","right":' + rsi + '},{"left":"is_primary","operation":"equal","right":true}],"options":{"lang":"ru"},"markets":["america"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["logoid","name","close","change","change_abs","Recommend.All","volume","market_cap_basic","price_earnings_ttm","earnings_per_share_basic_ttm","number_of_employees","sector","description","type","subtype","update_mode","pricescale","minmov","fractional","minmove2","currency","fundamental_currency_code"],"sort":{"sortBy":"market_cap_basic","sortOrder":"desc"},"range":[0,150]}'
    w_data = '{"filter":[{"left":"market_cap_basic","operation":"nempty"},{"left":"type","operation":"in_range","right":["stock","dr","fund"]},{"left":"subtype","operation":"in_range","right":["common","foreign-issuer","","etf","etf,odd","etf,otc","etf,cfd"]},{"left":"exchange","operation":"in_range","right":["AMEX","NASDAQ","NYSE"]},{"left":"RSI|1W","operation":"less","right":' + rsi + '},{"left":"is_primary","operation":"equal","right":true}],"options":{"lang":"ru"},"markets":["america"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["logoid","name","close|1W","change|1W","change_abs|1W","Recommend.All|1W","volume|1W","market_cap_basic","price_earnings_ttm","earnings_per_share_basic_ttm","number_of_employees","sector","description","type","subtype","update_mode|1W","pricescale","minmov","fractional","minmove2","currency","fundamental_currency_code"],"sort":{"sortBy":"market_cap_basic","sortOrder":"desc"},"range":[0,150]}'
    data = d_data if period == "d" else w_data
    while True:
        day_num = datetime.datetime.today().isoweekday()
        if day_num != 6 and day_num != 7:
            response = requests.post('https://scanner.tradingview.com/america/scan', headers=headers, data=data)
            for _ in response.json().get('data'):
                if _.get("s"):
                    paper = _.get("s").split(":")
                    if paper[1] in papers:
                        requests.post(f"{url}/service/", data={
                            "paper": paper[1],
                            "period": period
                        })
        time.sleep(timeout * 60)


api_request = requests.get(f"{url}/service/")
for item in api_request.json():
    threading.Thread(target=parser, name="D parser", args=(item.get('rsi_d'), item.get('papers'),
                                                           item.get('d_timeout'), "d")).start()
    threading.Thread(target=parser, name="W parser", args=(item.get('rsi_w'), item.get('papers'),
                                                           item.get('w_timeout'), "w")).start()
