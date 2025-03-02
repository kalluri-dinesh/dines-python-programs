import psycopg2
print(dir(psycopg2))

conn=psycopg2.connect(database="vamsi_db", user = "postgres", password ="1234", host = "127.0.0.1", port = "5432")

cur=conn.cursor()
cur.execute("SELECT * from my_details")
data=cur.fetchall()
print(data)