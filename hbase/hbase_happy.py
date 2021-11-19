import happybase as hb
con = hb.Connection('localhost')
con.open()
# con.create_table('py_table',{'cf1':dict(max_versions=10),
#                             'cf2':dict()})
# print(con.tables())
table=con.table('py_table')
table.put(b'1',{b'cf1:fname':b'Bob',
                b'cf1:lname':b'Moult',
                b'cf2:job':b'Engineer'})

for k,v in table.scan():
    print(k,v)

b=table.batch()
b.put(b'1',{b'cf1:fname':b'Bob',
                b'cf1:lname':b'Moult',
                b'cf2:job':b'Engineer'})
b.put(b'1',{b'cf1:fname':b'Bob',
                b'cf1:lname':b'Moult',
                b'cf2:job':b'Engineer'})
b.send()

for k,v in table():
    print(k,v)