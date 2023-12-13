from bottle import Bottle, route, post, run, template, request, redirect
import sqlite3

app = Bottle()

# SQLite Database Initialization
conn = sqlite3.connect('animals.db')
cursor = conn.cursor()

# Create animals table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animals (
        animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_name TEXT NOT NULL,
        species TEXT NOT NULL
    )
''')

# Create habitats table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS habitats (
        habitat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        habitat_name TEXT NOT NULL
    )
''')

# Create relationship table to represent the many-to-many relationship between animals and habitats
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animal_habitat (
        relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id INTEGER,
        habitat_id INTEGER,
        FOREIGN KEY (animal_id) REFERENCES animals(animal_id),
        FOREIGN KEY (habitat_id) REFERENCES habitats(habitat_id)
    )
''')

conn.commit()

# Routes

@app.route('/')
def index():
    return template('index')

# Animals CRUD

@app.route('/animals')
def animals():
    search_term = request.query.get('search', '').strip()

    # Fetch animals based on search_term
    if search_term:
        cursor.execute("SELECT * FROM animals WHERE animal_name LIKE ? OR species LIKE ?", (f"%{search_term}%", f"%{search_term}%"))
    else:
        cursor.execute("SELECT * FROM animals")

    result = cursor.fetchall()

    return template('animals', rows=result, search_term=search_term)

@app.route('/animal_habitats/<animal_id:int>')
def animal_habitats(animal_id):
    # Fetch habitats associated with the animal
    cursor.execute("SELECT habitats.habitat_name FROM habitats JOIN animal_habitat ON habitats.habitat_id = animal_habitat.habitat_id WHERE animal_habitat.animal_id = ?", (animal_id,))
    result = cursor.fetchall()

    return template('animal_habitats', animal_id=animal_id, habitats=result)

@app.route('/animals/add', method='GET')
def add_animal_form():
    return template('add_animal')

@app.route('/animals/add', method='POST')
def add_animal():
    animal_name = request.forms.get('animal_name')
    species = request.forms.get('species')

    cursor.execute("INSERT INTO animals (animal_name, species) VALUES (?, ?)", (animal_name, species))
    conn.commit()

    redirect('/animals')

@app.route('/animals/edit/<animal_id:int>', method='GET')
def edit_animal_form(animal_id):
    cursor.execute("SELECT * FROM animals WHERE animal_id=?", (animal_id,))
    animal = cursor.fetchone()
    return template('edit_animal', animal=animal)

@app.route('/animals/edit/<animal_id:int>', method='POST')
def edit_animal(animal_id):
    animal_name = request.forms.get('animal_name')
    species = request.forms.get('species')

    cursor.execute("UPDATE animals SET animal_name=?, species=? WHERE animal_id=?", (animal_name, species, animal_id))
    conn.commit()

    redirect('/animals')

@app.route('/animals/delete/<animal_id:int>')
def delete_animal(animal_id):
    cursor.execute("DELETE FROM animals WHERE animal_id=?", (animal_id,))
    conn.commit()

    redirect('/animals')

# Habitats CRUD

@app.route('/habitats')
def habitats():
    cursor.execute("SELECT * FROM habitats")
    result = cursor.fetchall()
    return template('habitats', rows=result)

@app.route('/habitats/add', method='GET')
def add_habitat_form():
    return template('add_habitat')

@app.route('/habitats/add', method='POST')
def add_habitat():
    habitat_name = request.forms.get('habitat_name')

    cursor.execute("INSERT INTO habitats (habitat_name) VALUES (?)", (habitat_name,))
    conn.commit()

    redirect('/habitats')

@app.route('/habitats/edit/<habitat_id:int>', method='GET')
def edit_habitat_form(habitat_id):
    cursor.execute("SELECT * FROM habitats WHERE habitat_id=?", (habitat_id,))
    habitat = cursor.fetchone()
    return template('edit_habitat', habitat=habitat)

@app.route('/habitats/edit/<habitat_id:int>', method='POST')
def edit_habitat(habitat_id):
    habitat_name = request.forms.get('habitat_name')

    cursor.execute("UPDATE habitats SET habitat_name=? WHERE habitat_id=?", (habitat_name, habitat_id))
    conn.commit()

    redirect('/habitats')

@app.route('/habitats/delete/<habitat_id:int>')
def delete_habitat(habitat_id):
    cursor.execute("DELETE FROM habitats WHERE habitat_id=?", (habitat_id,))
    conn.commit()

    redirect('/habitats')

# Static Routes
@app.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root='./static')

# Run the application
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
