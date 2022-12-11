# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:04:20 2022

@author: steve
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def getdata(filename):
    '''
    

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    ------- 
    df : TYPE
        DESCRIPTION.
    df2 : TYPE
        DESCRIPTION.

    '''
    df = pd.read_csv(filename, skiprows=(4), index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[df['Country Name'].isin(countries)]
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'], var_name='Years')
    
    del df2['Country Code']
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],'Country Name').reset_index()

    return df, df2

#df2.to_excel('test_data.xlsx')
countries = ['Australia','France','United States', 'Ireland']

#For Piechart
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('SP.POP.GROW')]
print(df2)

#df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.CO2E.SF.ZS')
#df2.dropna()



Aus= np.sum(df2['Australia'])
Fran= np.sum(df2['France'])
US= np.sum(df2['United States'])
Ire= np.sum(df2["Ireland"])

total= Aus + Fran + US + Ire


Aus_obs= Aus/ total*100
Fran_obs= Fran/ total*100
US_obs= US/ total*100
Ire_obs= Ire/ total*100

popu_growth= np.array([Aus_obs, Fran_obs, US_obs, Ire_obs])


plt.figure(dpi=144)
plt.pie(popu_growth, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Population growth (annual %)") # This function is for showing title of data
plt.show()

#For Barplot

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.USE.ELEC.KH.PC')]
df2.dropna()
print(df2)
#df2.to_excel('test_data5.xlsx')



df2 = df2.loc[df2['Years'].isin(['2000','2002','2004','2006','2008'])]
num = np.arange(5)
width = 0.2
years = df2['Years'].tolist()

plt.figure(dpi=120)
plt.title('Electric power consumption (kWh per capita)')
plt.bar(num+0.2, df2['Australia'], width, label='Australia')
plt.bar(num-0.2, df2['France'], width, label='France')
plt.bar(num+0.4, df2['United States'], width, label='United States')
plt.bar(num-0.2, df2['Ireland'], width, label='Ireland')
plt.xticks(num, years)
#plt.yticks(np.arange(100,6000,1000))
plt.xlabel('Years')
plt.ylabel('kWh per capita')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()


#for Lineplot
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.RNEW.ZS')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Renewable electricity output (% of total electricity output)')
plt.ylabel('% of total electricity output')
plt.show()





# Line plot2
#for Lineplot
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.PETR.ZS')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Electricity production from oil sources (% of total)')
plt.ylabel('% of total')
plt.show()
#####
###line plot3
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.NUCL.ZS')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Electricity production from nuclear sources (% of total)')
plt.ylabel('% of total')
plt.show()
########################
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.COAL.ZS')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Electricity production from coal sources (% of total)')
plt.legend(loc='lower left',bbox_to_anchor=(1,0.5))
plt.ylabel('% of total')
plt.show()
##################################
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.NGAS.ZS')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Electricity production from natural gas sources (% of total)')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.ylabel('% of total')
plt.show()

####
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EN.ATM.CO2E.PC')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='CO2 emissions (metric tons per capita)')
plt.legend(loc='lower left',bbox_to_anchor=(1,0.5))
plt.ylabel('metric tons per capita')
plt.show()
print(df.info())
print(df2.info()) 
