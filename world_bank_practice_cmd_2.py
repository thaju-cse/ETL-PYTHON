Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
web_page = requests.get(url)
web_page.status
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    web_page.status
AttributeError: 'Response' object has no attribute 'status'
web_page.status()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    web_page.status()
AttributeError: 'Response' object has no attribute 'status'
web_page
<Response [403]>
web_page.connection
<requests.adapters.HTTPAdapter object at 0x0000029355FBFE00>
web_page.ok
False
web_page.status_code
403
print(webpage.text)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(webpage.text)
NameError: name 'webpage' is not defined. Did you mean: 'web_page'?
web_page.text
'Please set a user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119.\n'
url = 'https://web.archive.org/web/20251007065341/https://en.wikipedia.org/wiki/List_of_largest_banks'
web_page = requests.get(url)
web_page.status_code
200
web_page_tables = web_page.text.find_all('table')

web_text = web_page.text
web_text

len(web_text)
214907
soup_web_text = BeautifuSoup(web_text, 'html.parser')

soup_web_text = BeautifulSoup(web_text, 'html.parser')
soup_tables = soup_web_text.find_all('table')
len(soup_tables)
4
soup_tables[0]

soup_tables[1]

soup_data = soup_tables.find_all('tr')

soup_data = soup_tables[1].find_all('tr')
print(soup_data.text)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(soup_data.text)
  File "E:\Python(latest)\Lib\site-packages\bs4\element.py", line 3203, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute "text". You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
soup_data[0]
<tr>
<th data-sort-type="number">Rank
</th>
<th>Bank name
</th>
<th>Total assets<br/>(2025)<br/>(<a class="mw-redirect" href="/web/20251007065341/https://en.wikipedia.org/wiki/US$" title="US$">US$</a> billion)
</th></tr>
soup_data[0].data
soup_data[0].text
'\nRank\n\nBank name\n\nTotal assets(2025)(US$ billion)\n'
soup_data[0].find_all('td')
[]
soup_data[1].find_all('td')
[<td>1
</td>, <td><span class="flagicon"><span class="mw-image-border" typeof="mw:File"><a href="/web/20251007065341/https://en.wikipedia.org/wiki/China" title="China"><img alt="China" class="mw-file-element" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/40px-Flag_of_the_People%27s_Republic_of_China.svg.png" srcset="//web.archive.org/web/20251007065341im_/https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/60px-Flag_of_the_People%27s_Republic_of_China.svg.png 2x" width="23"/></a></span></span> <a href="/web/20251007065341/https://en.wikipedia.org/wiki/Industrial_and_Commercial_Bank_of_China" title="Industrial and Commercial Bank of China">Industrial and Commercial Bank of China</a>
</td>, <td>6,688.74
</td>]
soup_data[1].find_all('td').text
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    soup_data[1].find_all('td').text
  File "E:\Python(latest)\Lib\site-packages\bs4\element.py", line 3203, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute "text". You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
soup_data[1].text
'\n1\n\n Industrial and Commercial Bank of China\n\n6,688.74\n'
soup_data[1].text.split()
['1', 'Industrial', 'and', 'Commercial', 'Bank', 'of', 'China', '6,688.74']
for i in soup_data[1].find_all('td')
SyntaxError: expected ':'
for i in soup_data[1].find_all('td'):
    print(i.text)

1

 Industrial and Commercial Bank of China

6,688.74

for i in soup_data[1::]:
    row = []
    for j in i.find_all('td')
SyntaxError: expected ':'
for i in soup_data[1::]:
    row = []
    for j in i.find_all('td'):
        row.append(j.text)
    print(row)


df = pd.DataFrame(columns =['Rank', 'Bank Name', 'Total Assets 2025($)'])
for i in soup_data[1::]:
    row = []
    for j in i.find_all('td'):
        row.append(j.text)
    df.loc[len(df)] = row

df
     Rank                                   Bank Name Total Assets 2025($)
0     1\n   Industrial and Commercial Bank of China\n           6,688.74\n
1     2\n                Agricultural Bank of China\n           5,923.76\n
2     3\n                   China Construction Bank\n           5,558.38\n
3     4\n                             Bank of China\n           4,803.51\n
4     5\n                            JPMorgan Chase\n           4,002.81\n
..    ...                                         ...                  ...
95   96\n                                 SEB Group\n             339.65\n
96   97\n                          Raiffeisen Group\n             337.25\n
97   98\n                            Banco Bradesco\n             331.96\n
98   99\n                                  VTB Bank\n             330.43\n
99  100\n                      First Abu Dhabi Bank\n             330.32\n

[100 rows x 3 columns]
>>> for i in soup_data[1::]:
...     row = []
...     for j in i.find_all('td'):
...         row.append(j.text)
...     print(row, end=',')
... 
['1\n', ' Industrial and Commercial Bank of China\n', '6,688.74\n'],['2\n', ' Agricultural Bank of China\n', '5,923.76\n'],['3\n', ' China Construction Bank\n', '5,558.38\n'],['4\n', ' Bank of China\n', '4,803.51\n'],['5\n', ' JPMorgan Chase\n', '4,002.81\n'],['6\n', ' Bank of America\n', '3,261.52\n'],['7\n', ' HSBC\n', '2,989.81\n'],['8\n', ' BNP Paribas\n', '2,809.83\n'],['9\n', ' Crédit Agricole\n', '2,693.58\n'],['10\n', ' Mitsubishi UFJ Financial Group\n', '2,628.12\n'],['11\n', ' Postal Savings Bank of China\n', '2,340.69\n'],['12\n', ' Citigroup\n', '2,151.95\n'],['13\n', ' Bank of Communications\n', '2,041.45\n'],['14\n', ' SMBC Group\n', '1,977.18\n'],['15\n', ' Wells Fargo\n', '1,929.85\n'],['16\n', ' Banco Santander\n', '1,901.94\n'],['17\n', ' Barclays\n', '1,900.67\n'],['18\n', ' Mizuho Financial Group\n', '1,805.52\n'],['19\n', ' Goldman Sachs\n', '1,675.97\n'],['20\n', ' China Merchants Bank\n', '1,664.87\n'],['21\n', ' Groupe BPCE\n', '1,646.53\n'],['22\n', ' Société Générale\n', '1,601.74\n'],['23\n', ' UBS\n', '1,563.32\n'],['24\n', ' Japan Post Bank\n', '1,546.95\n'],['25\n', ' Royal Bank of Canada\n', '1,513.86\n'],['26\n', ' Toronto-Dominion Bank\n', '1,446.51\n'],['27\n', ' Industrial Bank\n', '1,439.62\n'],['28\n', ' Deutsche Bank\n', '1,436.15\n'],['29\n', ' China CITIC Bank\n', '1,306.01\n'],['30\n', ' Shanghai Pudong Development Bank\n', '1,296.31\n'],['31\n', ' Crédit Mutuel\n', '1,252.10\n'],['32\n', ' Morgan Stanley\n', '1,215.07\n'],['33\n', ' Lloyds Banking Group\n', '1,135.12\n'],['34\n', ' China Minsheng Bank\n', '1,070.68\n'],['35\n', ' ING Group\n', '1,056.57\n'],['36\n', ' Bank of Montreal\n', '1,014.36\n'],['37\n', ' Scotiabank\n', '978.47\n'],['38\n', ' Intesa Sanpaolo\n', '966.23\n'],['39\n', ' China Everbright Bank\n', '953.41\n'],['40\n', ' NatWest Group\n', '886.34\n'],['41\n', ' ANZ Group\n', '852.19\n'],['42\n', ' Standard Chartered\n', '849.69\n'],['43\n', ' State Bank of India\n', '846.64\n'],['44\n', ' UniCredit\n', '811.68\n'],['45\n', ' Commonwealth Bank\n', '809.81\n'],['46\n', ' Banco Bilbao Vizcaya Argentaria\n', '799.67\n'],['47\n', ' Ping An Bank\n', '790.41\n'],['48\n', ' La Banque postale\n', '766.91\n'],['49\n', ' National Australia Bank\n', '748.98\n'],['50\n', ' Canadian Imperial Bank of Commerce\n', '747.91\n'],['51\n', ' Westpac\n', '747.10\n'],['52\n', ' DZ Bank\n', '682.93\n'],['53\n', ' U.S. Bancorp\n', '678.32\n'],['54\n', ' CaixaBank\n', '653.28\n'],['55\n', ' Rabobank\n', '651.47\n'],['56\n', ' Nordea\n', '645.36\n'],['57\n', ' Capital One\n', '637.78\n'],['58\n', ' DBS Group\n', '606.13\n'],['59\n', ' Huaxia Bank\n', '599.59\n'],['60\n', ' Commerzbank\n', '574.23\n'],['61\n', ' Bank of Beijing\n', '574.14\n'],['62\n', ' Norinchukin Bank\n', '560.75\n'],['63\n', ' PNC Financial Services\n', '560.04\n'],['64\n', ' Sberbank of Russia\n', '557.48\n'],['65\n', ' Bank of Jiangsu\n', '541.41\n'],['66\n', ' Truist Financial Corp\n', '531.18\n'],['67\n', ' Danske Bank\n', '515.87\n'],['68\n', ' KB Financial Group\n', '513.01\n'],['69\n', ' Shinhan Financial Group\n', '500.77\n'],['70\n', ' Nationwide Building Society\n', '498.77\n'],['71\n', ' Sumitomo Mitsui Trust Holdings\n', '498.16\n'],['72\n', ' China Guangfa Bank\n', '494.93\n'],['73\n', ' HDFC Bank\n', '494.06\n'],['74\n', ' Itaú Unibanco\n', '492.90\n'],['75\n', ' Resona Holdings\n', '491.13\n'],['76\n', ' Charles Schwab Corporation\n', '479.84\n'],['77\n', ' Oversea-Chinese Banking Corporation\n', '458.00\n'],['78\n', ' China Zheshang Bank\n', '455.61\n'],['79\n', ' Bank of Shanghai\n', '442.06\n'],['80\n', ' Hana Financial Group\n', '431.78\n'],['81\n', ' Bank of Ningbo\n', '428.16\n'],['82\n', ' Nonghyup Bank\n', '419.37\n'],['83\n', ' BNY Mellon\n', '416.06\n'],['84\n', ' ABN AMRO\n', '411.66\n'],['85\n', ' United Overseas Bank\n', '393.97\n'],['86\n', ' Banco do Brasil\n', '393.52\n'],['87\n', ' Woori Financial Group\n', '393.34\n'],['88\n', ' KBC Group\n', '386.22\n'],['89\n', ' Nomura Holdings\n', '385.00\n'],['90\n', ' Landesbank Baden-Württemberg\n', '368.98\n'],['91\n', ' Erste Group\n', '366.22\n'],['92\n', ' National Bank of Canada\n', '365.25\n'],['93\n', ' State Street Corporation\n', '362.95\n'],['94\n', ' Qatar National Bank\n', '356.52\n'],['95\n', ' Bank of Nanjing\n', '355.03\n'],['96\n', ' SEB Group\n', '339.65\n'],['97\n', ' Raiffeisen Group\n', '337.25\n'],['98\n', ' Banco Bradesco\n', '331.96\n'],['99\n', ' VTB Bank\n', '330.43\n'],['100\n', ' First Abu Dhabi Bank\n', '330.32\n'],
for i in df:
    print(i)

Rank
Bank Name
Total Assets 2025($)
df
     Rank                                   Bank Name Total Assets 2025($)
0     1\n   Industrial and Commercial Bank of China\n           6,688.74\n
1     2\n                Agricultural Bank of China\n           5,923.76\n
2     3\n                   China Construction Bank\n           5,558.38\n
3     4\n                             Bank of China\n           4,803.51\n
4     5\n                            JPMorgan Chase\n           4,002.81\n
..    ...                                         ...                  ...
95   96\n                                 SEB Group\n             339.65\n
96   97\n                          Raiffeisen Group\n             337.25\n
97   98\n                            Banco Bradesco\n             331.96\n
98   99\n                                  VTB Bank\n             330.43\n
99  100\n                      First Abu Dhabi Bank\n             330.32\n

[100 rows x 3 columns]
df.all
<bound method DataFrame.all of      Rank                                   Bank Name Total Assets 2025($)
0     1\n   Industrial and Commercial Bank of China\n           6,688.74\n
1     2\n                Agricultural Bank of China\n           5,923.76\n
2     3\n                   China Construction Bank\n           5,558.38\n
3     4\n                             Bank of China\n           4,803.51\n
4     5\n                            JPMorgan Chase\n           4,002.81\n
..    ...                                         ...                  ...
95   96\n                                 SEB Group\n             339.65\n
96   97\n                          Raiffeisen Group\n             337.25\n
97   98\n                            Banco Bradesco\n             331.96\n
98   99\n                                  VTB Bank\n             330.43\n
99  100\n                      First Abu Dhabi Bank\n             330.32\n

[100 rows x 3 columns]>
for i in range(len(df)):
    print(i)


for i in range(len(df)):
    print(df[i])

Traceback (most recent call last):
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    print(df[i])
  File "E:\Python(latest)\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "E:\Python(latest)\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 0
KeyboardInterrupt
for i in range(len(df)):
    print(df.loc[i])

    

for i in range(90,len(df)):
    print(type(df.loc[i]))

    
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
for i in range(90,len(df)):
    print(type(df.get()))

    
Traceback (most recent call last):
  File "<pyshell#74>", line 2, in <module>
    print(type(df.get()))
TypeError: NDFrame.get() missing 1 required positional argument: 'key'
for i in range(90,len(df)):
    print(df.get('Bank Name'), df.get('Total Assets 2025($)'))

    

for i in range(98,len(df)):
    print(df.attrs)

    
{}
{}
for i in range(98,len(df)):
    print(df.attrs())

    
Traceback (most recent call last):
  File "<pyshell#82>", line 2, in <module>
    print(df.attrs())
TypeError: 'dict' object is not callable
df.iat(0,0)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    df.iat(0,0)
TypeError: '_iAtIndexer' object is not callable
df.iat[0,0]
'1\n'
df.iat[0,2]
'6,688.74\n'
type(df.iat[0,2])
<class 'str'>
int(df.iat[0,2])
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    int(df.iat[0,2])
ValueError: invalid literal for int() with base 10: '6,688.74\n'
df.iat[0,2].replace(',','')
'6688.74\n'
int(df.iat[0,2].replace(',',''))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    int(df.iat[0,2].replace(',',''))
ValueError: invalid literal for int() with base 10: '6688.74\n'
df.iat[0,2].replace(',','').replace('\n','')
'6688.74'
float(df.iat[0,2].replace(',','').replace('\n',''))
6688.74
np.round(892.98983, decimals = 3)
np.float64(892.99)
np.round(4389.948,2)
np.float64(4389.95)
