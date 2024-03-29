# Build an Order Book

Thank you for taking the time to complete our coding test. Your challenge is to create an order book:

- an order book is a list of buy and sell orders for a security or instrument organized by price &amp; time.
- order books are used by almost every exchange for assets like stocks, bonds, currencies, and even cryptocurrencies.
- There are three parts to an order book: buy orders, sell orders, and order history.
- More information: [https://www.investopedia.com/terms/o/order-book.asp](https://www.investopedia.com/terms/o/order-book.asp)

You can use any language of your choice and any library for this test. We want to see how you think about and solve problems in code, so make sure there is enough of your own code in there.

Feel free to spend as much or as little time as you&#39;d like as long as you feel it&#39;s complete.

## Problem

Build a point-in-time order book that takes a timestamp input and returns the top 5 best bids (sorted by price descending &amp; time ascending) and top 5 best asks (sorted by price ascending &amp; time ascending) with quantities for a single security.

[Source dataset for the exercise.](https://github.com/Nasdaq/hack/blob/master/software-engineering-interview/quotes_2021-02-18.csv.zip)

Your output should be in the following format:
```
$symbol (time)
Best Bids: price1 (quantity); ... price5 (quantity);
Best Asks: price1 (quantity); ... price5 (quantity);
```

For example:
```
$FAKE (2000-01-02T10:20:55.015Z)
Best Bids: 128.28 (300); 128.27 (100); 128.27 (50); 128.26 (200); 128.24 (100);
Best Asks: 128.25 (100); 128.26 (50); 128.28 (50); 128.28 (200); 128.29 (100);
```

## Dataset Schema

| **Column** | **Description** |
| --- | --- |
| symbol | Symbol |
| marketCenter | Market center for the quote |
| bidQuantity | Bid quantity |
| askQuantity | Ask quantity |
| bidPrice | Bid price |
| askPrice | Ask price |
| startTime | Quote start timestamp in format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; |
| endTime | Quote end timestamp in format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; |
| quoteConditions | Quote condition |
| sipFeed | Feed on which quote was reported |
| sipfeedSeq | Sequence of quote on the feed |

## Submitting

Once you are happy with your code, zip it up, add a readme on running the code, and email it back to us.


