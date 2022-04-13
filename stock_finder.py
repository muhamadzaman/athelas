import requests
import csv 

list_json_objs = []
api_key = "cdd2oraad3ic4dien0ggcdd2oraad3ic4dien0h0"

def get_most_volatile_stock(symbols, api_key):
    """
    This function makes the API calls and gets the most volatile stock
    """

    for symbol in symbols:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
        response = requests.get(url)
        obj = response.json()
        obj["symbol"] = symbol
        list_json_objs.append(obj)

    most_valatile_stock = max(list_json_objs, key = lambda x: x['dp'])
    return most_valatile_stock

def create_csv(header, data):
    """
    This function creates a csv file with header and data passed to it
    """

    with open('stock-info.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

def parse_stock(stock):
    """
    This function parses the stock to get desired values
    """

    parsed_stock = [stock['symbol'], stock['dp'], stock['c'], stock['pc']]
    return parsed_stock


if __name__ == "__main__":

    list_of_symbols = ["AAPL","NFLX", "META", "GOOGL", "AMZN"]
    most_valatile_stock = get_most_volatile_stock(list_of_symbols, api_key)


    header = ["stock_symbol", "percentage_change", "current_price", "last_close_price"]
    data = parse_stock(most_valatile_stock)

    create_csv(header, data)