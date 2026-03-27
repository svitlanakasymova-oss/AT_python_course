import psycopg2

DB_HOST = "ep-small-voice-ab051c1n-pooler.eu-west-2.aws.neon.tech"
DB_PORT = "5432"
DB_NAME = "neondb"
DB_USER = "neondb_owner"
DB_PASSWORD = "npg_nxQh5Zv3zEaK"

#встановлюємо звʼязок з БД
def establish_connection():
    try:
        connection = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                                      sslmode="require")
        return connection
    except Exception as e:
        print(e)


#Витягуємо всі продукти з назвами категорій, до яких вони належать
def basic_products_desc(connection):
    cursor = connection.cursor()
    cursor.execute("""select p.id, p."name" as Product, c."name" as Category, p.price from products p
    join categories c on p.category_id = c.id;""")
    data = cursor.fetchall()
    for record in data:
        print(record)


#Витягуємо всі продукти, для яких не вказана кількість товару на складі (вважаємо їх відсутніми)
def get_out_of_stock_products(connection):
    cursor = connection.cursor()
    cursor.execute("""select p.id, p."name" as Product, c."name" as Category, s.quantity from products p
join categories c on p.category_id = c.id 
left join stock s on p.id = s.product_id
where s.quantity is null """)
    data = cursor.fetchall()
    for record in data:
        print(record)

connection = establish_connection()
#basic_products_desc(connection)
#get_out_of_stock_products(connection)