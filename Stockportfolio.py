import requests

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol):
        if symbol not in self.stocks:
            self.stocks[symbol] = {'name': None, 'price': None}
            self.update_stock_price(symbol)
        else:
            print(f"{symbol} is already in your portfolio.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"{symbol} removed from your portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def update_stock_price(self, symbol):
        api_key = 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

        try:
            response = requests.get(url)
            data = response.json()
            if 'Global Quote' in data:
                self.stocks[symbol]['price'] = float(data['Global Quote']['05. price'])
                self.stocks[symbol]['name'] = data['Global Quote']['01. symbol']
            else:
                print(f"Failed to retrieve data for {symbol}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_portfolio(self):
        print("Your Portfolio:")
        print("Symbol\t\tName\t\tPrice")
        for symbol, data in self.stocks.items():
            print(f"{symbol}\t\t{data['name']}\t\t{data['price']}")

# Example usage
portfolio = StockPortfolio()
portfolio.add_stock('AAP')
portfolio.add_stock('MSFT')
portfolio.add_stock('GOOGL')
portfolio.display_portfolio()
portfolio.remove_stock('GOOGL')
portfolio.display_portfolio()
