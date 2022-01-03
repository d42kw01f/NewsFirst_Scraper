from dateutil import parser
import requests
from bs4 import BeautifulSoup
import os
import re
import time
import pandas as pd
from datetime import datetime
from tqdm.auto import tqdm

def scraper(datelist):
    pageBlock = 0
    header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
    loop = tqdm(datelist)
    for i in loop:
        num_artical = 0
        theDate = i.date()
        theDate = str(theDate)
        LinkDate = theDate.replace('-','/')
        FileDate = theDate.replace('-','')
        thisYear = LinkDate.split('/')[0]
        url = f'https://www.newsfirst.lk/sinhala/{LinkDate}/'

        r_main = requests.get(url, headers=header)
        if r_main.status_code == 200:
            pageBlock = 0
            soup_main_page = BeautifulSoup(r_main.text, 'lxml')
            theComURL = ''
            for TheList in soup_main_page.find_all('div', class_='col-md-12 news-lf-section'):
                for TheLink in TheList.findAll('a'):
                    theURL = TheLink.get('href')
                    if (theURL != None) and (theURL != theComURL) and (theURL != '#'):
                        theComURL = theURL
                        try:
                            if re.match('^https://www.newsfirst.lk/', theURL):
                                r = requests.get(theURL, headers=header)
                                soup = BeautifulSoup(r.text, 'lxml')
                                theBody = soup.find('div', class_='text-left w-300 editor-styles')
                                TheRealBodyText = theBody.text.strip()
                                TheRealBodyText = TheRealBodyText.replace("COLOMBO (NEWS1ST) : ", "")
                                TheRealBodyText = TheRealBodyText.replace("\n", "")
                                num_artical += 1

                                if not os.path.isdir(thisYear):
                                    os.makedirs(thisYear)
                                    print('Created folder: ', thisYear)

                                with open(f'NewsFirst_Articals/{thisYear}/news1st_{FileDate}_{num_artical}.txt', 'w', encoding="utf-8") as file:
                                    file.write(TheRealBodyText)
                                loop.set_description(f'artical {num_artical}')
                        except:
                            continue
            # loop.set_description(f'date {LinkDate}')
            time.sleep(20)
        else:
            pageBlock += 1
            if pageBlock == 10:
                print('\n\n\nHad to stop reached 10 pageBlocks in a row!!')
                print('\tURL: {}\n'.format(url))
                print('\tDate: {}'.format(LinkDate))


def main():
    try:
        start_date = parser.parse(input("--> Enter start date: "))
        end_date = parser.parse(input("--> Enter end date: "))
    except:
        print('\n!!!something went wrong. try again...\n\n')

    print("\n\t# Start date: {}\n\t# End date: {}".format(start_date.date(), end_date.date()))
    datelist = pd.date_range(start=start_date.date(),end=end_date.date())
    print('\nHERE IS THE DATAFRAME: ')
    print(datelist)
    print('\n\t# LENGTH OF THE DATAFRAME IS: {}\n'.format(len(datelist))) 

    try:
        user_conf = input('Enter y to confirm & start scraping: [y/n]')
        if user_conf.lower() == 'y':
            print('\n\n\n')
            scraper(datelist)
    except:
        print('Something went wrong...')

main()
