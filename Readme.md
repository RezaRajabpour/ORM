# Books Database Management

A Python project for managing books and related resources using **SQLite** and an object-oriented structure. This project provides classes and adapters for easy interaction with database tables.

---

##  Getting Started

This project is compatible with **Python 3.x** and uses **SQLite** as the database.

### Prerequisites

- Python 3.x
- SQLite3 (comes with Python by default)

##  Project Structure

```
.
├── books1.db              # SQLite database
├── main.py                # Main project file
└── README.md              # Project documentation
```

---

##  Classes and Adapters

### Classes

- **Author**: Represents an author with attributes like id, name, last name, birthday, and grade.
- **Translator**: Represents a translator.
- **Publisher**: Represents a publisher.
- **Resource**: Represents a resource.
- **EsrbRating**: Represents an ESRB rating.
- **Genre**: Represents a book genre.
- **Language**: Represents a language.
- **Book**: Represents a book, containing lists of authors, translators, genres, languages, and resources.

### Data Adapters

- **DataAdapter**: Generic adapter to fetch data from any table.
- **AuthorsAdapter**, **TranslatorsAdapter**, **PublishersAdapter**, **ResourcesAdapter**, **EsrbRatingsAdapter**, **GenresAdapter**, **LanguagesAdapter**: Specific adapters for each table.

---

##  Usage

```python
from main import AuthorsAdapter, Book

# Get all authors
authors = AuthorsAdapter.get_all()
for author in authors:
    print(author)
```

You can use the adapters to fetch data from other tables similarly.

---

##  Notes

- The `Book` class can hold multiple related objects like authors, translators, genres, languages, and resources.
- The project is designed to be easily extendable to add more functionality, like inserting, updating, or deleting records.

