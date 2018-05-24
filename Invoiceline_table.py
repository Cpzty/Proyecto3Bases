import psycopg2
from faker import Faker
fake = Faker()
from random import randint
import random
count = 5

def retrieve_Last_InvoiceLineId():
    #conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    conn = psycopg2.connect("dbname=kappatalism user=postgres host=localhost password=j66352769")
    cur = conn.cursor()
    concat = '"InvoiceLine"'
    name = '"InvoiceLineId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean

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

def retrieve_Last_TrackId():
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Track"'
    name = '"TrackId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()

print(retrieve_Last_InvoiceLineId())
