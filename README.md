# NewsFirst_Scraper
This is a very simple python script that can scrapes the newsfirst.lk website based on the given dates. Moreover, It scrapes and stores the obtained data in a text file.
This script was developed to gain sinhala language data to train Sinhala NLP models.

## How to use this
```python
>>> python3 .\newsfirst_scraper.py

--> Enter start date: 2014-06-04
--> Enter end date: 2014-06-05

        # Start date: 2014-06-04
        # End date: 2014-06-05

HERE IS THE DATAFRAME:
DatetimeIndex(['2014-06-04', '2014-06-05'], dtype='datetime64[ns]', freq='D')

        # LENGTH OF THE DATAFRAME IS: 2

Enter y to confirm & start scraping: [y/n]y

articals 28: 100%|█████████████████████████████████████████████████████████████████████████| 2/2 [02:59<00:00, 89.59s/it]

  ```
  
