import psycopg2
def retrieve_Artists():
    conn = psycopg2.connect("dbname=kappatalism user=postgres host =localhost")
    cur = conn.cursor()
    concat = '"Artist"'
    name = '"Name"'
    query = "SELECT"+name+ "from"+concat+";"
    cur.execute(query)
    rows = cur.fetchall()
    print ("\nShow me the databases:\n")
    for row in rows:
        print ("   ", row[0])
    conn.commit()
    print ("inserted successfully")
    conn.close()

retrieve_Artists()

