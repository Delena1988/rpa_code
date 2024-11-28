import cx_Oracle

user = 'system'
password = '123456'
host = '192.168.3.158:1521'
service_name = 'orcl'
conn_str = f"{user}/{password}@{host}/{service_name}"  # ('system/system@172.24.0.64:1521/helowinXDB')
connect = cx_Oracle.connect(conn_str)
cursor = connect.cursor()
cursor.execute('select * from mytesttable')
print(cursor.fetchall())
