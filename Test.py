import os
import pandas as pd
import random as rm
from datetime import date, time, datetime
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COMANDO CLEARCONSOLE():

def clearConsole():
	os.system('clear')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VARIABLES:
ticket = [0]
ticket_actual = [0]
carrito = {}
carrito['Articulo'] = (f"\t   Cant.\t\tTotal")
cuenta = {}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LISTA:
lista = []
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EMPLEADOS:

empleados = ['MARIA','PEPE','JOSE','JAIME','XIMENA','ESTEPHANY','KARLA','GUILLERMO','HECTOR','JAZMIN']
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CICLO WHILE:

while True:
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MENU PRINCIPAL:

	def menu_principal():
		clearConsole()
		print(f"--- Bienvenido a CaliMax ---\n")
		print(f"1.-Frutas y Verduras\n\n2.-Higiene\n\n3.-Lacteos\n\n4.-Panaderia\n\n5.-Mascotas\n\n6.-Galletas\n\n7.-Botanas\n\n8.-Legumbres\n\n9.-Carniceria")
	menu_principal()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TRY:
	
	try:
		op_menu_principal = int(input("\nQue seccion quieres visitar? -> "))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	#FUNCIONES:

		def compra_del_producto(seccion,op,productos):

			cantidad = int(input("Cuantos deseas agregar? "))
			f_bucle = 0
			while f_bucle<cantidad:
				lista.append(productos[op])
				f_bucle += 1

			res = int(ticket[-1]) + (int(seccion[str(op)]) * cantidad)
			ticket_actual.clear()
			ticket_actual.append(res)

			ticket.clear()
			ticket.append(res)
			print("\nSe ha agregado al carrito! ")

			return seccion,op,productos,res
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Frutas_Verduras():
			clearConsole()

			print('===FRUTAS Y VERDURAS===\n\n1.-Tomates\n\n2.-Cebollas\n\n3.-Aguacates\n\n4.-Papas\n\n5.-Manzanas\n\n6.-Naranjas\n\n7.-Peras\n\n8.-Jicama\n\n9.-Duraznos')	

			seccion = {'1':12,'2':11,'3':20,'4':15,'5':12,'6':13,'7':14,'8':22,'9':18}
				
			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Tomates',2:'Cebollas',3:'Aguacates',4:'Papas',5:'Manzanas',6:'Naranjas',7:'Peras',8:'Jicama',9:'Duraznos'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Higiene():
			clearConsole()

			print('\n===HIGIENE===\n\n1.-Shampoo\n\n2.-Talco\n\n3.-Desodorante\n\n4.-Jabon para manos\n\n5.-Gel\n\n6.-Perfume\n\n7.-Crema corporal\n\n8.-Papel Higienico\n\n9.-Pasta Dental')
				
			seccion = {'1':23,'2':12,'3':24,'4':10,'5':25,'6':33,'7':42,'8':12,'9':16}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Shampoo',2:'Talco',3:'Desodorante',4:'Jabon para manos',5:'Gel',6:'Perfume',7:'Crema corporal',8:'Papel Higienico',9:'Pasta Dental'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Lacteos():
			clearConsole()

			print('\n==LACTEOS===\n\n1.-Leche Deslactosada\n\n2.-Yogurt\n\n3.-Helado\n\n4.-Queso\n\n5.-Carnation\n\n6.-Huevos\n\n7.-Leche Entera\n\n8.-Media Crema')

			seccion = {'1':17,'2':14,'3':54,'4':32,'5':16,'6':80,'7':19,'8':14}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Leche Deslactosada',2:'Yogurt',3:'Helado',4:'Queso',5:'Carnation',6:'Huevos',7:'Leche Entera',8:'Media Crema'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------		
		def Panaderia():
			clearConsole()

			print('\n===PANADERIA===\n\n1.-Concha\n\n2.-Orejas\n\n3.-Besos\n\n4.-Cocol\n\n5.-Campechanas\n\n6.-Garibaldis\n\n7.-Polvoron\n\n8.-Ojo de buey\n\n9.-Cuernitos')

			seccion = {'1':12,'2':11,'3':10,'4':13,'5':15,'6':13,'7':15,'8':17,'9':12}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Concha',2:'Orejas',3:'Besos',4:'Cocol',5:'Campechanas',6:'Garibaldis',7:'Polvoron',8:'Ojo de buey',9:'Cuernitos'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Mascotas():
			clearConsole()

			print('\n===MASCOTAS===\n\n1.-Comida\n\n2.-Correa\n\n3.-Ropa\n\n4.-Shampoo para perros\n\n5.-Hueso de juguete')

			seccion = {'1':34,'2':63,'3':87,'4':45,'5':32}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Comida',2:'Correa',3:'Ropa',4:'Shampoo para perros',5:'Hueso de juguete'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Galletas():
			clearConsole()

			print('\n===GALLETAS===\n\n1.-Emperador\n\n2.-Marias\n\n3.-Principe\n\n4.-Arcoiris\n\n5.-Chokis\n\n6.-Giro\n\n7.-Canelitas\n\n8.-Polvorones\n\n9.-Trikitrakes')

			seccion = {'1':17,'2':16,'3':18,'4':15,'5':16,'6':14,'7':16,'8':19,'9':25}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Emperador',2:'Marias',3:'Principe',4:'Arcoiris',5:'Chokis',6:'Giro',7:'Canelitas',8:'Polvorones',9:'Trikitrakes'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Botanas():
			clearConsole()

			print('\n===SABRITAS===\n\n.1-Doritos\n\n2.-Ruffles\n\n3.-Paketaxo\n\n4.-Rancheritos\n\n5.-Tostitos\n\n6.-Crujitos\n\n7.-Chips\n\n8.-Cheetos\n\n9.-Sabritas')

			seccion = {'1':14,'2':13,'3':18,'4':16,'5':17,'6':13,'7':17,'8':15,'9':12}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Doritos',2:'Ruffles',3:'Paketaxo',4:'Rancheritos',5:'Tostitos',6:'Crujitos',7:'Chips',8:'CHeetos',9:'Sabritas'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Legumbres():
			clearConsole()

			print('\n===LEGUMBRES===\n\n1.-Frijol\n\n2.-Arroz\n\n3.-Lentejas\n\n4.-Garbanzo\n\n5.-Maiz Palomero\n\n6.-Almendras\n\n7.-Nuez\n\n8.-Frutas del paraiso')

			seccion = {'1':16,'2':16,'3':17,'4':18,'5':17,'6':15,'7':14,'8':15}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Frijol',2:'Arroz',3:'Lentejas',4:'Garbanzo',5:'Maiz Palomero',6:'Almendras',7:'Nuez',8:'Frutas de paraiso'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------				
		def Carniceria():
			clearConsole()

			print('\n===CARNICERIA===\n\n1.-Chorizo\n\n2.-Jamon\n\n3.-Salchicha\n\n4.-Tocino\n\n5.-Chicharron\n\n6.-Carne Deshebrada\n\n7.-Pollo\n\n8.-Puerco\n\n9.-Res')

			seccion = {'1':15,'2':35,'3':23,'4':26,'5':25,'6':56,'7':104,'8':121,'9':129}

			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Chorizo',2:'Jamon',3:'Salchicha',4:'Tocino',5:'Chicharron',6:'Carne Deshebrada',7:'Pollo',8:'Puerco',9:'Res'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\n\nPrecio: $ {seccion[str(op)]}")

			if input('\nAgregar al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]):
					carrito[(f"{productos[op]}")] = (f"{lista.count(productos[op])}\t\t{int(seccion[str(op)]) * lista.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def error():
			print("\n# Utiliza enteros en el rango especificado #\n")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		switch_seccion = {
			1: Frutas_Verduras,
			2: Higiene,
			3: Lacteos,
			4: Panaderia,
			5: Mascotas,
			6: Galletas,
			7: Botanas,
			8: Legumbres,
			9: Carniceria
		}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		try:
			switch_seccion.get(op_menu_principal,error)()
		except KeyError:
			print("\n# Porfavor utiliza numeros en el rango especificado #")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EXCEPT:
	except ValueError:
		print("\n# ERROR #")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNC. TICKET DE COMPRA:
	
	def ticket_de_compra():
		carrito[' '] = ' '
		s = pd.Series(carrito,dtype = 'string')
		dt = datetime.now()
		print(f"\n{'-'*58}\nCALIMAX - LOS ENCINOS\nPuerto Ballarta 505 - 5a Planta\n{rm.choice(range(10000,99999))} - Puerto Rico\nCIF: {rm.choice(range(12200000,99999999))}\n\nCaja N. : 22321\t\tFactura Simplificada: {rm.choice(range(222400000000,999999999999))}\n\nTe atiende: {rm.choice(empleados)}\t\tFecha: {date.today()} {dt.hour}:{dt.minute}\n\n{'-'*58}\n{s}\n{'-'*58}")

		total_iva = int(ticket[-1]) + (int(ticket[-1])*0.08)
		dinero_pagado = int(input("Dinero: "))

		if dinero_pagado<int(total_iva):
			print('Dinero insuficiente...')
			return
		elif dinero_pagado>int(total_iva):
			print("")
			cuenta['Subtotal:              '] = ticket[-1]
			cuenta['IVA %8:'] = int(ticket[-1])*0.08
			cuenta['Total:'] = total_iva
			cuenta['Usted pago:'] = (dinero_pagado)
			cuenta['Cambio:'] = (dinero_pagado - total_iva)
			cuenta[' '] = ' '
			c = pd.Series(cuenta)
			print(c)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#SALIDA:

	if str(input("\nPresiona 'X' para salir '0' para continuar -> ").upper()) == 'X':
		if ticket[-1] == 0:
			break
		else:
			clearConsole()
			ticket_de_compra()
			break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\nGracias por su compra!\n")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------