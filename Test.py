import os
import pandas as pd
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#COMANDO CLEARCONSOLE():

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#VARIABLES:

dinero = [1500]
ticket = [0]
carrito = {'PRODUCTO':' \tPRECIO\n'}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:	
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MENU PRINCIPAL:

	def menu_principal():
		clearConsole()
		print(f"\n--- Bienvenido a CaliMax ---\n")
		print(f"1.-Frutas y Verduras\n2.-Higiene\n3.-Lacteos\n4.-Panaderia\n5.-Mascotas\n6.-Galletas\n7.-Botanas\n8.-Legumbres\n9.-Carniceria\nPresione cualquier otra tecla para salir...")
	menu_principal()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TRY:
	
	try:
		op_menu_principal = int(input("\nQue seccion quieres visitar? -> "))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	#FUNCIONES:

		def Frutas_Verduras():
			clearConsole()

			print('\n===FRUTAS Y VERDURAS===\n\n1.-Tomates\n2.-Cebollas\n3.-Aguacates\n4.-Papas\n5.-Manzanas\n6.-Naranjas\n7.-Peras\n8.-Jicama\n9.-Duraznos')	

			seccion_frutas_verduras = {'1':12,'2':11,'3':20,'4':15,'5':12,'6':13,'7':14,'8':22,'9':18}
				
			op_frutas_verduras = int(input("\nElige una opcion -> "))

			productos = {1:'Tomates',2:'Cebollas',3:'Aguacates',4:'Papas',5:'Manzanas',6:'Naranjas',7:'Peras',8:'Jicama',9:'Duraznos'}
			print(f"\nProducto: {productos[op_frutas_verduras]}\nPrecio: {seccion_frutas_verduras[str(op_frutas_verduras)]}")

			res = int(ticket[-1]) + seccion_frutas_verduras[str(op_frutas_verduras)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_frutas_verduras])] = str(seccion_frutas_verduras[str(op_frutas_verduras)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Higiene():
			clearConsole()

			print('\n===HIGIENE===\n\n1.-Shampoo\n2.-Talco\n3.-Desodorante\n4.-Jabon para manos\n5.-Gel\n6.-Perfume\n7.-Crema corporal\n8.-Papel Higienico\n9.-Pasta Dental')
				
			seccion_higiene = {'1':23,'2':12,'3':24,'4':10,'5':25,'6':33,'7':42,'8':12,'9':16}

			op_higiene = int(input("\nElige una opcion -> "))

			productos = {1:'Shampoo',2:'Talco',3:'Desodorante',4:'Jabon para manos',5:'Gel',6:'Perfume',7:'Crema corporal',8:'Papel Higienico',9:'Pasta Dental'}
			print(f"\nProducto: {productos[op_higiene]}\nPrecio: {seccion_higiene[str(op_higiene)]}")

			res = int(ticket[-1]) + seccion_higiene[str(op_higiene)]
			ticket.clear()
			ticket.append(res)
			carrito[str(productos[op_higiene])] = str(seccion_higiene[str(op_higiene)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Lacteos():
			clearConsole()

			print('\n==LACTEOS===\n\n1.-Leche Deslactosada\n2.-Yogurt\n3.-Helado\n4.-Queso\n5.-Carnation\n6.-Huevos\n7.-Leche Entera\n8.-Media Crema')

			seccion_lacteos = {'1':17,'2':14,'3':54,'4':32,'5':16,'6':80,'7':19,'8':14}

			op_lacteos = int(input("\nElige una opcion -> "))

			productos = {1:'Leche Deslactosada',2:'Yogurt',3:'Helado',4:'Queso',5:'Carnation',6:'Huevos',7:'Leche Entera',8:'Media Crema'}
			print(f"\nProducto: {productos[op_lacteos]}\nPrecio: {seccion_lacteos[str(op_lacteos)]}")

			res = int(ticket[-1]) + seccion_lacteos[str(op_lacteos)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_lacteos])] = str(seccion_lacteos[str(op_lacteos)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Panaderia():
			clearConsole()

			print('\n===PANADERIA===\n\n1.-Concha\n2.-Orejas\n3.-Besos\n4.-Cocol\n5.-Campechanas\n6.-Garibaldis\n7.-Polvoron\n8.-Ojo de buey\n9.-Cuernitos')

			seccion_panaderia = {'1':12,'2':11,'3':10,'4':13,'5':15,'6':13,'7':15,'8':17,'9':12}

			op_panaderia = int(input("\nElige una opcion -> "))

			productos = {1:'Concha',2:'Orejas',3:'Besos',4:'Cocol',5:'Campechanas',6:'Garibaldis',7:'Polvoron',8:'Ojo de buey',9:'Cuernitos'}
			print(f"\nProducto: {productos[op_panaderia]}\nPrecio: {seccion_panaderia[str(op_panaderia)]}")

			res = int(ticket[-1]) + seccion_panaderia[str(op_panaderia)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_panaderia])] = str(seccion_panaderia[str(op_panaderia)])	
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Mascotas():
			clearConsole()

			print('\n===MASCOTAS===\n\n1.-Comida\n2.-Correa\n3.-Ropa\n4.-Shampoo para perros\n5.-Hueso de juguete')

			seccion_mascotas = {'1':34,'2':63,'3':126,'4':45,'5':32}

			op_mascotas = int(input("\nElige una opcion -> "))

			productos = {1:'Comida',2:'Correa',3:'Ropa',4:'Shampoo para perros',5:'Hueso de juguete'}
			print(f"\nProducto: {productos[op_mascotas]}\nPrecio: {seccion_mascotas[str(op_mascotas)]}")

			res = int(ticket[-1]) + seccion_mascotas[str(op_mascotas)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_mascotas])] = str(seccion_mascotas[str(op_mascotas)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Galletas():
			clearConsole()

			print('\n===GALLETAS===\n\n1.-Emperador\n2.-Marias\n3.-Principe\n4.-Arcoiris\n5.-Chokis\n6.-Giro\n7.-Canelitas\n8.-Polvorones\n9.-Trikitrakes')

			seccion_galletas = {'1':17,'2':16,'3':18,'4':15,'5':16,'6':14,'7':16,'8':19,'9':25}

			op_galletas = int(input("\nElige una opcion -> "))

			productos = {1:'Emperador',2:'Marias',3:'Principe',4:'Arcoiris',5:'Chokis',6:'Giro',7:'Canelitas',8:'Polvorones',9:'Trikitrakes'}
			print(f"\nProducto: {productos[op_galletas]}\nPrecio: {seccion_galletas[str(op_galletas)]}")
			
			res = int(ticket[-1]) + seccion_galletas[str(op_galletas)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_galletas])] = str(seccion_galletas[str(op_galletas)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Botanas():
			clearConsole()

			print('\n===SABRITAS===\n\n.1-Doritos\n2.-Ruffles\n3.-Paketaxo\n4.-Rancheritos\n5.-Tostitos\n6.-Crujitos\n7.-Chips\n8.-Cheetos\n9.-Sabritas')

			seccion_botanas = {'1':14,'2':13,'3':18,'4':16,'5':17,'6':13,'7':17,'8':15,'9':12}

			op_botanas = int(input("\nElige una opcion -> "))

			productos = {1:'Doritos',2:'Ruffles',3:'Paketaxo',4:'Rancheritos',5:'Tostitos',6:'Crujitos',7:'Chips',8:'CHeetos',9:'Sabritas'}
			print(f"\nProducto: {productos[op_botanas]}\nPrecio: {seccion_botanas[str(op_botanas)]}")

			res = int(ticket[-1]) + seccion_botanas[str(op_botanas)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_botanas])] = str(seccion_botanas[str(op_botanas)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		def Legumbres():
			clearConsole()

			print('\n===LEGUMBRES===\n\n1.-Frijol\n2.-Arroz\n3.-Lentejas\n4.-Garbanzo\n5.-Maiz Palomero\n6.-Almendras\n7.-Nuez\n8.-Frutas del paraiso')

			seccion_legumbres = {'1':16,'2':16,'3':17,'4':18,'5':17,'6':15,'7':14,'8':15}

			op_legumbres = int(input("\nElige una opcion -> "))

			productos = {1:'Frijol',2:'Arroz',3:'Lentejas',4:'Garbanzo',5:'Maiz Palomero',6:'Almendras',7:'Nuez',8:'Frutas de paraiso'}
			print(f"\nProducto: {productos[op_legumbres]}\nPrecio: {seccion_legumbres[str(op_legumbres)]}")
			
			res = int(ticket[-1]) + seccion_legumbres[str(op_legumbres)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_legumbres])] = str(seccion_legumbres[str(op_legumbres)])
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------				
		def Carniceria():
			clearConsole()

			print('\n===CARNICERIA===\n\n1.-Chorizo\n2.-Jamon\n3.-Salchicha\n4.-Tocino\n5.-Chicharron\n6.-Carne Deshebrada\n7.-Pollo\n8.-Puerco\n9.-Res')

			seccion_carniceria = {'1':15,'2':35,'3':23,'4':26,'5':25,'6':103,'7':130,'8':123,'9':152}

			op_carniceria = int(input("\nElige una opcion -> "))

			productos = {1:'Chorizo',2:'Jamon',3:'Salchicha',4:'Tocino',5:'Chicharron',6:'Carne Deshebrada',7:'Pollo',8:'Puerco',9:'Res'}
			print(f"\nProducto: {productos[op_carniceria]}\nPrecio: {seccion_carniceria[str(op_carniceria)]}")
			
			res = int(ticket[-1]) + seccion_carniceria[str(op_carniceria)]
			ticket.clear()
			ticket.append(res)

			carrito[str(productos[op_carniceria])] = str(seccion_carniceria[str(op_carniceria)])

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
	if str(input("\nDeseas salir? ('S' para salir, cualquier otra tecla para continuar) -> ").upper()) == 'S':
		if ticket[0] == 0:
			break
		else:
			s = pd.Series(carrito,dtype= "string")
			print(f"\n---TICKET---\n\n{s}")
			break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(f"\nTotal: {ticket[0]}\n\nDinero actual: {int(dinero[-1]) - int(ticket[0])}\nQue tenga un excelente dia!")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------