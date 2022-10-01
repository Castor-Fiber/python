import pandas as p

print('----'*30)
print('Report card')

s_card = {
        'ID': ['01','02','03','04','05'],
        'First name' : ['Ivan','Peter','Sidr','Helga','Catherine'],
        'Second name': ['Ivanov','Petrov','Sidorov','Smolanova','Andreeva'],
        'Date of birth' : ['09.10.2001','05.04.2001','04.01.2001','29.03.2001','19.12.2001'],
        'Perfomance' : ['Excellent student','Satisfactory student','Good student','Excellent student','Good student']
}
    
sc = p.DataFrame(data = s_card)

with open('stud.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)
