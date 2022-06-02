import csv
import psycopg2
import glob
from psycopg2 import sql
from datetime import datetime


conn = psycopg2.connect('postgres://oynkonierltdgy:2e6c52a982ebe5d83448dd0f2a0a59115d028e9e6d1d2a394c713953e13c87ba@ec2-107-22-238-112.compute-1.amazonaws.com:5432/da7522agbf56fl')
cur = conn.cursor()


start_time = datetime.now()
with open('w_seltexts/de2.txt', 'r', errors='replace') as f:
    lines = f.readlines()
    for line in lines:
        if line != '\n':
            line = line.replace('\n','')
            cur.execute(sql.SQL("INSERT INTO de2(words) VALUES (%s)"),(line,))
            end_time = datetime.now()  #put end time where u want to cunt 
print('Duration: {}'.format(end_time - start_time))
                # cur.execute(sql.SQL('SELECT * FROM {}').format(sql.Identifier(lang)))
                # for i in cur.fetchone():
                #     print(i)
                # insert_query = "INSERT INTO {}(words) VALUES {}".format(lang,line)
                # cur.execute(insert_query)
                
#                 # cur.execute('SELECT * FROM de')
#                 cur.execute("INSERT INTO {}(text) VALUES {}".format(lang, line))
#             # cur.execute(f"INSERT INTO %s VALUES %s", (lang, line))


cur.execute('SELECT * FROM de2')
for i in cur.fetchall():
    print(i)
conn.commit()
