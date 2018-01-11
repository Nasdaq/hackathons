# Nasdaq's hackathon challenge:
## "Best Re-imagination of Markets" - Hack today's financial markets. We are looking for hacks that introduce a new way to look at financial markets.

Examples:
* Face recognition technology parallel to creating financial landmarks
* Electrical signal process to find financial signals
* Using Amazon Alexa, chat bots for financial use case
* VR for a financial use-case
* Graph technology for finance
* Visualization of some analysis; visualize market data as a tree growing
* Show streaming market data in context of historical norms
* Identify inflection point on streaming market data
* Chart of chocolate milk production vs. Nasdaq-100 index performance

## Judging Criteria
* Intersting use of the data
* Potential impact
* Technical accomplishment
* Flair, baby

## Sample Data

```json
{
    "Symbol": "NDAQ",
    "DateStamp": "2017-08-10T00:00:00Z",
    "High": 76.7999000000, 
    "Low": 75.5810000000,  
    "Open": 76.0300000000,
    "Close": 75.9200000000, 
    "LastSale": 75.9200000000, 
    "Volume": 750671
}
```

## Address and Usage
### URI for realtime stream
```
ws://34.214.40.112/stream
```

### Parameters
* Symbols (stock tickers) - one or more, comma seperated
```
symbol=NDAQ,AAPL,GOOG,MSFT
```
* Start date
```
start=20170101
```
* End date
```
end=20170201
```

## Client WebSocket Examples
### Nodejs
```javascript
    var WebSocket = require('ws');
    var ws = new WebSocket("ws://34.214.40.112/stream?symbol=NDAQ,AAPL,GOOG,MSFT&start=20170101&end=20170201");

    process.stdin.resume();
    process.stdin.setEncoding('utf8');

    process.stdin.on('data', function(message) {
      message = message.trim();
      ws.send(message, console.log.bind(null, 'Sent : ', message));
    });

    ws.on('message', function(message) {
      console.log('Received: ' + message);
    });

    ws.on('close', function(code) {
      console.log('Disconnected: ' + code);
    });

    ws.on('error', function(error) {
      console.log('Error: ' + error.code);
    });
```

### Python 2.7
```python
    import sys
    import websocket
    import thread
    import time

    def on_message(ws, message):
        print message

    def on_error(ws, error):
        print error

    def on_close(ws):
        print "### closed ###"

    def on_open(ws):
        def run(*args):
            for i in range(1):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            ws.close()
            print "thread terminating..."
        thread.start_new_thread(run, ())

    if __name__ == "__main__":
        websocket.enableTrace(True)
        url = 'ws://34.214.40.112/stream?symbol=NDAQ,AAPL,GOOG,MSFT&start=20170101&end=20170201')
        ws = websocket.WebSocketApp(url,
                                    on_message = on_message,
                                    on_error = on_error,
                                    on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()
```
 ### Python 3 Example
 ```python
 import websocket
import threading
import time
import argparse

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run():
        ws.send("")
        time.sleep(1)
        ws.close()
    threading.Thread(target=run).start()

def main():
    parser = argparse.ArgumentParser(description='gettin some market data')
    parser.add_argument('--start_date', required=True, help="Enter a valid start date in YYYYMMDD format")
    parser.add_argument('--end_date', required=True, help="Enter a valid end date in YYYYMMDD format")
    parser.add_argument('--symbols', required=True, help="Enter a ticker symbol or list of tickers. E.g. NDAQ or NDAQ,AAPL,MSFT")

    args = parser.parse_args()

    websocket.enableTrace(True)

    symbols = args.symbols.split(',')

    for symbol in symbols:
        url = 'ws://34.214.40.112/stream?symbol={}&start={}&end={}'.format(symbol,args.start_date,args.end_date)
 
        ws = websocket.WebSocketApp(url,
                                    on_message = on_message,
                                    on_error = on_error,
                                    on_close = on_close)
        ws.on_open = on_open
        ws.run_forever()

if __name__ == "__main__":
   main() 
```
