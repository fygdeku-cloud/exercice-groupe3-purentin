import csv
import pandas

#List of products
dataframe=pandas.read_csv('sales.csv', delimiter=',')

#Resume of the consoles
print("=============Vos produits vendu=============")
print(dataframe)

#Tunover
Tprice=0
Tquantity=0
for index,ligne in dataframe.iterrows():
    Tprice+=ligne['price']
    Tquantity+=ligne['quantity']
    
turnover=Tprice*Tquantity
print('=========== Son chiffre daffaire est : ',turnover,'FCFA')


# The best selling products
max=int(dataframe.at[0,'quantity'])
for index,ligne in dataframe.iterrows():
    if max < int(ligne['quantity']):
        max=ligne['quantity']
        max_index=index
max=dataframe.at[max_index,'product']       
print('===========Le produit le plus vendu est : ',max)



