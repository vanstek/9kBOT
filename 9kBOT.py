
import praw
import pdb
import re
import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json




#GET request url
coin_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


reddit = praw.Reddit('BTC9KBABY') #selects reddit user account. password is in praw.ini file


btc_text = open("prev_price.txt", "r") #opens previous price file
btc_prev = float(btc_text.read())

btc_text.close()


#post submission info if going up
over_title = 'It’s over 9000!!!!'
over_url = 'https://imgur.com/jyoZGyW'

#post submission info if going down
under_title = 'It’s under 9000!!!!'
under_url = 'https://i.imgur.com/SyzEGwl.png

#opens api key file so that api key is not in source code
key = open('coinmarketcap_api_key.txt')
coin_key = key.read()



#coinmarketcap recommended code
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': coin_key,
}
session = Session()
session.headers.update(headers)
parameters = {
  'id':'1'  #id 1 belongs to bitcoin
}

#sends GET request
try:
  response = session.get(coin_url, params=parameters)
  data = json.loads(response.text)
  btc = data["data"]["1"]["quote"]["USD"]["price"] #coinmarketcap api request sets btc price 
  print(str(data["data"]["1"]["quote"]["USD"]["price"]) + '\n \n API request succesful.')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#price movement comparisons for submission type
if btc > btc_prev and btc > 9000 and btc_prev < 9000:
        reddit.subreddit('BTC9K').submit(over_title, url=over_url)
        print('over @ ' + str(btc))
elif btc < btc_prev and btc < 9000 and btc_prev > 9000:
        reddit.subreddit('BTC9K').submit(under_title, url=under_url)
        print('under @ ' + str(btc))

btc_prev = btc

btc_text = open("prev_price.txt", "w") #opens previous price file
btc_text.write(str(btc_prev))
btc_text.close()


