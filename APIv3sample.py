#!/usr/bin/python3

import json

import BittrexAPIv3

loglevel = 10
marketSymbol = "BTC-USD"
currencySymbol = "USD"

result = BittrexAPIv3.get_currencies(currencySymbol, loglevel)
print (json.dumps(result, indent=4, sort_keys=True))

marketPath   = None
marketQuery  = None
result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
print (json.dumps(result, indent=4, sort_keys=True))

api = {'apikey' : '', 'apisecret' : ''}
#print (json.dumps(api, indent=4, sort_keys=True))
###############################################################################################
#
# Sample commands
#
# Be careful using the code. Careless use of the subs below can result in a loss of money!
#
# Read additional (official) information here: https://bittrex.github.io/api/v3
#
# Donations:
#
# BTC: 17kZJHjouZqLmMwntg2M6zzdEW3Jivx79o
# ETH: 0xda1be63336b49e25201d2f406f01b1989f6146c1
#
###############################################################################################
#
#ACCOUNT
#
#GET /account
#result = BittrexAPIv3.get_account(api, None, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/fees/trading
#result = BittrexAPIv3.get_account(api, "fees/trading", loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/fees/trading/{marketSymbol}
#result = BittrexAPIv3.get_account(api, "fees/trading/" + marketSymbol, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/volume
#result = BittrexAPIv3.get_account(api, "volume", loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/permissions/markets
#result = BittrexAPIv3.get_account(api, "permissions/markets", loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/permissions/markets/{marketSymbol}
#result = BittrexAPIv3.get_account(api, "permissions/markets/" + marketSymbol, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/permissions/currencies
#result = BittrexAPIv3.get_account(api, "permissions/currencies", loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /account/permissions/currencies
#result = BittrexAPIv3.get_account(api, "permissions/currencies/" + currencySymbol, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#ADDRESSES
#
#GET /addresses
#result = BittrexAPIv3.get_addresses(api, None, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#POST /addresses
#param = {'currencySymbol' : 'SYS'}
#result = BittrexAPIv3.post_addresses(api, param, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /addresses/{currencySymbol}
#currencySymbol = "SYS"
#result = BittrexAPIv3.get_addresses(api, currencySymbol, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#BALANCES
#
#GET /balances
#result = BittrexAPIv3.get_balances(api, None, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /balances
#result = BittrexAPIv3.head_balances(api, loglevel);
#print (result)
#
#GET /balances/{currencySymbol}
#currencySymbol = "SYS"
#result = BittrexAPIv3.get_balances(api, currencySymbol, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#BATCH
#
#POST /batch
#param = [{"resource": "string","operation": "string","payload": "object"}]
#result = BittrexAPIv3.post_batch(api, param, loglevel);
#print (result)
#
#CONDITIONAL ORDERS
#
#GET /conditional-orders/{conditionalOrderId}
#orderid = ""
#result = BittrexAPIv3.get_conditionalorders(api, orderid, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#DELETE /conditional-orders/{conditionalOrderId}
#orderid = "b06281b7-0329-4ba3-84c1-0704d2bb6602"
#result = BittrexAPIv3.del_conditionalorders(api, orderid, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /conditional-orders/closed
#result = BittrexAPIv3.get_conditionalorders(api, "closed", loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /conditional-orders/open
#result = BittrexAPIv3.get_conditionalorders(api, "open", loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /conditional-orders/open
#result = BittrexAPIv3.head_conditionalorders(api, "open", loglevel);
#print (result)
#
#POST /conditional-orders
#newConditionalOrder = {
#  "marketSymbol": "BTC-EUR",
#  "operand": "GTE",
#  "triggerPrice": "100000",
#  "orderToCreate": {
#    "marketSymbol": "BTC-EUR",
#    "direction": "BUY",
#    "type": "LIMIT",
#    "quantity": "1",
#    "limit": "10",
#    "timeInForce": "GOOD_TIL_CANCELLED",
#  },
#}
#result = BittrexAPIv3.post_conditionalorders(api, newConditionalOrder, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#CURRENCIES
#
#GET /currencies
#currencySymbol = None
#result = BittrexAPIv3.get_currencies(currencySymbol, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /currencies/{symbol}
#currencySymbol = "BTC"
#result = BittrexAPIv3.get_currencies(currencySymbol, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#DEPOSITS
#
#GET /deposits/open
#result = BittrexAPIv3.get_deposits(api, "open", loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /deposits/open
#result = BittrexAPIv3.head_deposits(api, "open", loglevel)
#print (result)
#
#GET /deposits/closed
#result = BittrexAPIv3.get_deposits(api, "closed", loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /deposits/ByTxId/{txId}
#txid = ""
#result = BittrexAPIv3.get_deposits(api, "ByTxId/" + txid, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /deposits/{depositId}
#depositid = ""
#result = BittrexAPIv3.get_deposits(api, depositid, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#EXECUTIONS
#
#GET /executions/{executionId}
#executionid = ""
#result = BittrexAPIv3.get_executions(api, executionid, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /executions
#params = "marketSymbol=BTC-USD&startDate=2019-01-02T16:23:45Z"
#result = BittrexAPIv3.get_executions(api, None, params, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /executions/last-id
#result = BittrexAPIv3.get_executions(api, "last-id", None, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /executions/last-id
#result = BittrexAPIv3.head_executions(api, "last-id", loglevel)
#print (result)
#
#FUNDS TRANSFER METHODS
#
#GET /funds-transfer-methods/{fundsTransferMethodId}
#param = ""
#result = BittrexAPIv3.get_fundstransfermethods(api, param, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#MARKETS
#
#GET /markets
#marketSymbol = None
#marketPath   = None
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /markets/summaries
#marketSymbol = None
#marketPath   = "summaries"
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /markets/summaries
#marketSymbol = None
#marketPath   = "summaries"
#marketQuery  = None
#result = BittrexAPIv3.head_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (result)
#
#GET /markets/tickers
#marketSymbol = None
#marketPath   = "tickers"
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /markets/tickers
#marketSymbol = None
#marketPath   = "tickers"
#marketQuery  = None
#result = BittrexAPIv3.head_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (result)
#
#GET /markets/{marketSymbol}/ticker
#marketSymbol = "BTC-USD"
#marketPath   = "ticker"
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /markets/{marketSymbol}
#marketSymbol = "BTC-USD"
#marketPath   = None
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /markets/{marketSymbol}/summary
#marketSymbol = "BTC-USD"
#marketPath   = "summary"
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /markets/{marketSymbol}/orderbook
#marketSymbol = "BTC-USD"
#marketPath   = "orderbook"
#marketQuery  = "depth=500" #Allowed values: 1, 25, 500
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /markets/{marketSymbol}/orderbook
#marketSymbol = "BTC-USD"
#marketPath   = "orderbook"
#marketQuery  = "depth=500" #Allowed values: 1, 25, 500
#result = BittrexAPIv3.head_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (result)
#
#GET /markets/{marketSymbol}/trades
#marketSymbol = "BTC-USD"
#marketPath   = "trades"
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /markets/{marketSymbol}/trade
#marketSymbol = "BTC-USD"
#marketPath   = "trades"
#marketQuery  = None
#result = BittrexAPIv3.head_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (result)
#
#GET /markets/{marketSymbol}/candles/{candleType}/{candleInterval}/recent
#marketSymbol = "BTC-EUR"
#candleInterval = "MINUTE_5" #MINUTE_1, MINUTE_5, HOUR_1, DAY_1
#candleType   = "TRADE"      #TRADE, MIDPOINT
#marketPath   = "candles/" + candleType + "/" + candleInterval + "/recent"
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /markets/{marketSymbol}/trade
#marketSymbol = "BTC-EUR"
#candleInterval = "MINUTE_5" #MINUTE_1, MINUTE_5, HOUR_1, DAY_1
#candleType   = "TRADE"      #TRADE, MIDPOINT
#marketPath   = "candles/" + candleType + "/" + candleInterval + "/recent"
#marketQuery  = None
#result = BittrexAPIv3.head_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (result)
#
#GET /markets/{marketSymbol}/candles/{candleType}/{candleInterval}/historical/{year}/{month}/{day}
#marketSymbol = "BTC-EUR"
#candleInterval = "MINUTE_5" #MINUTE_1, MINUTE_5, HOUR_1, DAY_1
#candleType   = "TRADE"      #TRADE, MIDPOINT
#year = 2021
#month = 1
#day  = 1
#marketPath   = "candles/" + candleType + "/" + candleInterval + "/historical/" + str(year) + "/" + str(month) + "/" + str(day)
#marketQuery  = None
#result = BittrexAPIv3.get_markets(marketSymbol, marketPath, marketQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#ORDERS
#
#GET /orders/closed
#orderPath  = "closed"
#orderParam = None
#result = BittrexAPIv3.get_orders(api, orderPath, orderParam, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /orders/open
#orderPath  = "open"
#orderParam = None
#result = BittrexAPIv3.get_orders(api, orderPath, orderParam, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#DELETE /orders/open
#orderPath  = "open"
#orderParam = "marketSymbol=BTC-EUR"
#result = BittrexAPIv3.del_orders(api, orderPath, orderParam, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#HEAD /orders/open
#orderPath  = "open"
#result = BittrexAPIv3.head_orders(api, orderPath, loglevel)
#print (result)
#
#GET /orders/{orderId}
#orderPath = ""
#orderParam = None
#result = BittrexAPIv3.get_orders(api, orderPath, orderParam, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#DELETE /orders/{orderId}
#orderPath = ""
#orderParam = None
#result = BittrexAPIv3.del_orders(api, orderPath, orderParam, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /orders/{orderId}/executions
#orderId   = ""
#orderPath = orderId + "/executions"
#orderParam = None
#result = BittrexAPIv3.get_orders(api, orderPath, orderParam, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#POST /orders
#newOrder = {
#  "marketSymbol": "BTC-EUR",
#  "direction": "BUY",          #BUY, SELL
#  "type": "LIMIT",             #LIMIT, MARKET, CEILING_LIMIT, CEILING_MARKET
#  "quantity": "1",
#  "limit": "1",
#  "timeInForce": "GOOD_TIL_CANCELLED", #GOOD_TIL_CANCELLED, IMMEDIATE_OR_CANCEL, FILL_OR_KILL, POST_ONLY_GOOD_TIL_CANCELLED, BUY_NOW, INSTANT
#}
#result = BittrexAPIv3.post_orders(api, newOrder, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#PING
#
#GET /ping
#result = BittrexAPIv3.get_ping(loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#SUBACCOUNTS NOTE: This API is limited to partners and not available for traders.
#
#GET /subaccounts
#subaccountsQuery = "&".join(["nextPageToken=", "previousPageToken=", "pageSize=100"]) #optional
#subaccountsQuery = None
#result = BittrexAPIv3.get_subaccounts(api, None, subaccountsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#POST /subaccounts
#newSubaccount = {} #There is no official specifications
#result = BittrexAPIv3.post_subaccounts(api, newSubaccount, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /subaccounts/{subaccountId}
#subaccountId = ""
#result = BittrexAPIv3.get_subaccounts(api, subaccountId, None, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /subaccounts/withdrawals/open
#subaccountsQuery = "&".join(["currencySymbol=string","nextPageToken="]) #...etc optional
#subaccountsQuery = None
#subaccountsPath = "withdrawals/open"
#result = BittrexAPIv3.get_subaccounts(api, subaccountsPath, subaccountsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /subaccounts/withdrawals/closed
#subaccountsQuery = "&".join(["currencySymbol=string","nextPageToken="]) #...etc optional
#subaccountsQuery = None
#subaccountsPath = "withdrawals/closed"
#result = BittrexAPIv3.get_subaccounts(api, subaccountsPath, subaccountsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /subaccounts/deposits/open
#subaccountsQuery = "&".join(["currencySymbol=string","nextPageToken="]) #...etc optional
#subaccountsQuery = None
#subaccountsPath = "deposits/open"
#result = BittrexAPIv3.get_subaccounts(api, subaccountsPath, subaccountsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /subaccounts/deposits/closed
#subaccountsQuery = "&".join(["currencySymbol=string","nextPageToken="]) #...etc optional
#subaccountsQuery = None
#subaccountsPath = "deposits/closed"
#result = BittrexAPIv3.get_subaccounts(api, subaccountsPath, subaccountsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#TRANSFERS NOTE: This API is limited to partners and not available for traders.
#
#GET /transfers/sent
#transfersQuery = "&".join(["currencySymbol=string","nextPageToken="]) #...etc optional
#transfersQuery = None
#transfersPath = "sent"
#result = BittrexAPIv3.get_transfers(api, transfersPath, transfersQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /transfers/received
#transfersQuery = "&".join(["currencySymbol=string","nextPageToken="]) #...etc optional
#transfersQuery = None
#transfersPath = "received"
#result = BittrexAPIv3.get_transfers(api, transfersPath, transfersQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /transfers/{transferId}
#transfersQuery = None
#transfersPath = "" # transferId uuid-formatted string
#result = BittrexAPIv3.get_transfers(api, transfersPath, transfersQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#POST /transfers
#newTransfer = {}
#result = BittrexAPIv3.post_transfers(api, newTransfer, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#WITHDRAWALS
#
#GET /withdrawals/open
#withdrawalsQuery = "&".join(["status=AUTHORIZED", "currencySymbol=BTC"]) #REQUESTED, AUTHORIZED, PENDING, ERROR_INVALID_ADDRESS
#withdrawalsPath = "open"
#result = BittrexAPIv3.get_withdrawals(api, withdrawalsPath, withdrawalsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /withdrawals/closed
#withdrawalsQuery = "&".join(["status=COMPLETED", "currencySymbol=BTC"])
#withdrawalsPath = "closed"
#result = BittrexAPIv3.get_withdrawals(api, withdrawalsPath, withdrawalsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /withdrawals/ByTxId/{txId}
#withdrawalsQuery = None
#txId = ""
#withdrawalsPath = "ByTxId/" + txId
#result = BittrexAPIv3.get_withdrawals(api, withdrawalsPath, withdrawalsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /withdrawals/{withdrawalId}
#withdrawalsQuery = None
#withdrawalId = ""
#result = BittrexAPIv3.get_withdrawals(api, withdrawalsId, withdrawalsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#DELETE /withdrawals/{withdrawalId}
#withdrawalId = ""
#result = BittrexAPIv3.del_withdrawals(api, withdrawalsId, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
#
#POST /withdrawals
#newWithdrawal = {
#  "currencySymbol": "BTC",
#  "quantity": "0.001",
#  "cryptoAddress": "", # Be careful!!!
#}
#result = BittrexAPIv3.post_withdrawals(api, newWithdrawal, loglevel);
#print (json.dumps(result, indent=4, sort_keys=True))
#
#GET /withdrawals/allowed-addresses
#withdrawalsQuery = None
#withdrawalsPath = "allowed-addresses"
#result = BittrexAPIv3.get_withdrawals(api, withdrawalsPath, withdrawalsQuery, loglevel)
#print (json.dumps(result, indent=4, sort_keys=True))
