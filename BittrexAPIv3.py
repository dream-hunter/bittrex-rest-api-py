#!/usr/bin/python3

import requests
import json
import time
import hashlib
import hmac

def logmessage(message, loglevel):
    if int(loglevel) > 5:
        print(message)

def url_request_get(url, parameters, api, method, loglevel):
    if parameters is not None:
        url = str(url) + "?" + str(parameters)
    print ("Attempt to get ", url)
    if api is not None :
        apikey    = api['apikey']
        apisecret = api['apisecret']
        nonce = int(time.time() * 1000)
        contenthash = hashlib.sha512().hexdigest()
        presign = str(nonce) + url + method + contenthash
        signature = hmac.new(apisecret.encode(), presign.encode(), hashlib.sha512).hexdigest()
        headers = {
          'Api-Key' : apikey,
          'Api-Timestamp' : str(nonce),
          'Api-Content-Hash': contenthash,
          'Api-Signature' : signature
        }
        req = requests.get(url, headers=headers)
    else:
        req = requests.get(url)

    parsed = json.loads(req.text)
#    print (json.dumps(parsed, indent=4, sort_keys=True))
    return parsed

def url_request_head(url, parameters, api, method, loglevel):
    if parameters is not None:
        url = str(url) + "?" + str(parameters)
    print ("Attempt to head ",url)
    if api is not None :
        apikey    = api['apikey']
        apisecret = api['apisecret']
        nonce = int(time.time() * 1000)
        contenthash = hashlib.sha512(json.dumps(parameters).encode()).hexdigest()
        presign = str(nonce) + url + method + contenthash
        signature = hmac.new(apisecret.encode(), presign.encode(), hashlib.sha512).hexdigest()
        headers = {
          'Api-Key' : apikey,
          'Api-Timestamp' : str(nonce),
          'Api-Content-Hash': contenthash,
          'Api-Signature' : signature
        }
        req = requests.head(url, headers=headers)
    else:
        req = requests.head(url)
    return req.headers

def url_request_post(url, parameters, api, method, loglevel):
    print ("Attempt to post ",url)
    if api is not None :
        apikey    = api['apikey']
        apisecret = api['apisecret']
        nonce = int(time.time() * 1000)
        contenthash = hashlib.sha512(json.dumps(parameters).encode()).hexdigest()
        presign = str(nonce) + url + method + contenthash
        signature = hmac.new(apisecret.encode(), presign.encode(), hashlib.sha512).hexdigest()
        headers = {
          'Api-Key' : apikey,
          'Api-Timestamp' : str(nonce),
          'Api-Content-Hash': contenthash,
          'Api-Signature' : signature
        }
        req = requests.post(url, headers=headers, json=parameters)
    else:
        req = requests.post(url, data=parameters)
    parsed = json.loads(req.text)
    return parsed

def url_request_del(url, parameters, api, method, loglevel):
    if parameters is not None:
        url = str(url) + "?" + str(parameters)
    print ("Attempt to delete ", url)
    if api is not None :
        apikey    = api['apikey']
        apisecret = api['apisecret']
        nonce = int(time.time() * 1000)
        contenthash = hashlib.sha512().hexdigest()
        presign = str(nonce) + url + method + contenthash
        signature = hmac.new(apisecret.encode(), presign.encode(), hashlib.sha512).hexdigest()
        headers = {
          'Api-Key' : apikey,
          'Api-Timestamp' : str(nonce),
          'Api-Content-Hash': contenthash,
          'Api-Signature' : signature
        }
        req = requests.delete(url, headers=headers)
    else:
        req = requests.delete(url)

    parsed = json.loads(req.text)
    return parsed

def url_request(url, parameters, api, method, loglevel):
    result = None
    if method == 'GET':
        result = url_request_get(url, parameters, api, method, loglevel),
    if method == 'HEAD':
        result = url_request_head(url, parameters, api, method, loglevel),
    if method == 'POST':
        result = url_request_post(url, parameters, api, method, loglevel),
    if method == 'DELETE':
        result = url_request_del(url, parameters, api, method, loglevel),
    return result

def bittrex_api(command, parameters, api, method, loglevel):
    url = "https://api.bittrex.com/v3/" + str(command)
    logmessage ("bittrex_api Exec request \"" + url + "\"...", loglevel);
    result = url_request(url, parameters, api, method, loglevel);
#    logmessage ("bittrex_api Response code: " + str(result), loglevel);
    return result

def get_account(api, addPath, loglevel):
    apiRequest = "account"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def get_addresses(api, addPath, loglevel):
    apiRequest = "addresses"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def post_addresses(api, parameters, loglevel):
    apiRequest = "addresses"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def get_balances(api, addPath, loglevel):
    apiRequest = "balances"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def head_balances(api, loglevel):
    apiRequest = "balances"
    method     = "HEAD"
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def post_batch(api, parameters, loglevel):
    apiRequest = "batch"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def get_conditionalorders(api, addPath, loglevel):
    apiRequest = "conditional-orders"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def del_conditionalorders(api, addPath, loglevel):
    apiRequest = "conditional-orders"
    method     = "DELETE"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def head_conditionalorders(api, addPath,loglevel):
    apiRequest = "conditional-orders"
    method     = "HEAD"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def post_conditionalorders(api, parameters, loglevel):
    apiRequest = "conditional-orders"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def get_currencies(currencySymbol, loglevel):
    apiRequest = "currencies"
    method     = "GET"
    if currencySymbol is not None:
        apiRequest = str(apiRequest) + "/" + str(currencySymbol)
    result = bittrex_api(apiRequest, None, None, method, loglevel)
    return result

def get_deposits(api, addPath, loglevel):
    apiRequest = "deposits"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def head_deposits(api, addPath, loglevel):
    apiRequest = "deposits"
    method     = "HEAD"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def get_executions(api, addPath, parameters, loglevel):
    apiRequest = "executions"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def head_executions(api, addPath, loglevel):
    apiRequest = "executions"
    method     = "HEAD"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def get_fundstransfermethods(api, addPath, loglevel):
    apiRequest = "funds-transfer-methods"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def get_markets(marketSymbol, marketPath, marketQuery, loglevel):
    apiRequest = "markets"
    method     = "GET"
    if marketSymbol is not None:
        apiRequest = str(apiRequest) + "/" + str(marketSymbol)
    if marketPath is not None:
        apiRequest = str(apiRequest) + "/" + str(marketPath)
    if marketQuery is not None:
        apiRequest = str(apiRequest) + "?" + str(marketQuery)
    result = bittrex_api(apiRequest, None, None, method, loglevel)
    return result

def head_markets(marketSymbol, marketPath, marketQuery, loglevel):
    apiRequest = "markets"
    method     = "HEAD"
    if marketSymbol is not None:
        apiRequest = str(apiRequest) + "/" + str(marketSymbol)
    if marketPath is not None:
        apiRequest = str(apiRequest) + "/" + str(marketPath)
    if marketQuery is not None:
        apiRequest = str(apiRequest) + "?" + str(marketQuery)
    result = bittrex_api(apiRequest, None, None, method, loglevel)
    return result

def get_orders(api, addPath, parameters, loglevel):
    apiRequest = "orders"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def del_orders(api, addPath, parameters, loglevel):
    apiRequest = "orders"
    method     = "DELETE"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def head_orders(api, addPath, loglevel):
    apiRequest = "orders"
    method     = "HEAD"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

def post_orders(api, parameters, loglevel):
    apiRequest = "orders"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def get_ping(loglevel):
    apiRequest = "ping"
    method     = "GET"
    result = bittrex_api(apiRequest, None, None, method, loglevel)
    return result

def get_subaccounts(api, addPath, parameters, loglevel):
    apiRequest = "subaccounts"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def post_subaccounts(api, parameters, loglevel):
    apiRequest = "subaccounts"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def get_transfers(api, addPath, parameters, loglevel):
    apiRequest = "transfers"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def post_transfers(api, parameters, loglevel):
    apiRequest = "transfers"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def get_withdrawals(api, addPath, parameters, loglevel):
    apiRequest = "withdrawals"
    method     = "GET"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def post_withdrawals(api, parameters, loglevel):
    apiRequest = "withdrawals"
    method     = "POST"
    result = bittrex_api(apiRequest, parameters, api, method, loglevel)
    return result

def del_withdrawals(api, addPath, loglevel):
    apiRequest = "withdrawals"
    method     = "DELETE"
    if addPath is not None:
        apiRequest = str(apiRequest) + "/" + str(addPath)
    result = bittrex_api(apiRequest, None, api, method, loglevel)
    return result

