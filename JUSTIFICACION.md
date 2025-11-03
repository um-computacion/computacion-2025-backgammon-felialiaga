# Justificacion Backgammon Computacion 2025
## 1- Resumen del diseño
- El juego esta diseñado siguiendo los principios Solid y la programacion orientada a objetos
- El juego cuenta con 5 Clases para la logica del juego, un CLI para la ejecucion del mismo y una interfaz grafica con Pygame
## 2- Principios SOLID
- S - Single Responsability Principle
    Definicion: Una clase debe tener una sola responsabilidad
    Cumple este principio ya que cada clase se encarga de lo suyo, ejemplo: desde la clase Player no manejo los turnos ni tiro el dado, cada clase solo tiene sus responsabilidades
- O - Open/Closed Principle
    Definicion: Las clases deben estar abiertas para extensiones y cerradas para modificaciones
    Cumple este principio ya que yo puedo extender algun metodo sin necesidad de cambiar la clase. Ejemplo: puedo renderizar el tablero de otra forma sin tener que cambiar la clase base de Board
- L - Liskov Substitution Principle
    Definicion: Los objetos de una subclase deben poder reemplazar a los de la superclase sin alterar el comportamiento del programa, herencia
- I - Interface Segregation Principle
    Definicion: Ningun cliente deberia verse obligado a depender de metodos que no usa
    Cada clase debe contener los metodos que vaya a usar, y no metodos extras que obligen a la clase a usarlo. Se cumple ya que cada clase tiene lo justo para funcionar
- D - Dependency Inversion Principle
    Definicion: Los modulos de alto nivel no deben depender de modulos de mas bajo nivel
    Se cumple ya que el CLI solo se comunica con Game y no con las demas clases

## 3- Justificacion de Clases y responsabilidad de cada una
### Game
- La clase Game se encarga de manejar todo el juego, validando las reglas originales del juego.
- Esta clase es necesaria para poder llevar a cabo todas las validaciones del juego conectandose con las distintas clases
### Board
- Gestiona todo lo que tiene que ver con el tablero, los puntos, la barra y el home
- Esta clase requiere de un metodo que renderice el tablero, metodos para manipular la barra, el home y los distintos puntos
### Player
- Esta clase maneja el uso de jugadores, almacenando su numero y ficha
- Es necesaria para poder indentificar a cada usuario que esta jugando, y en un futuro poder agregarle cosas como: historial, nombre, puntaje, etc
### Checker
- Representa una ficha junto a sus estados y el jugador al que le pertenece
- Elegi hacerla con estados ya que esto facilita conocer la situacion de una ficha
### Dice
- Gestiona las tiradas de dados e implementa una logica para saber si son dobles 
- Cuenta con una lista donde voy a tener los dados(2 o 4 en caso de ser iguales) y una lista donde voy agregando los dados usados, y asi evitar usarlo mas de una vez
### CLI
- Gestiona la interaccion del usuario con el juego desde la consola
- Se separa de toda ka logica del juego para que sea mas facil de testear y de visualizar las cosas
## 4- Justificacion de atributos
### Game
- board: cuenta con un tablero que me permite poder acceder a todos los metodos para trabajar con este
- players: tiene una lista con los 2 jugadores que estan jugando la partida
- dice: gestiona todas las tiradas y los valores disponibles
- turno: gestiona el turno de los jugadores para poder ir cambiando de uno al otro
- dados_actuales: es una lista que va guardando los dados disponibles para la partida
- dados_usados: lista con los dados que ya fueron usados en el turno para evitar que se usen dos veces
### Board
- positions: guarda una lista con 24 posiciones validas, donde cada posicion es una lista de hasta 5 elementos
- bar: es un diccionario con la barra del jugador 1 y del jugador 2
- home: diccionario con el home de cada uno de los jugadores
### Player
- numero: guarda el numero del jugador, que puede ser 1 o 2
- ficha: guarda la ficha del jugador. Depende del numero del jugador
### Checker
- jugador: representa el numero del jugador 
- en_barra: estado de la ficha que puede ser False o True, dependiendo de la posicion, True si se encuentra en la barra y False si no
- en_meta: estado de la ficha que puede ser False o True, dependiendo de la posicion, True si se encuentra en la meta y False si no
### Dice
- valores: representa los valores actuales de los dados, siguiendo la regla de tirada doble
- usados: representa los dados que ya fueron usados
### CLI
- game: unicamente se conecta a la clase Game y permite crear una instancia del juego
## 5- Testing
- El programa cuenta con tests unitarios para validar el funcionamiento correcto de cada validacion o metodo
- Aparte para poder testear el CLI sin tener que ejecutar el juego, se usan mocks para simular algun estado del juego
- Testea cada input, print, metodo, validacion, repr, los comandos del cli, etc
## 6- Estrategias
- Se usa git-changelog para poder hacer un versionado de los cambios
- Se usa pylint para obtener una califiacion y poder hacer que el programa cumpla ciertos requisitos
- Se usa coverage para determinar el porcentaje de codigo que se encuentra cubierto por los tests unitarios