import psycopg2
import glob
conn = psycopg2.connect('postgres://oynkonierltdgy:2e6c52a982ebe5d83448dd0f2a0a59115d028e9e6d1d2a394c713953e13c87ba@ec2-107-22-238-112.compute-1.amazonaws.com:5432/da7522agbf56fl')
cur = conn.cursor()




value = [] 
{value.append(file.split('\\')[1].split('.')[0]) for file in glob.glob("w_seltexts\*.txt")} 
# print(value)
# cur.execute("""CREATE TABLE dr(text CHAR)""")
# cur.execute('SELECT * FROM dr')

for lang in value:
    # id integer PRIMARY KEY,
    # print(lang)
    cur.execute(f"""CREATE TABLE {lang}(
        text CHAR
)
        """)
    with open('w_seltexts/{}.txt'.format(lang), 'r', errors='pass') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                cur.execute(f"INSERT INTO {lang}(text) VALUES {line}") 
            # cur.execute(f"INSERT INTO %s VALUES %s", (lang, line))


conn.commit()