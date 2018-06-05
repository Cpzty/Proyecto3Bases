import csv
import psycopg2
conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('album.csv', 'w') as f:
    cur.copy_to(f, '"Album"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('artist.csv', 'w') as f: 
    cur.copy_to(f, '"Artist"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('customer.csv', 'w') as f:
    cur.copy_to(f, '"Customer"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('employee.csv', 'w') as f:
    cur.copy_to(f, '"Employee"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('genre.csv', 'w') as f:
    cur.copy_to(f, '"Genre"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('invoice.csv', 'w') as f:
    cur.copy_to(f, '"Invoice"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('invoiceline.csv', 'w') as f:
    cur.copy_to(f, '"InvoiceLine"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('mediatype.csv', 'w') as f:
    cur.copy_to(f, '"MediaType"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('playlist.csv', 'w') as f:
    cur.copy_to(f, '"Playlist"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('playlisttrack.csv', 'w') as f:
    cur.copy_to(f, '"PlaylistTrack"',sep = ";")
conn.commit()
conn.close()

conn = psycopg2.connect("dbname=proyecto user=postgres host =localhost password = admin")
cur = conn.cursor()
with open('track.csv', 'w') as f:
    cur.copy_to(f, '"Track"',sep = ";")
conn.commit()
conn.close()

