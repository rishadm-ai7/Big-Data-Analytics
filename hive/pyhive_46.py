from pyhive import hive
cursor=hive.connect(host='localhost',database='batch46').cursor()
cursor.execute('select * from customer')
print(cursor.fetchall())
