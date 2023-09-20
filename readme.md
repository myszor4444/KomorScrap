## What is this?

KomornikScrap is **extremely simple** program for scraping bailiff announcements from from Polish National Bailiffs' Council website. It was created **for educational purposes**.


## Technical matters

Script is written in Python 3 and you need some Python modules to use it:
1. requests
2. BeautifulSoup
3. unicodedata
4. re

## How to use it?

Bailiff notices in Poland are published on https://licytacje.komornik.pl. Each Notice has a unique number. 

To use a program just run it and input required data:

1. Notice Number from each you want to start scraping. 
2. Number of subsequent announcements you wish to download.

If notices with given notice numbers are still accessible, script downloads them and saves them in file HTML (notices.html).
Additional information found in notices - land and mortgage register numbers and adresses - is saved in TXT file (books.txt)
