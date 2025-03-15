# Library Management System

This project is a basic implementation of a library management system in Python. It allows users to add books, borrow them, return them, and check the inventory of available books.

## Features

- Register new books with title, author, and ISBN.
- Borrow books, changing their status from "available" to "unavailable".
- Return books, changing their status back to "available".
- View the full inventory of library books and their status.
- Search for books by ISBN.

## Technologies Used

- Python 3.x
- Lists to store the books
- No external dependencies required

## Requirements

- Python 3.x installed on your machine.

## How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your_username/your_repository.git
```

2. Navigate to the repository folder:
 ```bash
example:
cd your_repository
 ```

3. Run the script:
 ```bash
python sistema_de_gestion_de_biblioteca.py
```

4. The program will display a menu with the following options:

1. Add book: Add a new book to the library.
2. Borrow book: Borrow a book by searching for its ISBN.
3. Return book: Return a book by searching for its ISBN.
4. Show books: Show all books and their status.
5. Search book: Search for a book by its ISBN and display its status.
6. Exit: Exit the program.

## Example Usage
Upon running the program:
Welcome to the Library Management System

1. Add book
2. Borrow book
3. Return book
4. Show books
5. Search book
6. Exit

Choose an option: 1
Title: Don Quixote
Author: Cervantes
ISBN: 12345
Book added successfully.

Choose an option: 4
- Don Quixote (Cervantes) - ISBN: 12345 - Available: Yes

Choose an option: 2
Enter the ISBN: 12345
Book borrowed successfully.

Choose an option: 4
- Don Quixote (Cervantes) - ISBN: 12345 - Available: No





# Sistema de Gestión de Biblioteca

Este proyecto es una implementación básica de un sistema de gestión para una biblioteca en Python. Permite a los usuarios agregar libros, prestarlos, devolverlos y consultar el inventario de libros disponibles.

## Características

- Registrar nuevos libros con título, autor e ISBN.
- Prestar libros a los usuarios, cambiando su estado de "disponible" a "no disponible".
- Devolver libros, cambiando su estado de vuelta a "disponible".
- Consultar el inventario completo de libros de la biblioteca, mostrando su estado.
- Buscar libros por ISBN.

## Tecnologías utilizadas

- Python 3.x
- Listas para almacenar los libros
- No requiere dependencias externas

## Requisitos

- Python 3.x instalado en tu máquina.

## Cómo usarlo

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
      ```
2. Ve a la carpeta del repositorio:
   ```bash
cd tu_repositorio
   ```
3. Ejecuta el script:
   ```bash
python biblioteca.py
   ```
4. El programa te mostrará un menú con las siguientes opciones:

1. Agregar libro: Añade un nuevo libro a la biblioteca.
2. Prestar libro: Presta un libro buscando por ISBN.
3. Devolver libro: Devuelve un libro buscando por ISBN.
4. Mostrar libros: Muestra todos los libros y su estado.
5. Buscar libro: Busca un libro por su ISBN y muestra su estado.
6. Salir: Sale del programa.

## Ejemplo de uso
Al ejecutar el programa:

   ```bash
Bienvenido al Sistema de Gestión de Biblioteca

1. Agregar libro
2. Prestar libro
3. Devolver libro
4. Mostrar libros
5. Buscar libro
6. Salir

Elige una opción: 1
Título: El Quijote
Autor: Cervantes
ISBN: 12345
Libro agregado con éxito.

Elige una opción: 4
- El Quijote (Cervantes) - ISBN: 12345 - Disponible: Sí

Elige una opción: 2
Ingresa el ISBN: 12345
Libro prestado con éxito.

Elige una opción: 4
- El Quijote (Cervantes) - ISBN: 12345 - Disponible: No
   ```
## Contribuciones
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork de este repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza los cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Empuja los cambios a tu repositorio remoto (git push origin feature/nueva-funcionalidad).
Crea un pull request.


