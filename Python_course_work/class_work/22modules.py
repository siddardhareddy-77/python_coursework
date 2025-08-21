seats = {
    'U1':{'booking_status':True,'gender':'F' ,'price':1220, 'seat_type':'upper' ,'Name':'A','Age':32},
    'U2':{'booking_status':False,'gender':None ,'price':1220, 'seat_type':'upper','Name':None,'Age':None},
    'U3':{'booking_status':True,'gender':'M' ,'price':1220, 'seat_type':'upper','Name':'B','Age':38},
    'U4':{'booking_status':False,'gender':None,'price':1220, 'seat_type':'upper'},
    'U5':{'booking_status':False,'gender':None ,'price':1220, 'seat_type':'upper'},
    'U6':{'booking_status':True,'gender':'F' ,'price':1220, 'seat_type':'upper','Name':'A','Age':32},
    'U7':{'booking_status':True,'gender':'M' ,'price':1220, 'seat_type':'upper','Name':'A','Age':32},
    'U8':{'booking_status':True,'gender':'F' ,'price':1220, 'seat_type':'upper','Name':'A','Age':32}
}

for i in seats:
    if seats[i]['booking_status']:
        if seats[i]['gender']=='M':
            print(f'**{i}**--M')
        else:
            print(f'**{i}**--F')
    else:
        print(f'{i}-1220')