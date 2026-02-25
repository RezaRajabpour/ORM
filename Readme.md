---

# Books Database Management

A Python project for managing books and all related entities using **SQLite** and a clean **object-oriented architecture** combined with the **Data Adapter pattern**.  
The project focuses on correctness, extensibility, and real-world database querying.

---

## Overview

This project provides a structured way to interact with a relational books database while keeping business logic, database logic, and domain models clearly separated.

It is designed as a **backend-style foundation** that can later be extended with APIs, pagination, full-text search, or user interfaces.

---

## Key Features

- SQLite database with real relational data
- Object-oriented domain models
- Data Adapter pattern for database access
- Advanced multi-field book search
- Safe parameterized queries
- No duplicate results in search
- Easily extendable architecture

---

## Technology Stack

- Python 3.x
- SQLite3 (Python standard library)
- No external dependencies

---

## Project Structure

```
.
├── books1.db          SQLite database
├── CT.py              Main source file (models + adapters)
└── README.md          Project documentation
```

---

## Domain Models

Each database table is represented by a dedicated Python class:

- Author  
- Translator  
- Publisher  
- Resource  
- EsrbRating  
- Genre  
- Language  
- Book  

### Book Model

The `Book` entity acts as an aggregate root and is capable of holding multiple related objects, including:

- authors
- translators
- genres
- languages
- resources

This design allows full object representation when detailed data is required.

---

## Data Adapters

All database access is handled through adapter classes:

- DataAdapter (base class)
- BooksDataAdapter
- AuthorsDataAdapter
- TranslatorsDataAdapter
- PublishersDataAdapter
- ResourcesDataAdapter
- EsrbRatingsDataAdapter
- GenresDataAdapter
- LanguagesDataAdapter

Adapters are responsible for:
- executing SQL queries
- mapping rows to domain objects
- isolating SQL logic from the rest of the application

---

## Advanced Search Capability

The project includes a robust book search mechanism that supports filtering by:

- title
- author
- translator
- publisher
- genre
- any combination of the above (logical AND)

### Search Design Characteristics

- Uses SQL `EXISTS` subqueries instead of heavy JOIN chains
- Prevents duplicate records at the database level
- Fully parameterized and safe against SQL injection
- Tested on real data stored in the database

This makes the search method suitable for real-world usage and scalable extensions.

---

## Testing

The search functionality has been tested directly against the real SQLite database using multiple scenarios, including single-field and combined filters.  
All tests confirm correct filtering behavior and consistent results.

---

## Extensibility

The architecture is intentionally designed to support future enhancements, such as:

- Pagination and sorting
- Case-insensitive search
- SQLite Full-Text Search (FTS5)
- Create, update, and delete operations
- REST API layer (e.g., FastAPI or Flask)
- Integration with a frontend application

---

## Summary

This project demonstrates:

- clean separation of concerns
- practical database modeling
- real-world query design
- scalable backend-oriented architecture

It is suitable both as a learning project and as a solid foundation for further backend development.
---
