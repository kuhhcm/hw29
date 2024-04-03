import psycopg2

def connect_to_db():
    connect = psycopg2.connect(host = '127.0.0.1', port = 5432, dbname = 'postgres', user = 'postgres', password = 'postgres')
    return connect

connection = connect_to_db()
cursor = connection.cursor()



def create():
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    year = int(input("Enter year: "))
    price = int(input("Enter price: "))
    create = f"insert into games values ( {id}, '{name}', {year}, {price})"
    cursor.execute(create)
    connection.commit()


def read_all():
    read = "select * from games"
    cursor.execute(read)
    rows = cursor.fetchall()
    print(rows)


def read_one():
    id = int(input("Enter id you want to read: "))
    read_only_one =  f"select * from games where id = {id}"
    cursor.execute(read_only_one)
    row = cursor.fetchall()
    print(row)
    

def update():
    id = int(input('Enter id you want to update: '))
    name = input('Enter name: ')
    price = input('Enter price: ')
    year = int(input("Enter year: "))
    update = f"update games set name = '{name}', price= {price}, year = '{year}' where id = {id}"
    cursor.execute(update)
    connection.commit()
   
    
def delete():
    id = int(input("Enter id you want to delete: "))
    delete = f"delete from games where id = {id}"
    cursor.execute(delete)
    connection.commit()
    
    

choice = input("Select an action: \n\n1. Create\n2. Read all rows\n3. Read one row\n4. Update\n5. Delete\n\n ")
match choice:
    case "1":
        create()
    case "2":
        read_all()
    case "3":
        read_one()
    case "4":
        update()
    case "5":
        delete()
