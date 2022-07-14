import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

dinero = [1500]

while True:

	clearConsole()

	def menu_principal():
		print(f"\nBienvenido a Abarrotes Maury !\n")
		print(f"1.-Frutas y Verduras\n2.-Higiene\n3.-Lacteos\n4.-Panaderia\n5.-Mascotas\n6.-Galletas\n7.-Botanas\n8.-Legumbres\n9.-Carniceria\nPresione cualquier otra tecla para salir...")
	menu_principal()

	op_menu_principal = int(input("\nQue seccion quieres visitar? ->"))
	clearConsole()

	def Frutas_Verduras():
		print('\n===FRUTAS Y VERDURAS===\n\n1.-Tomates\n2.-Cebollas\n3.-Aguacates\n4.-Papas\n5.-Manzanas\n6.-Naranjas\n7.-Peras\n8.-Jicama\n9.-Duraznos')
		
		seccion_frutas_verduras = {'1':12,'2':11,'3':20,'4':15,'5':12,'6':13,'7':14,'8':22,'9':18}
		
		op_frutas_verduras = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_frutas_verduras[str(op_frutas_verduras)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Higiene():
		print('\n===HIGIENE===\n\n1.-Shampoo\n2.-Talco\n3.-Desodorante\n4.-Jabon para manos\n5.-Gel\n6.-Perfume\n7.-Crema corporal\n8.-Papel Higienico\n9.-Pasta Dental')
		
		seccion_higiene = {'1':23,'2':12,'3':24,'4':10,'5':25,'6':33,'7':42,'8':12,'9':16}

		op_higiene = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_higiene[str(op_higiene)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Lacteos():
		print('\n==LACTEOS===\n\n1.-Leche Deslactosada\n2.-Yogurt\n3.-Helado\n4.-Queso\n5.-Carnation\n6.-Huevos\n7.-Leche Entera\n8.-Media Crema')

		seccion_lacteos = {'1':17,'2':14,'3':54,'4':32,'5':16,'6':80,'7':19,'8':14}

		op_lacteos = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_lacteos[str(op_lacteos)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Panaderia():
		print('\n===PANADERIA===\n\n1.-Concha\n2.-Orejas\n3.-Besos\n4.-Cocol\n5.-Campechanas\n6.-Garibaldis\n7.-Polvoron\n8.-Ojo de buey\n9.-Cuernitos')

		seccion_panaderia = {'1':12,'2':11,'3':10,'4':13,'5':15,'6':13,'7':15,'8':17,'9':12}

		op_panaderia = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_panaderia[str(op_panaderia)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Mascotas():
		print('\n===MASCOTAS===\n\n1.-Comida\n2.-Collares/Correas\n3.-Ropa\n4.-Shampoo para perros\n5.-Hueso de juguete')

		seccion_mascotas = {'1':34,'2':63,'3':126,'4':45,'5':32}

		op_mascotas = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_mascotas[str(op_mascotas)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Galletas():
		print('\n===GALLETAS===\n\n1.-Emperador\n2.-Marias\n3.-Principe\n4.-Arcoiris\n5.-Chokis\n6.-Giro\n7.-Canelitas\n8.-Polvorones\n9.-Trikitrakes')

		seccion_galletas = {'1':17,'2':16,'3':18,'4':15,'5':16,'6':14,'7':16,'8':19,'9':25}

		op_galletas = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_galletas[str(op_galletas)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Botanas():
		print('\n===SABRITAS===\n\n.1-Doritos\n2.-Ruffles\n3.-Paketaxo\n4.-Rancheritos\n5.-Tostitos\n6.-Crujitos\n7.-Chips\n8.-Cheetos\n9.-Sabritas')

		seccion_botanas = {'1':14,'2':13,'3':18,'4':16,'5':17,'6':13,'7':17,'8':15,'9':12}

		op_botanas = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_botanas[str(op_botanas)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Legumbres():
		print('\n===LEGUMBRES===\n\n1.-Frijol\n2.-Arroz\n3.-Lentejas\n4.-Garbanzo\n5.-Maiz Palomero\n6.-Almendras\n7.-Nuez\n8.-Frutas del paraiso')

		seccion_legumbres = {'1':16,'2':16,'3':17,'4':18,'5':17,'6':15,'7':14,'8':15}

		op_legumbres = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_legumbres[str(op_legumbres)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Carniceria():
		print('\n===CARNICERIA===\n\n1.-Chorizo\n2.-Jamon\n3.-Salchicha\n4.-Tocino\n5.-Chicharron\n6.-Carne Deshebrada\n7.-Pollo\n8.-Puerco\n9.-Res')

		seccion_carniceria = {'1':15,'2':35,'3':23,'4':26,'5':25,'6':103,'7':130,'8':123,'9':152}

		op_carniceria = int(input("\nElige una opcion ->"))

		res = int(dinero[-1]) - seccion_carniceria[str(op_carniceria)]
		dinero.append(res)
		print(dinero[-1])

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def error():
		print('error')

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

	switch_seccion.get(op_menu_principal, error)()
print("Gracias por su compra!\nDinero actual: " + dinero)