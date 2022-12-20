import requests

while True:
    to_search = input()
    url = f"https://lumi-ragnarok.net/api/market/whosell?limit=50&offset=0&filter=all&query={to_search}&jobs=all"
    request = requests.get(url).json()

    for item in request["results"]:
        print(item["name"], item['x'], item['y'], item['amount'], item['price'])
# данный код позволяет в реальном времени отслеживать информацию о наличии предметов на рынке(онлайн рынок игровой,введите слово
# на английском,например 'blue'. Это лучше,чем спарсить погоду =). Он показывает название предмета,продавцы с его игровыми
# координатами и цену предмета