# Nasdaq's 2017 HackMIT Challenge:
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

## The Data: Realtime Streaming Stock Market Data 
Two datasets: A) intraday for selected days and b) end-of-day for longer historical range

### Level 1 Data
One of the tools (day) traders use to make their trades is market data, commonly referred to as Level 1 and Level 2 market data, or market depth. Reliable Level 1 quotes aid investors in getting better prices for security purchases and sales, especially in fast-moving markets where investors may prefer limit orders rather than market orders.

### What is 'Bid and Ask'
A two-way price quotation that indicates the best price at which a security can be sold and bought at a given point in time.The bid price represents the maximum price that a buyer or buyers are willing to pay for a security. The ask price represents the minimum price that a seller or sellers are willing to receive for the security. A trade or transaction occurs when the buyer and seller agree on a price for the security.

The difference between the bid and asked prices, or the spread, is a key indicator of the liquidity of the asset - generally speaking, the smaller the spread, the better the liquidity.

### Sample Data

```json
{
    "type": "l1_quote",
    "time": "08:07:10.958899195",
    "symbol": "NDAQ",
    "best_bid": 26.32,
    "best_ask": 48.30
}
```

### Nodejs Client SDK - WebSockets

```javascript
    var sys = require('sys');
    var WebSocket = require('websocket').WebSocket;

    // host connection
    var ws = new WebSocket('ws://0.0.0.0/', 'data');

    // bind listener
    ws.addListener('data', function(buf) {
        sys.debug('Got data: ' + sys.inspect(buf));
    });

    // do something with the stream data  
    ws.onmessage = function(m) {
        sys.debug('Got message: ' + m);
    }
```
