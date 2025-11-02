from core.Game import Game

class main:

    def __init__(self):
        self.__game__ = Game()

    def mostrar_estado(self):

        board = self.__game__.get_board()
        print("\n=== Estado del Tablero ===")
        board.display()
        print("==========================\n")

    def mostrar_ayuda(self):
        print("\n=== Guía rápida de comandos ===")
        print("Durante tu turno, deberás ingresar:")
        print(" - Origen: punto desde el que moverás tu ficha (1-24, o 0 si está en la barra).")
        print(" - Destino: punto al que querés moverla (1-24, o 25 si querés sacarla del tablero).")
        print(" - Dado: valor del dado que vas a usar para ese movimiento.")
        print("\nEjemplo: si tiraste [3, 5], podés mover desde el punto 12 al 9 (usando 3).")
        print("El sistema te avisará si un movimiento no es válido.")
        print("\nComandos disponibles durante la partida:")
        print(" - 'salir': finaliza la partida inmediatamente.")
        print(" - 'ayuda': muestra nuevamente esta guía.")
        print(" - 'tablero': muestra el estado actual del tablero.")
        print("===============================\n")

    def mostrar_resultado_final(self):
        ganador = self.__game__.get_ganador()
        print("\n=== Resultado Final ===")
        if ganador:
            print(f"El Jugador {ganador.get_numero()} ({ganador.get_ficha()}) ganó.")
        else:
            print("La partida terminó sin ganador.")
        print("========================\n")

    def mostrar_dados(self, valores):
        print(f"\nDados obtenidos: {valores}\n")

    def mostrar_menu_principal(self):
        print("=== Menú Principal ===")
        print("1: Jugar una nueva partida")
        print("2: Ver ayuda")
        print("3: Reiniciar partida")
        print("4: Salir")
        return input("\nSelecciona una opción (1-4): ").strip()

    def procesar_comando(self, comando):
        comando = comando.lower()

        if comando == "salir":
            print("\nJuego interrumpido por el usuario.")
            return False
        elif comando == "ayuda":
            self.mostrar_ayuda()
            return True
        elif comando == "tablero":
            self.mostrar_estado()
            return True

        return True

    def ejecutar_turno(self):
        jugador = self.__game__.get_jugador_actual()
        print("\n------------------------------------------")
        print(f"Turno del Jugador {jugador.get_numero()} ({jugador.get_ficha()})")
        print("------------------------------------------")

        # Tirar los dados
        valores = self.__game__.tirar_dados()
        self.mostrar_dados(valores)

        # Mientras haya dados disponibles, el jugador puede seguir moviendo fichas
        while self.__game__.get_dados_actuales():
            # Mostrar el estado actual del tablero antes de cada movimiento
            self.mostrar_estado()

            try:
                # --- Solicitar punto de origen ---
                origen_input = input("Origen (1-24, 0=barra, 'salir'=terminar): ").strip()
                if not self.procesar_comando(origen_input):
                    exit(0)
                if not origen_input.isdigit():
                    continue
                origen = int(origen_input)

                # --- Solicitar punto de destino ---
                destino_input = input("Destino (1-24, 25=meta, 'salir'=terminar): ").strip()
                if not self.procesar_comando(destino_input):
                    exit(0)
                if not destino_input.isdigit():
                    continue
                destino = int(destino_input)

                # --- Seleccionar el dado a usar ---
                dado_input = input(f"Selecciona dado {self.__game__.get_dados_actuales()}: ").strip()
                if not self.procesar_comando(dado_input):
                    exit(0)
                if not dado_input.isdigit():
                    continue
                dado = int(dado_input)

                # --- Intentar realizar el movimiento ---
                if self.__game__.mover_ficha(origen, destino, dado):
                    print("Movimiento realizado correctamente.")

                    # Verificar si con este movimiento se completó la partida
                    if self.__game__.juego_terminado():
                        self.mostrar_resultado_final()
                        return
                else:
                    print("Movimiento inválido. Intenta nuevamente.")

            except ValueError:
                print("Entrada inválida. Solo se permiten números enteros.")
            except Exception as e:
                print(f"Error: {str(e)}")

        # Cambiar turno
        print("\nFin del turno.")
        self.__game__.cambiar_turno()
        input("Presiona Enter para continuar con el siguiente jugador...")

    def reiniciar_partida(self):

        print("\nReiniciando partida...\n")
        self.__game__ = Game()
        print("Nueva partida lista.\n")
        self.mostrar_estado()

    def iniciar(self):
        print("=== Bienvenido al Backgammon ===")

        while True:
            opcion = self.mostrar_menu_principal()

            if opcion == "1":
                print("\nIniciando...\n")
                self.mostrar_estado()
                while not self.__game__.juego_terminado():
                    self.ejecutar_turno()
                self.mostrar_resultado_final()

            elif opcion == "2":
                self.mostrar_ayuda()

            elif opcion == "3":
                self.reiniciar_partida()

            elif opcion == "4":
                print("Gracias por jugar al Backgammon.")
                break

            else:
                print("Opción inválida. Elegí 1, 2, 3 o 4.\n")

if __name__ == "__main__":
    cli = main()
    cli.iniciar()