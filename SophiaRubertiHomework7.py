#Sophia Ruberti Homework 7
#Part A
import pandas as pd
customer = {'name': 'Orwell', 'address':'4 Church St', 'age':'45'}
#find and print address
# print(customer['address'])

#add new key-value
customer['birthday'] = '25 June'

#change value
customer['name']='George Orwell'

#print changes
# print(customer)

#Part B
phonebook = {
            'Euclid': {'number':'212.479.2851'}
            , 'Pythagoras': {'number':'212.479.4653'}
            , 'Avicenna': {'number':'212.892.1234'}
            , 'Descartes': {'number':'917.372.1650'}
            }

#get Newton
result = phonebook.get('Newton')
if result is not None:
    print(result)
else:
    print('Name not found')

#add to dict
if result is not None:
    print(result)
else:
    phonebook['Newton'] = {'number':'917.364.1727'}

#change number
phonebook.update({'Avicenna':{'number':'212.472.1037'}})
   
#remove
del phonebook['Descartes']

#print names
for key, value in phonebook.items():
    print(key, phonebook[key]['number'])

#Part C
phonebookDF = pd.DataFrame(phonebook)
print(phonebookDF.transpose())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    