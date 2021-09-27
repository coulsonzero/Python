import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='0627', database='mysql', charset='UTF8MB4')
cursor = conn.cursor()

def doSQL(sql):
    cursor.execute(sql)
    conn.commit()

doSQL('drop database if exists demo;')
doSQL('create DATABASE demo;')
doSQL('drop table if exists test1;')

sql='''
create table if not exists test1(
id int auto_increment,
name varchar(45),
age int,
primary key(id)
)engine=innodb default charset=utf8mb4;
'''
doSQL(sql)

doSQL('delete from test1;')
for i in range(10):
    sql = 'insert into test1(name) value("名字{0}");'.format(1)
    cursor.execute(sql)
conn.commit()

sql='select * from test1'
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()