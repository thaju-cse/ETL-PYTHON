import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime


def extract(url, head):
    print("Started Extraction of data..")

    web_text = requests.get(url).text
    soup_web = BeautifulSoup(web_text, 'html.parser')
    soup_tables = soup_web.find_all('table')

    soup_table = soup_tables[0].find_all('tr')
    #print(soup_table)
    table_data_frame = pd.DataFrame(columns = head)

    for row in soup_table[1::]:
        row_list = []
        for element in row.find_all('td'):
            row_list.append(element.text)
            #print(row_list)

        table_data_frame.loc[len(table_data_frame)] = row_list

    print("Data frame creation Successful..")

    logging('extract')
    return table_data_frame
    
def transform(frame, col, variation):
    print("Transforming process started..")

    transformed_data_frame = pd.DataFrame(columns = col)

    GBP = variation['GBP']
    EUR= variation['EUR']
    INR = variation['INR']
    for i in range(len(frame)):
        dollar = float(frame.iat[i,2].replace(',','').replace('\n',''))
        gbp = np.round(dollar*GBP, decimals = 2)
        eur = np.round(dollar*EUR, decimals = 2)
        inr = np.round(dollar*INR, decimals = 2)
        transformed_data_frame.loc[i] = [i+1 ,frame.iat[i,1], dollar, gbp, eur, inr]

    print("Data Transformed Successfully..")

    logging('transform')
    return transformed_data_frame


def load(frame):
    print("Started loading process..")

    db_name = 'top_10_world_banks.db'
    table_name = 'top_10_world_banks'
    csv_file = 'top_10_world_banks.csv'

    with open(csv_file, 'w') as file:
        frame.to_csv(file, sep = ',')

    print("CSV file creted successfully..")

    conn = sqlite3.connect(db_name)
    frame.to_sql(table_name, conn, if_exists = 'replace', index= False)
    conn.close()
    print("Table created in DB successfully..")

    logging('load')
    return True

def logging(value):
    file = 'log_book.txt'
    
    if value == 'extract':
        with open(file, 'a') as f:
            f.write(str(datetime.now())+ ' : Extracted data from the web and returned a DtaFrame.\n\n')

    elif value == 'transform':
        with open(file, 'a') as f:
            f.write(str(datetime.now())+ ' : Data Transformed and returned a DataFrame.\n\n')
            
    elif value == 'load':
        with open(file, 'a') as f:
            f.write(str(datetime.now())+ ' : A CSV file and a Table created.\n\n')
            
    elif value == 'query':
        with open(file, 'a') as f:
            f.write(str(datetime.now())+ ' : Query Execution completed.\n\n')
            
    else:
        with open(file, 'a') as f:
            f.write(str(datetime.now())+ ' : Something has Done now.\n\n')
            
    print("\nLogged Exection Details successfully..\n")

    return True

def querying(query, db_name):
    conn = sqlite3.connect(db_name)
    ans = pd.read_sql(query, conn)
    print("Query executed successfully..")

    logging('query')
    return ans


def main():
    url = 'https://web.archive.org/web/20251007065341/https://en.wikipedia.org/wiki/List_of_largest_banks'
    head = ['Rank', 'Bank Name', 'Total Assets 2025($)']
    table_data_frame = extract(url, head)

    #soup_table =['1\n', ' Industrial and Commercial Bank of China\n', '6,688.74\n'],['2\n', ' Agricultural Bank of China\n', '5,923.76\n'],['3\n', ' China Construction Bank\n', '5,558.38\n'],['4\n', ' Bank of China\n', '4,803.51\n'],['5\n', ' JPMorgan Chase\n', '4,002.81\n'],['6\n', ' Bank of America\n', '3,261.52\n'],['7\n', ' HSBC\n', '2,989.81\n'],['8\n', ' BNP Paribas\n', '2,809.83\n'],['9\n', ' Crédit Agricole\n', '2,693.58\n'],['10\n', ' Mitsubishi UFJ Financial Group\n', '2,628.12\n'],['11\n', ' Postal Savings Bank of China\n', '2,340.69\n'],['12\n', ' Citigroup\n', '2,151.95\n'],['13\n', ' Bank of Communications\n', '2,041.45\n'],['14\n', ' SMBC Group\n', '1,977.18\n'],['15\n', ' Wells Fargo\n', '1,929.85\n'],['16\n', ' Banco Santander\n', '1,901.94\n'],['17\n', ' Barclays\n', '1,900.67\n'],['18\n', ' Mizuho Financial Group\n', '1,805.52\n'],['19\n', ' Goldman Sachs\n', '1,675.97\n'],['20\n', ' China Merchants Bank\n', '1,664.87\n'],['21\n', ' Groupe BPCE\n', '1,646.53\n'],['22\n', ' Société Générale\n', '1,601.74\n'],['23\n', ' UBS\n', '1,563.32\n'],['24\n', ' Japan Post Bank\n', '1,546.95\n'],['25\n', ' Royal Bank of Canada\n', '1,513.86\n'],['26\n', ' Toronto-Dominion Bank\n', '1,446.51\n'],['27\n', ' Industrial Bank\n', '1,439.62\n'],['28\n', ' Deutsche Bank\n', '1,436.15\n'],['29\n', ' China CITIC Bank\n', '1,306.01\n'],['30\n', ' Shanghai Pudong Development Bank\n', '1,296.31\n'],['31\n', ' Crédit Mutuel\n', '1,252.10\n'],['32\n', ' Morgan Stanley\n', '1,215.07\n'],['33\n', ' Lloyds Banking Group\n', '1,135.12\n'],['34\n', ' China Minsheng Bank\n', '1,070.68\n'],['35\n', ' ING Group\n', '1,056.57\n'],['36\n', ' Bank of Montreal\n', '1,014.36\n'],['37\n', ' Scotiabank\n', '978.47\n'],['38\n', ' Intesa Sanpaolo\n', '966.23\n'],['39\n', ' China Everbright Bank\n', '953.41\n'],['40\n', ' NatWest Group\n', '886.34\n'],['41\n', ' ANZ Group\n', '852.19\n'],['42\n', ' Standard Chartered\n', '849.69\n'],['43\n', ' State Bank of India\n', '846.64\n'],['44\n', ' UniCredit\n', '811.68\n'],['45\n', ' Commonwealth Bank\n', '809.81\n'],['46\n', ' Banco Bilbao Vizcaya Argentaria\n', '799.67\n'],['47\n', ' Ping An Bank\n', '790.41\n'],['48\n', ' La Banque postale\n', '766.91\n'],['49\n', ' National Australia Bank\n', '748.98\n'],['50\n', ' Canadian Imperial Bank of Commerce\n', '747.91\n'],['51\n', ' Westpac\n', '747.10\n'],['52\n', ' DZ Bank\n', '682.93\n'],['53\n', ' U.S. Bancorp\n', '678.32\n'],['54\n', ' CaixaBank\n', '653.28\n'],['55\n', ' Rabobank\n', '651.47\n'],['56\n', ' Nordea\n', '645.36\n'],['57\n', ' Capital One\n', '637.78\n'],['58\n', ' DBS Group\n', '606.13\n'],['59\n', ' Huaxia Bank\n', '599.59\n'],['60\n', ' Commerzbank\n', '574.23\n'],['61\n', ' Bank of Beijing\n', '574.14\n'],['62\n', ' Norinchukin Bank\n', '560.75\n'],['63\n', ' PNC Financial Services\n', '560.04\n'],['64\n', ' Sberbank of Russia\n', '557.48\n'],['65\n', ' Bank of Jiangsu\n', '541.41\n'],['66\n', ' Truist Financial Corp\n', '531.18\n'],['67\n', ' Danske Bank\n', '515.87\n'],['68\n', ' KB Financial Group\n', '513.01\n'],['69\n', ' Shinhan Financial Group\n', '500.77\n'],['70\n', ' Nationwide Building Society\n', '498.77\n'],['71\n', ' Sumitomo Mitsui Trust Holdings\n', '498.16\n'],['72\n', ' China Guangfa Bank\n', '494.93\n'],['73\n', ' HDFC Bank\n', '494.06\n'],['74\n', ' Itaú Unibanco\n', '492.90\n'],['75\n', ' Resona Holdings\n', '491.13\n'],['76\n', ' Charles Schwab Corporation\n', '479.84\n'],['77\n', ' Oversea-Chinese Banking Corporation\n', '458.00\n'],['78\n', ' China Zheshang Bank\n', '455.61\n'],['79\n', ' Bank of Shanghai\n', '442.06\n'],['80\n', ' Hana Financial Group\n', '431.78\n'],['81\n', ' Bank of Ningbo\n', '428.16\n'],['82\n', ' Nonghyup Bank\n', '419.37\n'],['83\n', ' BNY Mellon\n', '416.06\n'],['84\n', ' ABN AMRO\n', '411.66\n'],['85\n', ' United Overseas Bank\n', '393.97\n'],['86\n', ' Banco do Brasil\n', '393.52\n'],['87\n', ' Woori Financial Group\n', '393.34\n'],['88\n', ' KBC Group\n', '386.22\n'],['89\n', ' Nomura Holdings\n', '385.00\n'],['90\n', ' Landesbank Baden-Württemberg\n', '368.98\n'],['91\n', ' Erste Group\n', '366.22\n'],['92\n', ' National Bank of Canada\n', '365.25\n'],['93\n', ' State Street Corporation\n', '362.95\n'],['94\n', ' Qatar National Bank\n', '356.52\n'],['95\n', ' Bank of Nanjing\n', '355.03\n'],['96\n', ' SEB Group\n', '339.65\n'],['97\n', ' Raiffeisen Group\n', '337.25\n'],['98\n', ' Banco Bradesco\n', '331.96\n'],['99\n', ' VTB Bank\n', '330.43\n'],['100\n', ' First Abu Dhabi Bank\n', '330.32\n'],
    #table_data_frame = pd.DataFrame(columns = head)
    '''for row in soup_table[0:5]:
        row_list = []
        for element in row:
            row_list.append(element)
            #print(row_list)

        table_data_frame.loc[len(table_data_frame)] = row_list
    #print(table_data_frame)'''
    col = ['Rank', 'Bank Name', 'Total Assets($)', 'Toatal Assests in GBP', 'Total Assets in EUR', 'Toatal Assets in INR']
    variation = {'GBP': 0.76, 'EUR': 0.86, 'INR': 90.24}
    transformed_data_frame = transform(table_data_frame, col, variation )
    
    #print(transformed_data_frame.iat[0,0])

    db_name = 'top_10_world_banks.db'
    table_name = 'top_10_world_banks'
    csv_file = 'top_10_world_banks.csv'
    print(load(transformed_data_frame))   

    query = 'select * from ' + table_name +' limit 10'
    print(querying(query, db_name))
    print("*****Completed*****")

if __name__ == '__main__':
    main()
