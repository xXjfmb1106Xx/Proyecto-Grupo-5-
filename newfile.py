#esta es la base de el codigo, lo que tenemos por ahora por "base de datos" donde se almacena toda la informacion previa del programa
usuarios {
	
}
peliculas_en_cartelera_y_su_duracion = {
    "Fight Club" : 2.19,
    "For F1" : 2.19,
    "Destino Final Bloodlines" : 1.40,
    "El Lobo de Wall Street" : 3,
    "Oppenheimer" : 3,
    "Barbie" : 1.54,
    "Interestelar" : 2.49,
    "No mires arriba" : 2.25,
    "Birdbox a ciegas" : 2.4,
    "Scary Movie" : 1.28,
    "Terrifier" : 2.5,
    "El resplandor" : 2.26,
    "Sonic 3" : 1.50}
hora_y_sillas_disponibles_sala1 = {
    11 : 96,
    1.05 : 96,
    3 : 96,
    5.10 : 96,
    6.55 : 96 }
hora_y_sillas_disponibles_sala2 = {
    11 : 96,
    12.45 : 96,
    3 : 96,
    5.45 : 96,
    8.25 : 96 }
hora_y_sillas_disponibles_sala3 = {
    11 : 96,
    2.15 : 96,
    5.20 : 96,
    8.10 : 96,
    6.55 : 96 }
hora_y_sillas_disponibles_sala4 = {
    11 : 96,
    1.05 : 96,
    3.25 : 96,
    5.35 : 96,
    8.10 : 96,
    11.10 : 96}
salas_y_sus_horarios = {
    "sala_1" : hora_y_sillas_disponibles_sala1,
    "sala_2" : hora_y_sillas_disponibles_sala2,
    "sala_3" : hora_y_sillas_disponibles_sala3,
    "sala_4" : hora_y_sillas_disponibles_sala4 }
#diccionario individual de las horas en las que estan disponibles cada pelicula y en que sala para facilitar el mostrarlos en interfaz
Fight_Club = { 5.35 : "sala_1", 6.55 : "sala_4" }
For_F1 = {5.20 : "sala_3"}
Destino_Final_bloodlines = { 1.05 : "sala_1" , 8.25 : "sala_2 "}
El_Lobo_de_Wall_Street = {8.10 : "sala_4"}
Oppenheimer = {11 : "sala_3"}
Barbie = { 3 : "saña_1", 3.25 : "sala_4"}
Interestelar = {2.15 : "sala_3" }
No_Mires_Arriba = { 5.45 : "sala_2" }
Birdbox_a_ciegas = {12.45 : "sala_2"}
Scary_Movie = {11 : "sala_ 2", 8.10 : "sala_3"}
Terrifier = {1.05 : "sala_4"}
El_Resplandor = { 3 : "sala_2"}
Sonic_3 = { 11 : "sala_1", 11 : "sala_4"}
#la interfaz que ve el usuario cuando entra a la pagina 
print (f"Cine mundo te da la bienvenida \n ¿Que desea hacer? \n 1. iniciar secion  \n  2.crear cuenta")
camino_inicial = int(input("¿que desea hacer? "))
# la bariable "camino inicial" sirve para ver que desea hacer el usuario y en funcion de eso decidir que hacer
if camino_inicial == 2 :
	usuaros[input("ingrese su nombre de contraseña")] = input("ingrese su usuario")
elif camino_inicial != 1 :
	while camino_inicial != 1 or  camino_inicial != 2 :
		print ("opcion invalida vuelva ha intentarlo")
		print (f"Cine mundo te da la bienvenida \n ¿Que desea hacer? \n 1 iniciar secion  \n  2.crear cuenta")
		camino_inicial = int(input("¿que desea hacer? ")).lowed
print (f" hola Cine mundo te da la bienvenida esta es nuestra cartelera de hoy ; \n ")