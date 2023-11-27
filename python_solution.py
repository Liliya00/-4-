import sqlite3

#Підключаємося до БД
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#Створюємо medical_record table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medical_record (
        id_record INTEGER PRIMARY KEY AUTOINCREMENT,
        issue_date DATE NOT NULL
    )
''')

cursor.execute("INSERT INTO medical_record (issue_date) VALUES ('2023-11-20')")
cursor.execute("INSERT INTO medical_record (issue_date) VALUES ('2023-11-21')")

#Створюємо driving_school table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS driving_school (
        id_school INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL
    )
''')

cursor.execute("INSERT INTO driving_school (name) VALUES ('Шалені водії')")
cursor.execute("INSERT INTO driving_school (name) VALUES ('За кермом 24/7')")

#Створюємо future_driver table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS future_driver (
        id_future_driver INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL
    )
''')

cursor.execute("INSERT INTO future_driver (name) VALUES ('Петро Гайдаш')")
cursor.execute("INSERT INTO future_driver (name) VALUES ('Олеся Синичко')")

#Створюємо the studying_plan table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS studying_plan (
        id_course_number INTEGER PRIMARY KEY AUTOINCREMENT,
        id_future_driver INT NOT NULL,
        id_school INT NOT NULL,
        FOREIGN KEY (id_school) REFERENCES driving_school (id_school),
        FOREIGN KEY (id_future_driver) REFERENCES future_driver (id_future_driver)
    )
''')

cursor.execute("INSERT INTO studying_plan (id_future_driver, id_school) VALUES (1, 1)")
cursor.execute("INSERT INTO studying_plan (id_future_driver, id_school) VALUES (2, 2)")

#Створюємо test_center table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_center (
        id_mvs INTEGER PRIMARY KEY AUTOINCREMENT,
        test_date DATE NOT NULL,
        FOREIGN KEY (test_date) REFERENCES future_driver (name)
    )
''')
#Обираємо та друкуємо наповнення test_center table
cursor.execute("INSERT INTO test_center (test_date) VALUES ('2023-11-22')")
cursor.execute("INSERT INTO test_center (test_date) VALUES ('2023-11-23')")

#Обираємо та друкуємо наповнення medical_record table
cursor.execute("SELECT * FROM medical_record")
print(cursor.fetchall())

#Обираємо та друкуємо наповнення driving_school table
cursor.execute("SELECT * FROM driving_school")
print(cursor.fetchall())

#Обираємо та друкуємо наповнення future_driver table
cursor.execute("SELECT * FROM future_driver")
print(cursor.fetchall())

#Обираємо та друкуємо наповнення studying_plan table
cursor.execute("SELECT * FROM studying_plan")
print(cursor.fetchall())

#Обираємо та друкуємо наповнення test_center table
cursor.execute("SELECT * FROM test_center")
print(cursor.fetchall())

cursor.execute("UPDATE medical_record SET issue_date = '2023-11-25' WHERE id_record = 1")

#Оновлюємо наповнення future_driver table
cursor.execute("UPDATE future_driver SET name = 'Семен Гайдаш' WHERE id_future_driver = 1")

#Обираємо та друкуємо все з medical_record table
cursor.execute("SELECT * FROM medical_record")
print(cursor.fetchall())

#Обираємо та друкуємо все з future_driver table після оновлення
cursor.execute("SELECT * FROM future_driver")
print(cursor.fetchall())

#Зберігаємо зміни в БД та закриваємо з'єднання з нею
conn.commit()
conn.close()