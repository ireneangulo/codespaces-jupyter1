#El comandante de la estrella de la muerte el gran Moff Tarkin debe administrar las asigna- ciones de vehículos y Stromtroopers a las distintas misiones que parten desde la estrella de la muerte, para facilitar esta tarea nos encomienda desarrollar las funciones necesarias para gestionar esto mediante prioridades de la siguiente manera:
#de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;
#si la misión fue pedida por Palpatine o Darth Vader estas tendrán alta prioridad, sino su prioridad será baja;
#si la misión es de prioridad alta los recursos se asignarán manualmente independiente- mente de su tipo;
#si la misión es de baja prioridad se asignarán los recursos de la siguiente manera dependiendo de su tipo:
#exploración: 15 Scout Troopers y 2 speeder bike,
#contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
#ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT),
#realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, per- mitiendo agregar nuevos pedidos de misiones durante la atención;
#indicar la cantidad total de recursos asignados a las misiones.
import random
import time

class Misión:
    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general
        if self.general == 'Palpatine' or self.general == 'Darth Vader':
            self.prioridad = 'alta'
        else:
            self.prioridad = 'baja'
        self.scout_troopers = 0
        self.speeder_bike = 0
        self.stormtroopers = 0
        self.vehículos = []
        self.recursos = 0

    def __str__(self):
        return f'{self.planeta} - {self.tipo} - {self.general} - {self.prioridad} - {self.recursos}'

    def asignar(self):
        if self.prioridad == 'alta':
            self.scout_troopers = int(input('Cuantos Scout Troopers? '))
            self.speeder_bike = int(input('Cuantos speeder bike? '))
            self.stormtroopers = int(input('Cuantos Stormtroopers? '))
            vehículos = int(input('Cuantos vehículos? '))
            for i in range(vehículos):
                self.vehículos.append(input('Qué vehículo? '))
        else:
            if self.tipo == 'exploración':
                self.scout_troopers = 15
                self.speeder_bike = 2
            elif self.tipo == 'contención':
                self.stormtroopers = 30
                vehículos = random.randint(1, 3)
                for i in range(vehículos):
                    self.vehículos.append(random.choice(['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST']))
            elif self.tipo == 'ataque':
                self.stormtroopers = 50
                vehículos = random.randint(4, 7)
                for i in range(vehículos):
                    self.vehículos.append(random.choice(['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST', 'AT-M6', 'AT-MP', 'AT-DT']))
        self.recursos = self.scout_troopers + self.speeder_bike + self.stormtroopers + len(self.vehículos)

    def asignar_recursos(self):
        print(f'{self.planeta} - {self.tipo} - {self.general} - {self.prioridad} - {self.recursos}')
        print(f'Scout Troopers: {self.scout_troopers}')
        print(f'Speeder Bike: {self.speeder_bike}')
        print(f'Stormtroopers: {self.stormtroopers}')
        print(f'Vehículos: {self.vehículos}')

def main():

    misiones = []
    while True:
        print('1 - Agregar misión')
        print('2 - Asignar recursos')
        print('3 - Salir')
        opcion = input('Opción: ')
        if opcion == '1':
            tipo = input('Tipo de misión: ')
            planeta = input('Planeta destino: ')
            general = input('General: ')
            misiones.append(Misión(tipo, planeta, general))
        elif opcion == '2':
            for mision in misiones:
                mision.asignar()
            for mision in misiones:
                mision.asignar_recursos()
                time.sleep(1)
            print(f'Total de recursos: {sum([mision.recursos for mision in misiones])}')
        elif opcion == '3':
            break

if __name__ == '__main__':
    main()










