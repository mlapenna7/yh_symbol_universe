import requests
import json
#from array import array
#from datetime import datetime
import logging
#import os
#from html.parser import HTMLParser
#import time

logging.basicConfig(level=logging.DEBUG, filename='yh_get_all_sym.log', 
    filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

hdr = {
    "authority": "finance.yahoo.com",
    "method": "GET",
    "scheme": "https",
    "accept": "text/html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

def get_counts(body, srch):
    count_beg = body.find('All (')
    #print(count_beg)
    rest = body[count_beg+5: count_beg+20]
    #print( rest)
    count_end = rest.find(')')
    #print(count_end)
    count_all = rest[0: count_end]
    logging.info('Counts: ' + srch + ' ' + str(count_all))
    return count_all

def call_url(url,hdr):
    confirmed = False
    while not confirmed:
        try:
            r = requests.get(url, headers=hdr)
            r.raise_for_status()

            #if r.text.find('Something went wrong') > -1:
            #    logging.warning("Found:" + 'Something went wrong')
            #else:
            confirmed = True
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
            logging.warning("Http Error:" + str(errh))
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            logging.warning("Error Connecting" + str(errc.status_code))
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", str(errt.status_code))
            logging.warning("Timeout Error:" + errt)
        except requests.exceptions.RequestException as err:
            print("Something Other Request Error", err)
            logging.warning("Something Other Request Error" + str(err.status_code))

        if not confirmed:
            print("Waiting 1 sec to see if problem resolved then retry")
            time.sleep(1)

    #print()
    # special debug
    #f=open("yh_data/yhallsym.txt","w",encoding='UTF-8')
    #f.write( r.text )
    #f.close()
    return r.text


def process_one(body, srch, yh_all_sym):
    # {"lookupData":{"start":0,"count":100,"total":100,"documents":
    pos_start = body.find('"lookupData":')
    pos_beg = body.find('"documents":')

    look_for_end = "No Results for '" + srch + "'</span>"
    if body.find(look_for_end) > 0:
        print('End of data for ' + srch)
        return -1

    pos_end = body.find('"searchString":', pos_beg+1)

    if pos_start == -1:
        logging.warning("Couldn't find any search data ")
        print('No data for ' + srch)
        return -1

    chunk = body[pos_beg+12: pos_end-1]

    all_rows = ''
    try:
        all_rows = eval(chunk)
    except:
        logging.error("Eval on chunk failed ")
        print('***** Eval on chunk failed')
        return -1

    if len(all_rows) == 0:
        print('End of data for ' + srch)
        return -1
    #else:
        #print('Batch of ' + str(len(all_rows)))

    for one in all_rows:
        #print(one.get('symbol'), one.get('industryName'),  one.get('exchange'), one.get('type'))
        #print(one)
        yh_all_sym[one.get('symbol')] = one.get('shortName')

    return 0


def process_block(body, srch, yh_all_sym, hdr):
    for block in range(0, 9999, 100):
        url = "https://finance.yahoo.com/lookup/all?s=" + srch + "&t=A&b=" + str(block) + "&c=100"
        print('Processing: ', srch, block)
        logging.info('Processing: ' + srch + str(block))
        body = call_url(url,hdr)
        result = process_one(body, srch, yh_all_sym)
        if result == -1:
            break

def main():
    search_set = []
    print(ord('0'), ord('9'), ord('A'), ord('Z'))

    for x in range(65, 91):
        search_set.append(chr(x))

    for x in range(48, 58):
        search_set.append(chr(x))

    #print(search_set)
    yh_all_sym = {}

    #sector_set = [ 'equity', 'mutualfund', 'etf', 'index', 'future', 'currency']
    #sector_set = ['all']
    term_1 = 0
    term_2 = 0
    term_3 = 0

    for term_1 in search_set:
        for term_2 in search_set:
            search_term = term_1 + term_2

            url = "https://finance.yahoo.com/lookup/all?s=" + search_term + "&t=A&b=0&c=25"
            print("calling URL: ", url)

            global hdr
            hdr["path"]=url

            body = call_url(url,hdr)
            all_num = get_counts(body, search_term)
            all_num = int(all_num)
            print(search_term, 'Total:', all_num)

            if all_num < 9000:
                process_block(body, search_term, yh_all_sym,hdr)
            else:
                for term_3 in search_set:
                    search_term = term_1 + term_2 + term_3
                    url = "https://finance.yahoo.com/lookup/all?s=" + search_term + "&t=A&b=0&c=25"
                    hdr["path"] = url

                    body = call_url(url, hdr)
                    all_num= get_counts(body, search_term)
                    all_num = int(all_num)
                    print(search_term, 'Total:', all_num)

                    if all_num < 9000:
                        process_block(body, search_term, yh_all_sym,hdr)
                    else:
                        for term_4 in search_set:
                            search_term = term_1 + term_2 + term_3 + term_4
                            process_block(body, search_term, yh_all_sym, hdr)

            print("Symbols stored so far: ", len(yh_all_sym))
        print("Symbols stored so far: ", len(yh_all_sym))
    print("Total symbols: ", len(yh_all_sym))

    f=open("yhallsym.txt","w",encoding='UTF-8')
    # thefile.write. thefile.write('\n'.join(thelist)) or thefile.write(str(item) + "\n")
    f.write(str(yh_all_sym))
    f.close()

if __name__ == '__main__':
    main()
