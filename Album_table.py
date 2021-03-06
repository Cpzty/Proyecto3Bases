import psycopg2
from faker import Faker
fake = Faker()

def retrieve_All():
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    query = "SELECT *"+"from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nRows: \n")
    for row in rows:
        print ("   ", row[0],"   ",row[1],"   ",row[2])
    conn.commit()
    conn.close()
#retrieve_All()
def retrieve_Id():
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"AlbumId"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando Id:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
#retrieve_Id()

def retrieve_Last_Id():
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"AlbumId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean

def retrieve_Last_ArtistId():
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"ArtistId"'
    query = "SELECT"+name+ "from"+concat+"ORDER BY"+name+" desc limit 1;"
    cur.execute(query)
    rows = cur.fetchall()
    clean = str(rows[0]).replace('(','')
    clean = clean.replace(',','')
    clean = clean.replace(')','')
    conn.commit()
    conn.close()
    return clean

def retrieve_Title():
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"Title"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando Id:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
#retrieve_Title()
def retrieve_ArtistId():
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    name = '"ArtistId"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nMostrando Id:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    conn.close()
#retrieve_ArtistId()
def Insert_Album():
    album_id = retrieve_Last_Id()
    artist_id = retrieve_Last_ArtistId()
    conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
    cur = conn.cursor()
    concat = '"Album"'
    field1 = '"AlbumId"'
    field2 = '"Title"'
    field3 = '"ArtistId"'
    artist = fake.name()
    artist = "'"+artist+"'"
    id_pos = int(album_id)+1
    id_pos = str(id_pos)
    id_pos2 = int(artist_id)+1
    id_pos2 = str(id_pos2)
    query = "INSERT INTO "+concat+"("+field1+","+field2+","+field3+")"+" values("+id_pos+","+artist+","+id_pos2+");"
    cur.execute(query)
    #print ("\nInsercion hecha con exito\n")
    conn.commit()
    conn.close()
#Insert_Album()
