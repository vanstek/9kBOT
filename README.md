# 9kBOT

 
CRONTAB Code in bash
This is to create a job that automates the python script every 5 minutes. (could do up to 1 minute but free-tier CoinMarketCap API only allows for 333 requests a day)

Automate script:
crontab -e
*/5 * * * * cd /usr/bin/9kBOT//; ./9kBOT.py
