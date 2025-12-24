import sqlite3

conn = sqlite3.connect('books1.db')
cursor = conn.cursor()

class Authors:
    def __init__(self, id=0, national_code="", name="", last_name="", birthday="", grade=""):
        self.id = id
        self.national_code = national_code
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.grade = grade
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, last_name: {self.last_name}"

class Translators:
    def __init__(self, id=0, national_code="", name="", last_name="", grade=""):
        self.id = id
        self.national_code = national_code
        self.name = name
        self.last_name = last_name
        self.grade = grade
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, last_name: {self.last_name}"

class Publishers:
    def __init__(self, id=0, name="", address="", phone_number="", fax_number="", email="", establish_date=""):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.fax_number = fax_number
        self.email = email
        self.establish_date = establish_date
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

class Resources:
    def __init__(self, id=0, title="", type="", establish_date=""):
        self.id = id
        self.title = title
        self.type = type
        self.establish_date = establish_date
    
    def __str__(self):
        return f"id: {self.id}, title: {self.title}"

class Esrb_ratings:
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

class Genres:
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

class Languages:
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

class Books:
    def __init__(self, id=0, name="", title="", description="", esrb_rating_id=None, publisher_id=None):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.esrb_rating_id = esrb_rating_id
        self.publisher_id = publisher_id
        self.authors = []
        self.translators = []
        self.resources = []
        self.genres = []
        self.languages = []
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, title: {self.title}"

class AuthorsDataAdapter:
    @staticmethod
    def get_all():
        authors = []
        cursor.execute("SELECT * FROM authors")
        for row in cursor.fetchall():
            a = Authors(row[0], row[1], row[2], row[3], row[4], row[5])
            authors.append(a)
        return authors
    
    @staticmethod
    def insert(author):
        cursor.execute("INSERT INTO authors (national_code, name, last_name, birthday, grade) VALUES (?, ?, ?, ?, ?)",
                      (author.national_code, author.name, author.last_name, author.birthday, author.grade))
        conn.commit()
        author.id = cursor.lastrowid
        return author
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT id FROM books WHERE author_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM authors WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class TranslatorsDataAdapter:
    @staticmethod
    def get_all():
        translators = []
        cursor.execute("SELECT * FROM translators")
        for row in cursor.fetchall():
            t = Translators(row[0], row[1], row[2], row[3], row[4])
            translators.append(t)
        return translators
    
    @staticmethod
    def insert(translator):
        cursor.execute("INSERT INTO translators (national_code, name, last_name, grade) VALUES (?, ?, ?, ?)",
                      (translator.national_code, translator.name, translator.last_name, translator.grade))
        conn.commit()
        translator.id = cursor.lastrowid
        return translator
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT translator_id FROM book_translator WHERE translator_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM translators WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class PublishersDataAdapter:
    @staticmethod
    def get_all():
        publishers = []
        cursor.execute("SELECT * FROM publishers")
        for row in cursor.fetchall():
            p = Publishers(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            publishers.append(p)
        return publishers
    
    @staticmethod
    def insert(publisher):
        cursor.execute("INSERT INTO publishers (name, address, phone_number, fax_number, email, establish_date) VALUES (?, ?, ?, ?, ?, ?)",
                      (publisher.name, publisher.address, publisher.phone_number, publisher.fax_number, publisher.email, publisher.establish_date))
        conn.commit()
        publisher.id = cursor.lastrowid
        return publisher
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT publisher_id FROM books WHERE publisher_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM publishers WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class Esrb_ratingsDataAdapter:
    @staticmethod
    def get_all():
        esrbs = []
        cursor.execute("SELECT * FROM esrb_ratings")
        for row in cursor.fetchall():
            e = Esrb_ratings(row[0], row[1])
            esrbs.append(e)
        return esrbs
    
    @staticmethod
    def insert(esrb):
        cursor.execute("INSERT INTO esrb_ratings (name) VALUES (?)", (esrb.name,))
        conn.commit()
        esrb.id = cursor.lastrowid
        return esrb
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT esrb_rating_id FROM books WHERE esrb_rating_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM esrb_ratings WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class ResourcesDataAdapter:
    @staticmethod
    def get_all():
        resources = []
        cursor.execute("SELECT * FROM resources")
        for row in cursor.fetchall():
            r = Resources(row[0], row[1], row[2], row[3])
            resources.append(r)
        return resources
    
    @staticmethod
    def insert(resource):
        cursor.execute("INSERT INTO resources (title, type, establish_date) VALUES (?, ?, ?)",
                      (resource.title, resource.type, resource.establish_date))
        conn.commit()
        resource.id = cursor.lastrowid
        return resource
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT resource_id FROM book_resource WHERE resource_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM resources WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class GenresDataAdapter:
    @staticmethod
    def get_all():
        genres = []
        cursor.execute("SELECT * FROM genres")
        for row in cursor.fetchall():
            g = Genres(row[0], row[1])
            genres.append(g)
        return genres
    
    @staticmethod
    def insert(genre):
        cursor.execute("INSERT INTO genres (name) VALUES (?)", (genre.name,))
        conn.commit()
        genre.id = cursor.lastrowid
        return genre
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT genre_id FROM book_genre WHERE genre_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM genres WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class LanguagesDataAdapter:
    @staticmethod
    def get_all():
        languages = []
        cursor.execute("SELECT * FROM languages")
        for row in cursor.fetchall():
            l = Languages(row[0], row[1])
            languages.append(l)
        return languages
    
    @staticmethod
    def insert(language):
        cursor.execute("INSERT INTO languages (name) VALUES (?)", (language.name,))
        conn.commit()
        language.id = cursor.lastrowid
        return language
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT language_id FROM book_language WHERE language_id = ?", (id,))
        if cursor.fetchone() is None:
            cursor.execute("DELETE FROM languages WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

class BooksDataAdapter:
    @staticmethod
    def get_all():
        books = []
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            b = Books(row[0], row[1], row[2], row[3], row[4], row[5])
            
            cursor.execute("SELECT a.id, a.name, a.last_name FROM authors a JOIN book_author ba ON a.id = ba.author_id WHERE ba.book_id = ?", (b.id,))
            for auth_row in cursor.fetchall():
                b.authors.append(Authors(auth_row[0], "", auth_row[1], auth_row[2]))
            
            if b.publisher_id:
                cursor.execute("SELECT name FROM publishers WHERE id = ?", (b.publisher_id,))
                pub_row = cursor.fetchone()
                if pub_row:
                    b.publisher = Publishers(b.publisher_id, pub_row[0])
            
            books.append(b)
        return books
    
    @staticmethod
    def delete(id):
        cursor.execute("SELECT id FROM books WHERE id = ?", (id,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM book_author WHERE book_id = ?", (id,))
            cursor.execute("DELETE FROM book_translator WHERE book_id = ?", (id,))
            cursor.execute("DELETE FROM book_resource WHERE book_id = ?", (id,))
            cursor.execute("DELETE FROM book_language WHERE book_id = ?", (id,))
            cursor.execute("DELETE FROM book_genre WHERE book_id = ?", (id,))
            cursor.execute("DELETE FROM books WHERE id = ?", (id,))
            conn.commit()
            return True
        return False

books_list = BooksDataAdapter.get_all()
for b in books_list:
    print(b)
