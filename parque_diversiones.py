from ClasesBase import *

class Visitante:
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre

    def __str__(self):
        return f"{self.tipo} - {self.nombre}"

class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = Stack()

    def agregar_visitante(self, visitante):
        self.visitantes.push(visitante)

    def procesar_turno(self):
        procesados = Stack()
        for _ in range(self.capacidad):
            if not self.visitantes.is_empty():
                procesados.push(self.visitantes.pop())
            else:
                break
        return procesados

    def __repr__(self):
        return f"{self.nombre} (capacidad {self.capacidad}) - En espera: {self.visitantes}"


class Parque:
    def __init__(self):
        self.atracciones = Queue()

    def agregar_atraccion(self, nombre, capacidad):
        nueva = Atraccion(nombre, capacidad)
        self.atracciones.enqueue(nueva)
        return f"Atracción {nombre} agregada con capacidad {capacidad}"

    def eliminar_atraccion(self, nombre):
        aux = Queue()
        eliminada = False
        while not self.atracciones.is_empty():
            atr = self.atracciones.dequeue()
            if atr.nombre != nombre:
                aux.enqueue(atr)
            else:
                eliminada = True
        self.atracciones = aux
        return f"Atracción {nombre} eliminada" if eliminada else f"Atracción {nombre} no encontrada"

    def agregar_visitante(self, tipo, nombre):
        if self.atracciones.is_empty():
            return "No hay atracciones en el parque."
        
        visitante = Visitante(tipo, nombre)
        primera = self.atracciones.dequeue()
        primera.agregar_visitante(visitante)
        self.atracciones.enqueue(primera)
        for _ in range(self.atracciones.len() - 1):
            self.atracciones.enqueue(self.atracciones.dequeue())
        return f"Visitante {nombre} agregado como {tipo} en {primera.nombre}"

    def ejecutar_turno(self):
      if self.atracciones.is_empty():
          return "No hay atracciones en el parque."

      atr = self.atracciones.dequeue()
      procesados = atr.procesar_turno()
      if not procesados.is_empty():
          if not self.atracciones.is_empty():
              siguiente = self.atracciones.first()
              while not procesados.is_empty():
                  siguiente.agregar_visitante(procesados.pop())
              reporte = f"{atr.nombre}: procesó visitantes → pasan a {siguiente.nombre}"
          else:
              reporte = f"{atr.nombre}: procesó visitantes → SALEN DEL PARQUE"
      else:
          reporte = f"{atr.nombre}: sin visitantes para procesar"

      self.atracciones.enqueue(atr)

      return reporte

    def estado(self):
        if self.atracciones.is_empty():
            return "No hay atracciones en el parque."
        estado_str = Queue()
        for _ in range(self.atracciones.len()):
            atr = self.atracciones.dequeue()
            estado_str.enqueue(f"{atr.nombre} (capacidad {atr.capacidad}) -> En espera: {(atr.visitantes.len())}")
            self.atracciones.enqueue(atr)
        salida = ""
        while not estado_str.is_empty():
            salida += estado_str.dequeue() + "\n"
        return salida.strip()

parque = Parque()
parque.agregar_atraccion("Montaña Rusa", 3)
parque.agregar_atraccion("Carros Chocones", 2)
parque.agregar_atraccion("Rueda de la Fortuna", 2)
parque.agregar_atraccion("Casa del terror", 2)

parque.agregar_visitante("Adulto", "Carlos")
parque.agregar_visitante("Niño", "Lucía")
parque.agregar_visitante("Adulto", "Mateo")
parque.agregar_visitante("Adulto", "Camila")
parque.agregar_visitante("Niño", "Jony")
parque.agregar_visitante("Adulto", "Daniel")
parque.agregar_visitante("Adulto", "Isabela")
parque.agregar_visitante("Niño", "Emily")

while True:
    print("\n===== PARQUE DE ATRACCIONES =====")
    print("1. Agregar visitante (adulto o niño)")
    print("2. Ejecutar turno")
    print("3. Eliminar una atracción")
    print("4. Agregar una nueva atracción")
    print("5. Consultar estado del sistema")
    print("6. Salir")
    op = input("Seleccione una opción: ")

    if op == "1":
        tipo = input("Tipo de visitante (Adulto/Niño): ")
        nombre = input("Nombre del visitante: ")
        print(parque.agregar_visitante(tipo, nombre))

    elif op == "2":
        print("\n--- EJECUTANDO TURNO ---")
        print(parque.ejecutar_turno())

    elif op == "3":
        nombre = input("Nombre de la atracción a eliminar: ")
        print(parque.eliminar_atraccion(nombre))

    elif op == "4":
        nombre = input("Nombre de la nueva atracción: ")
        capacidad = int(input("Capacidad de la atracción: "))
        print(parque.agregar_atraccion(nombre, capacidad))

    elif op == "5":
        print("\n--- ESTADO DEL SISTEMA ---")
        print(parque.estado())

    elif op == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")