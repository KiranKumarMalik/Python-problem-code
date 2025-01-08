import sqlite3
con_obj=sqlite3.connect('demo.db')
cur_obj=con_obj.cursor()
cur_obj.execute('create table python(id number primary key,name varchar,mock varchar)')
cur_obj.execute('insert into python values(1,"Kiran","P1")')
cur_obj.execute('insert into python values(2,"Sagar","P2")')
cur_obj.execute('insert into python values(3,"Ravi","P3")')
con_obj.commit()
records=cur_obj.execute('select * from python')
for _ in records:
    print(_)
cur_obj.execute('update python set name="Raj" where id=3')
records=cur_obj.execute('select * from python')
for _ in records:
    print(_)
cur_obj.execute('delete from python where id=2')
records=cur_obj.execute('select * from python')
for _ in records:
    print(_)