import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_animals_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animals (
                animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_name TEXT NOT NULL,
                species TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_habitats_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS habitats (
                habitat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                habitat_name TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_animal_habitat_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animal_habitat (
                relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_id INTEGER,
                habitat_id INTEGER,
                FOREIGN KEY (animal_id) REFERENCES animals(animal_id),
                FOREIGN KEY (habitat_id) REFERENCES habitats(habitat_id)
            )
        ''')
        self.conn.commit()

    def add_animal(self, animal_name, species):
        self.cursor.execute("INSERT INTO animals (animal_name, species) VALUES (?, ?)", (animal_name, species))
        self.conn.commit()

    def get_animals(self):
        self.cursor.execute("SELECT * FROM animals")
        return self.cursor.fetchall()

    def add_habitat(self, habitat_name):
        self.cursor.execute("INSERT INTO habitats (habitat_name) VALUES (?)", (habitat_name,))
        self.conn.commit()

    def get_habitats(self):
        self.cursor.execute("SELECT * FROM habitats")
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
