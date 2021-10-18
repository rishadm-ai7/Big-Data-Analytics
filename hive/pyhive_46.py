from pyhive import hive
cursor=hive.connect(host='localhost',database='batch46').cursor()
cursor.execute('select * from cust')
print(cursor.fetchall())
