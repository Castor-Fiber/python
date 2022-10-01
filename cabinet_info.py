import pandas as p

print('----'*30)
print('Information')

card = {
        'Subject': ['Russian Language','Chemistry','Physics','Biologi','IT'],
        'Place number' : ['1','2','3','4','5'],
        'Row': ['First','Second','Third','Fourth','Fifth'],
        'Place type' : ['Single-placed','Single-placed','Double-placed ','Double-placed ','Single-placed'],
        'ID' : ['01','02','03','04','05']
}
    
c = p.DataFrame(data = card)

with open('cab.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{c}')
        cl.write('\n')
    
print(c)
