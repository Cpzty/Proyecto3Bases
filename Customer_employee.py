#Customer debe tener una referencia obtenida de Employee para support id
import psycopg2
from faker import Faker
fake = Faker()
from random import randint
import random

def retrieve_last_employee():
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Employee"'
    name = '"EmployeeId"'
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

def insert_employees():
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Employee"'
    field1 = '"EmployeeId"'
    field2 = '"LastName"'
    field3 = '"FirstName"'
    field4 = '"Title"'
    #Del diagrama ER parece que ReportsTo es sobre EmployeeId
    field5 = '"ReportsTo"'
    field6 = '"BirthDate"'
    field7 = '"HireDate"'
    field8 = '"Address"'
    field9 = '"City"'
    field10 = '"State"'
    field11 = '"Country"'
    field12 = '"PostalCode"'
    field13 = '"Phone"'
    field14 = '"Fax"'
    field15 = '"Email"'
    firstlastname = str.split(fake.name())
    first_name = "'"+str(firstlastname[0])+"'"
    last_name = "'"+str(firstlastname[1])+"'"
    employee_pos = int(retrieve_last_employee())+1
    employee_pos = str(employee_pos)
    title_list = ['Sales Support Agent','IT Staff']
    title_pick = randint(0,len(title_list)-1)
    final_title = "'"+title_list[title_pick]+"'"
    if(title_pick == 0):
        reports_to = 2
    else:
        reports_to = 6
    reports_to = "'"+str(reports_to)+"'"
    query = "INSERT INTO "+concat+"("+field1+","+field2+","+field3+","+field4+","+field5+","+field6+","+field7+","+field8+","+field9+","+field10+","+field11+","+field12+","+field13+","+field14+","+field15+")"+" values("+employee_pos+","+last_name+","+first_name+","+final_title+","+reports_to+",'1980-02-20','2004-05-05','923 7 st na','Englang','az','Canada','t1h 1y8','1(403)467-3351','1(780)836-9543','seth@gmail.com');"
    cur.execute(query)
    print ("\nInsercion hecha con exito\n")
    conn.commit()
    conn.close()
    
insert_employees()    
