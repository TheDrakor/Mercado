import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

dinero = 1000
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
		frutas_verduras = {'1':13,'2':14,'3':15,'4':16,'5':17,'6':18,'7':19,'8':20,'9':21}
		
		op_frutas_verduras = int(input("\nElige una opcion ->"))

		confirmacion = input("Presione cualquier tecla para continuar...")
		clearConsole()

	def Higiene():
		print('\n===HIGIENE===\n\n1.-Shampoo\n2.-Talco\n3.-Desodorante\n4.-Jabon para manos\n5.-Gel\n6.-Perfume\n7.-Crema corporal\n8.-Papel Higienico\n9.-Pasta Dental')

	def Lacteos():
		print('\n==LACTEOS===\n\n1.-Leche Deslactosada\n2.-Yogurt\n3.-Helado\n4.-Queso\n5.-Carnation\n6.-Huevos\n7.-Leche Entera\n8.-Media Crema')

	def Panaderia():
		print('\n===PANADERIA===\n\n1.-Concha\n2.-Orejas\n3.-Besos\n4.-Cocol\n5.-Campechanas\n6.-Garibaldis\n7.-Polvoron\n8.-Ojo de buey\n9.-Cuernitos')

	def Mascotas():
		print('\n===MASCOTAS===\n\n1.-Comida\n2.-Collares/Correas\n3.-Ropa\n4.-Shampoo para perros\n5.-Hueso de juguete')

	def Galletas():
		print('\n===GALLETAS===\n\n1.-Emperador\n2.-Marias\n3.-Principe\n4.-Arcoiris\n5.-Chokis\n6.-Giro\n7.-Canelitas\n8.-Polvorones\n9.-Trikitrakes')

	def Botanas():
		print('\n===SABRITAS===\n\n.1-Doritos\n2.-Ruffles\n3.-Paketaxo\n4.-Rancheritos\n5.-Tostitos\n6.-Crujitos\n7.-Chips\n8.-Cheetos\n9.-Sabritas')

	def Legumbres():
		print('\n===LEGUMBRES===\n\n1.-Frijol\n2.-Arroz\n3.-Lentejas\n4.-Garbanzo\n5.-Maiz Palomero\n6.-Almendras\n7.-Nuez\n8.-Frutas del paraiso')

	def Carniceria():
		print('\n===CARNICERIA===\n\n1.-Chorizo\n2.-Jamone\n3.-Salchicha\n4.-Tocino\n5.-Chicharron\n6.-Carne Deshebrada\n7.-Pollo\n8.-Puerco\n9.-Res')

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