import psycopg2
from faker import Faker
fake = Faker()
from random import randint
count =5

def retrieve_Last_InvoiceId():
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Invoice"'
    name = '"InvoiceId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean

def retrieve_Last_CustomerId():
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Customer"'
    name = '"CustomerId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    #print(clean)
    conn.commit()
    conn.close()
    return clean

#retrieve_Last_CustomerId()

def Insert_sale(count):
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Invoice"'
    field1 = '"InvoiceId"'
    field2 = '"CustomerId"'
    field3 = '"InvoiceDate"'
    field4 = '"BillingAddress"'
    field5 = '"BillingCity"'
    field6 = '"BillingState"'
    field7 = '"BillingCountry"'
    field8 = '"BillingPostalCode"'
    field9 = '"Total"'
    id_invoice = retrieve_Last_InvoiceId()
    customer_id = int(retrieve_Last_CustomerId())
    cus_pos = str(randint(1,customer_id ))
    count = count +1
    dia = str(count)
   # if(int(dia) >= 30):
    #    count = 1
     #   dia =str(1)
    date = '2018/06/'+dia
    adress = fake.address()
    adress = "'"+adress+"'"
    date = "'"+date+"'"
    id_pos = int(id_invoice)+1
    id_pos = str(id_pos)
    artist = fake.name()
    artist = "'"+artist+"'"
    cities = ['Stuttgart','Palooza','Guatemala City']
    city_pick = randint(0,len(cities))
    city_pos = "'"+cities[city_pick]+"'"
    query = "INSERT INTO "+concat+"("+field1+","+field2+","+field3+","+field4+","+field5+","+field6+","+field7+","+field8+","+field9+")"+" values("+id_pos+","+cus_pos+","+date+","+adress+","+city_pos+",'8210 111 ST NW','Germany','70174', 1.98);"
    cur.execute(query)
    print ("\nInsercion hecha con exito\n")
    conn.commit()
    conn.close()
def multi_insert(veces):
    i =0
    count =5
    while(i<veces):
        Insert_sale(count)
        count = count+1
        if(count>=30):
            count = 1
        i = i+1
multi_insert(10)

