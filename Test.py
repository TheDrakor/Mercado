import os
import pandas as pd
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COMANDO CLEARCONSOLE():

def clearConsole():
	os.system('clear')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VARIABLES:

dinero = [1500]
ticket = [0]
ticket_actual = [0]
carrito = {'PRODUCTO':'\tPRECIO''\t\tPIEZAS\n'}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LISTAS:

frutas_verduras_list = []
higiene_list = []
lacteos_list = []
panaderia_list = []
mascotas_list = []
galletas_list = []
botanas_list = []
legumbres_list = []
carniceria_list = []
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:	
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MENU PRINCIPAL:

	def menu_principal():
		clearConsole()
		print(f"--- Bienvenido a CaliMax ---\n")
		print(f"1.-Frutas y Verduras\n2.-Higiene\n3.-Lacteos\n4.-Panaderia\n5.-Mascotas\n6.-Galletas\n7.-Botanas\n8.-Legumbres\n9.-Carniceria\nPresione cualquier otra tecla para salir...")
	menu_principal()
	print(f"\nDinero actual: $ {dinero[-1]}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TRY:
	
	try:
		op_menu_principal = int(input("\nQue seccion quieres visitar? -> "))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	#FUNCIONES:

		def compra_del_producto(seccion,op,productos):

			res = int(ticket[-1]) + seccion[str(op)]
			ticket_actual.clear()
			ticket_actual.append(res)

			if res < int(dinero[-1]):
				ticket.clear()
				ticket.append(res)
				dinero[0] = int(dinero[0]) - int(seccion[str(op)])
				print("Se ha agregado al carrito! ")
				return seccion,op,productos,res
			else:
				print(f"\nNo tienes suficiente dinero...")
				return seccion,op,productos,res

		def Frutas_Verduras():
			clearConsole()

			print('===FRUTAS Y VERDURAS===\n\n1.-Tomates\n2.-Cebollas\n3.-Aguacates\n4.-Papas\n5.-Manzanas\n6.-Naranjas\n7.-Peras\n8.-Jicama\n9.-Duraznos')	

			seccion = {'1':12,'2':11,'3':20,'4':15,'5':12,'6':13,'7':14,'8':22,'9':18}
				
			op = int(input("\nElige una opcion -> "))

			clearConsole()

			productos = {1:'Tomates',2:'Cebollas',3:'Aguacates',4:'Papas',5:'Manzanas',6:'Naranjas',7:'Peras',8:'Jicama',9:'Duraznos'}
			print(f"===COMPRA DEL PRODUCTO===\n\nProducto: {productos[op]}\nPrecio: $ {seccion[str(op)]}")

			frutas_verduras_list.append(productos[op])

			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[-1]) < int(dinero[-1]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{frutas_verduras_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Higiene():
			clearConsole()

			print('\n===HIGIENE===\n\n1.-Shampoo\n2.-Talco\n3.-Desodorante\n4.-Jabon para manos\n5.-Gel\n6.-Perfume\n7.-Crema corporal\n8.-Papel Higienico\n9.-Pasta Dental')
				
			seccion = {'1':23,'2':12,'3':24,'4':10,'5':25,'6':33,'7':42,'8':12,'9':16}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Shampoo',2:'Talco',3:'Desodorante',4:'Jabon para manos',5:'Gel',6:'Perfume',7:'Crema corporal',8:'Papel Higienico',9:'Pasta Dental'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			higiene_list.append(productos[op])

			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{higiene_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Lacteos():
			clearConsole()

			print('\n==LACTEOS===\n\n1.-Leche Deslactosada\n2.-Yogurt\n3.-Helado\n4.-Queso\n5.-Carnation\n6.-Huevos\n7.-Leche Entera\n8.-Media Crema')

			seccion = {'1':17,'2':14,'3':54,'4':32,'5':16,'6':80,'7':19,'8':14}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Leche Deslactosada',2:'Yogurt',3:'Helado',4:'Queso',5:'Carnation',6:'Huevos',7:'Leche Entera',8:'Media Crema'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			lacteos_list.append(productos[op])

			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{lacteos_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Panaderia():
			clearConsole()

			print('\n===PANADERIA===\n\n1.-Concha\n2.-Orejas\n3.-Besos\n4.-Cocol\n5.-Campechanas\n6.-Garibaldis\n7.-Polvoron\n8.-Ojo de buey\n9.-Cuernitos')

			seccion = {'1':12,'2':11,'3':10,'4':13,'5':15,'6':13,'7':15,'8':17,'9':12}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Concha',2:'Orejas',3:'Besos',4:'Cocol',5:'Campechanas',6:'Garibaldis',7:'Polvoron',8:'Ojo de buey',9:'Cuernitos'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			panaderia_list.append(productos[op])

			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{panaderia_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Mascotas():
			clearConsole()

			print('\n===MASCOTAS===\n\n1.-Comida\n2.-Correa\n3.-Ropa\n4.-Shampoo para perros\n5.-Hueso de juguete')

			seccion = {'1':34,'2':63,'3':126,'4':45,'5':32}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Comida',2:'Correa',3:'Ropa',4:'Shampoo para perros',5:'Hueso de juguete'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			mascotas_list.append(productos[op])

			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{mascotas_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Galletas():
			clearConsole()

			print('\n===GALLETAS===\n\n1.-Emperador\n2.-Marias\n3.-Principe\n4.-Arcoiris\n5.-Chokis\n6.-Giro\n7.-Canelitas\n8.-Polvorones\n9.-Trikitrakes')

			seccion = {'1':17,'2':16,'3':18,'4':15,'5':16,'6':14,'7':16,'8':19,'9':25}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Emperador',2:'Marias',3:'Principe',4:'Arcoiris',5:'Chokis',6:'Giro',7:'Canelitas',8:'Polvorones',9:'Trikitrakes'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			galletas_list.append(productos[op])
			
			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{galletas_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Botanas():
			clearConsole()

			print('\n===SABRITAS===\n\n.1-Doritos\n2.-Ruffles\n3.-Paketaxo\n4.-Rancheritos\n5.-Tostitos\n6.-Crujitos\n7.-Chips\n8.-Cheetos\n9.-Sabritas')

			seccion = {'1':14,'2':13,'3':18,'4':16,'5':17,'6':13,'7':17,'8':15,'9':12}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Doritos',2:'Ruffles',3:'Paketaxo',4:'Rancheritos',5:'Tostitos',6:'Crujitos',7:'Chips',8:'CHeetos',9:'Sabritas'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			botanas_list.append(productos[op])

			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{botanas_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Legumbres():
			clearConsole()

			print('\n===LEGUMBRES===\n\n1.-Frijol\n2.-Arroz\n3.-Lentejas\n4.-Garbanzo\n5.-Maiz Palomero\n6.-Almendras\n7.-Nuez\n8.-Frutas del paraiso')

			seccion = {'1':16,'2':16,'3':17,'4':18,'5':17,'6':15,'7':14,'8':15}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Frijol',2:'Arroz',3:'Lentejas',4:'Garbanzo',5:'Maiz Palomero',6:'Almendras',7:'Nuez',8:'Frutas de paraiso'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			legumbres_list.append(productos[op])
			
			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{legumbres_list.count(productos[op])}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------				
		def Carniceria():
			clearConsole()

			print('\n===CARNICERIA===\n\n1.-Chorizo\n2.-Jamon\n3.-Salchicha\n4.-Tocino\n5.-Chicharron\n6.-Carne Deshebrada\n7.-Pollo\n8.-Puerco\n9.-Res')

			seccion = {'1':15,'2':35,'3':23,'4':26,'5':25,'6':103,'7':130,'8':123,'9':152}

			op = int(input("\nElige una opcion -> "))

			productos = {1:'Chorizo',2:'Jamon',3:'Salchicha',4:'Tocino',5:'Chicharron',6:'Carne Deshebrada',7:'Pollo',8:'Puerco',9:'Res'}
			print(f"\nProducto: {productos[op]}\nPrecio: {seccion[str(op)]}")

			carniceria_list.append(productos[op])
			
			if input('\nDesea agregarlo al carrito (Y/N)? ').upper() == 'Y':
				compra_del_producto(seccion,op,productos)
				if int(ticket_actual[0]) < int(dinero[0]):
					carrito[str(productos[op])] = (f"{seccion[str(op)]}\t\t{carniceria_list.count(productos[op])}")
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
		print("\n# ERROR #\n")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	if str(input("\nPresiona 'S' para salir, cualquier otra tecla para continuar -> ").upper()) == 'S':
		if ticket[-1] == 0:
			break
		else:
			s = pd.Series(carrito,dtype = 'string')
			print(f"\n---TICKET---\n{'-'*42}\n{s}\n{'-'*42}")
			break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(f"\nTotal: ${ticket[-1]}\n\nDinero actual: {dinero[-1]}\nQue tenga un excelente dia!")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------