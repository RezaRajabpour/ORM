import sqlite3

conn = sqlite3.connect("books1.db")
cur = conn.cursor()

class Author:
    def __init__(self, id=0, national_code="", name="", last_name="", birthday="", grade=""):
        self.id, self.national_code, self.name, self.last_name, self.birthday, self.grade = id, national_code, name, last_name, birthday, grade
    def __str__(self):
        return f"{self.name} {self.last_name}"

class Translator:
    def __init__(self, id=0, national_code="", name="", last_name="", grade=""):
        self.id, self.national_code, self.name, self.last_name, self.grade = id, national_code, name, last_name, grade
    def __str__(self):
        return f"{self.name} {self.last_name}"

class Publisher:
    def __init__(self, id=0, name="", address="", phone_number="", fax_number="", email="", establish_date=""):
        self.id, self.name, self.address, self.phone_number, self.fax_number, self.email, self.establish_date = id, name, address, phone_number, fax_number, email, establish_date
    def __str__(self):
        return f"{self.name}"

class Resource:
    def __init__(self, id=0, title="", type="", establish_date=""):
        self.id, self.title, self.type, self.establish_date = id, title, type, establish_date
    def __str__(self):
        return f"{self.title}"

class EsrbRating:
    def __init__(self, id=0, esrb_name=""): 
        self.id, self.esrb_name = id, esrb_name
    def __str__(self): 
        return self.esrb_name

class Genre:
    def __init__(self, id=0, name=""): 
        self.id, self.name = id, name
    def __str__(self): 
        return self.name

class Language:
    def __init__(self, id=0, name=""): 
        self.id, self.name = id, name
    def __str__(self): 
        return self.name

class Book:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.title = ""
        self.description = ""
        self.esrb_rating_id = None
        self.publisher_id = None
        self.resources = []
        self.authors = []
        self.translators = []
        self.genres = []
        self.languages = []

    def __str__(self):
        fmt = lambda items: ', '.join(str(i) for i in items)
        return f"{self.title}"

class DataAdapter:
    def __init__(self, table, model):
        self.table = table
        self.model = model

    def get_all(self):
        return list(map(lambda row: self.model(*row), cur.execute(f"SELECT * FROM {self.table}")))

AuthorsAdapter = DataAdapter("authors", Author)
TranslatorsAdapter = DataAdapter("translators", Translator)
PublishersAdapter = DataAdapter("publishers", Publisher)
ResourcesAdapter = DataAdapter("resources", Resource)
EsrbRatingsAdapter = DataAdapter("esrb_ratings", EsrbRating)
GenresAdapter = DataAdapter("genres", Genre)
LanguagesAdapter = DataAdapter("languages", Language)
