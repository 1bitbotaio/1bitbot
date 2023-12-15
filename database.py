import sqlite3

clients_db = 'Clients.db'
connection_clients_db = sqlite3.connect(clients_db)
cursor_clients_db = connection_clients_db.cursor()
cursor_clients_db.execute("""
    CREATE TABLE IF NOT EXISTS Clients (
    INN number(15),
    CLient_surname varchar2(30),
    Client_name varchar2(30),
    CLient_patronymic varchar2(30),
    CLient_Date_of_Birth date,
    Client_phonenumber VARCHAR2(20),
    TG_ID VARCHAR2(50),
    CONSTRAINT pk_INN primary key (INN)
    );
    """)
connection_clients_db.commit()
sql = ('''INSERT INTO Clients (INN, CLient_surname, CLient_name, CLient_patronymic, CLient_Date_of_Birth, 
Client_phonenumber, TG_ID) values(?, ?, ?, ?, ?, ?, ?)''')
data = [
    ('6766201793', 'Voronin', 'Ivan', 'Yaroslavovich', '1988-03-15', '89110546783', '0'),
    ('1537504888', 'Pavlova', 'Victoria', 'Evgenievna', '1993-07-24', '89231112344', '0'),
    ('0545609195', 'Berezin', 'Daniil', 'Tihonovich', '1981-11-04', '89157564534', '0'),
    ('7025879893', 'Frolova', 'Ekaterina', 'Denisovna', '1984-03-09', '89560442242', '0'),
    ('9666850374', 'Karasev', 'Vladimir', 'Andreevich', '1978-10-21', '89152347645', '0'),
    ('1071240952', 'Minina', 'Arina', 'Dmitrievna', '1991-12-04', '89413258769', '0'),
    ('7261913011', 'Kozlov', 'Fedor', 'Ruslanovich', '1983-06-12', '89520908762', '0'),
    ('0133096455', 'Kuznetsova', 'Maria', 'Stepanovna', '1988-03-25', '89600607621', '0'),
    ('6050803799', 'Terekhov', 'Ilya', 'Maksimovich', '1970-01-23', '89540445626', '0'),
    ('1207982583', 'Lazareva', 'Margarita', 'Dmitrievna', '1978-06-13', '89412459089', '0')
]
# with connection_clients_db:
#    connection_clients_db.executemany(sql, data)
#
# with connection_clients_db:
#    con = connection_clients_db.execute("SELECT * FROM Clients")
#    for row in data:
#        print(row)


managers_db = 'Managers.db'
connection_managers_db = sqlite3.connect(managers_db)
cursor_managers_db = connection_managers_db.cursor()
cursor_managers_db.execute("""
    CREATE TABLE IF NOT EXISTS Managers (
    ID_Manager number(15),
    Manager_surname varchar2(30),
    Manager_name varchar2(30),
    Manager_patronymic varchar2(30),
    Manager_Date_of_Birth date,
    Department_number number(15),
    Manager_phonenumber varchar2(20),
    Manager_email VARCHAR2(20),
    CONSTRAINT pk_ID_Manager primary key (ID_Manager)
    );
    """)
connection_managers_db.commit()
sql1 = ('''INSERT INTO Managers (ID_Manager, Manager_surname, Manager_name, Manager_patronymic, Manager_Date_of_Birth,
Department_number, Manager_phonenumber, Manager_email) values(?, ?, ?, ?, ?, ?, ?, ?)''')
data1 = [
    ('001', 'Egorov', 'Roman', 'Andreevich', '1994-04-12', '03', '89221346576', 'fabin98858@gyxmz.com'),
    ('002', 'Alekseeva', 'Anna', 'Maksimovna', '1997-02-25', '02', '89514564545', 'lenki0058@gyxmz.com'),
    ('003', 'Astakhov', 'Maksim', 'Alexandrovich', '1990-11-03', '02', '89555256577', 'zaskn58@gyxmz.com'),
    ('004', 'Alekseeva', 'Anna', 'Vladimirovna', '2000-04-13', '03', '89514262221', 'abisdfn9858@gyxmz.com'),
    ('005', 'Solodov', 'Denis', 'Petrovich', '1988-10-16', '02', '89600981344', 'qwan858@gyxmz.com')
]
# with connection_managers_db:
#    connection_managers_db.executemany(sql1, data1)
#
# with connection_managers_db:
#    con = connection_managers_db.execute("SELECT * FROM Managers")
#    for row in data1:
#        print(row)
