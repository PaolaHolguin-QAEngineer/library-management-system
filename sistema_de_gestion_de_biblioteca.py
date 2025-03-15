#Crea una clase Libro con los atributos titulo (str), autor (str), isbn (str) y disponible (bool, inicialmente True). 
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

#Incluye un método agregar() que permita introducir un nuevo libro con sus características. 
    def agregar(self):
        """Agrega un libro nuevo a la biblioteca."""
        return f"Libro '{self.titulo}' agregado con éxito."

#Incluye un método prestar() que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado. 
    def prestar(self, isbn):
        """Presta un libro si está disponible."""
        if self.isbn == isbn:
            if self.disponible:
                self.disponible = False
                return f"Libro '{self.titulo}' prestado con éxito."
            else:
                return f"El libro '{self.titulo}' ya está prestado."
        return "ISBN no encontrado."

#Incluye un método devolver() que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible. 
    def devolver(self, isbn):
        """Devuelve un libro si está prestado."""
        if self.isbn == isbn:
            if not self.disponible:
                self.disponible = True
                return f"Libro '{self.titulo}' devuelto con éxito."
            else:
                return f"El libro '{self.titulo}' ya estaba disponible."
        return "ISBN no encontrado."

#Incluye un método mostrar() que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos y diga si estás disponible o no. 
    def mostrar(self):
        """Muestra todos los libros y su disponibilidad."""
        estado = "Sí" if self.disponible else "No"
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"

#Incluye un método buscar() que busque un libro en concreto por su ISBM y lo muestre en pantalla con todos sus datos y diga si está disponible o no. 
    def buscar(self, isbn):
        """Busca un libro por su ISBN."""
        if self.isbn == isbn:
            return self.mostrar()
        return "ISBN no encontrado."


#Usa una lista para almacenar objetos de la clase Libro. 
biblioteca = []

# Función para mostrar el menú y las opciones
def menu():
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca de Pao Holguin")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar")
        print("6. Salir")
        opcion = input("Elige una opción por favor: ")

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.append(libro)
            print(libro.agregar())
        elif opcion == '2':
            isbn = input("Ingresa el ISBN por favor: ")
            for libro in biblioteca:
                print(libro.prestar(isbn))
        elif opcion == '3':
            isbn = input("Ingresa el ISBN por favor: ")
            for libro in biblioteca:
                print(libro.devolver(isbn))
        elif opcion == '4':
            print("\nLista de libros:")
            for libro in biblioteca:
                print(libro.mostrar())
        elif opcion == '5':
            isbn = input("Ingresa el ISBN por favor: ")
            for libro in biblioteca:
                print(libro.buscar(isbn))
        elif opcion == '6':
            print("¡Gracias por usar el Sistema de Gestión de Biblioteca de Pao Holguin!")
            break
        else:
            print("Opción no válida  cariño. Intenta nuevamente.")

# Ejecutar el menú
menu()