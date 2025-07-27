# Diccionario que contiene los usuarios registrados en el sistema
base_datos = {"test@gmail.com": "qwerty"}  # Formato: correo electrónico : contraseña

peliculas_en_cartelera_y_su_duracion = {    
    "Fight Club" : 2.19,                   
    "For F1" : 2.19,                        
    "Destino Final Bloodlines" : 1.40,      
    "El Lobo de Wall Street" : 3,           
    "Oppenheimer" : 3,                      
    "Barbie" : 1.54,                        
    "Interestelar" : 2.49,                  # Diccionario con las películas disponibles y su duración en horas
    "No mires arriba" : 2.25,
    "Birdbox a ciegas" : 2.4,
    "Scary Movie" : 1.28,
    "Terrifier" : 2.5,
    "El resplandor" : 2.26,
    "Sonic 3" : 1.50
}

# Diccionario con los horarios y sillas disponibles para las Salas
hora_y_sillas_disponibles_sala1 = {    # Horarios y sillas para la Sala 1                  
    11 : 96,      # 11:00 am
    13.05 : 96,   # 1:03 pm
    15 : 96,      # 3:00 pm        # Horarios (en horas 24h) y sillas disponibles (96) para cada sala
    17.35 : 96,   # 5:21 pm
    18.55 : 96    # 6:33 pm
}

hora_y_sillas_disponibles_sala2 = {    # Horarios y sillas para la Sala 2
    11 : 96,      # 11:00 AM
    12.45 : 96,   # 12:27 PM
    15: 96,       # 3:00 PM
    17.45 : 96,   # 5:27 PM
    20.25 : 96    # 8:15 PM
}

hora_y_sillas_disponibles_sala3 = {    # Horarios y sillas para la Sala 3
    11: 96,       # 11:00 AM
    14.15: 96,    # 2:09 PM
    17.20: 96,    # 5:12 PM
    20.10: 96,    # 8:06 PM
    06.55: 96     # 6:33 PM 
}

hora_y_sillas_disponibles_sala4 = {    # Horarios y sillas para la Sala 4
    11.1: 96,     # 11:06 AM
    13.05: 96,    # 1:03 PM
    15.25: 96,    # 3:15 PM
    18.55: 96,    # 6:33 PM
    20.10: 96,    # 8:06 PM
    23.10: 96     # 11:06 PM
}

salas_y_sus_horarios = {                       
    "sala_1" : hora_y_sillas_disponibles_sala1,
    "sala_2" : hora_y_sillas_disponibles_sala2,  # Diccionario que asocia cada sala con sus respectivos horarios y sillas disponibles
    "sala_3" : hora_y_sillas_disponibles_sala3,
    "sala_4" : hora_y_sillas_disponibles_sala4 
}

# Diccionarios que indican en qué horarios y en qué sala se proyecta cada película
# Formato: hora (float) : sala (string)

Fight_Club = { 
    17.35: "sala_1",    # 5:21 PM
    18.55: "sala_4"     # 6:33 PM
}

F1 = {
    17.20: "sala_3"     # 5:12 PM
}

Destino_Final = { 
    13.05: "sala_1",    # 1:03 PM
    20.25: "sala_2"     # 8:15 PM
}

El_Lobo_de_Wall_Street = {
    20.10: "sala_4"     # 8:06 PM
}

Oppenheimer = {
    11: "sala_3"        # 11:00 AM
}

Barbie = {
    15: "sala_1",       # 3:00 PM
    15.25: "sala_4"      # 3:25 pm 
}

Interestelar = {
    14.15: "sala_3"     # 2:09 PM
}

No_Mires_Arriba = { 
    17.45: "sala_2"     # 5:27 PM
}

Birdbox_a_ciegas = {
    12.45: "sala_2"     # 12:27 PM
}

Scary_Movie = {
    11: "sala_2",       # 11:00 AM
    20.10: "sala_3"     # 8:06 PM
}

Terrifier = {
    13.05: "sala_4"     # 1:03 PM
}

El_Resplandor = { 
    15: "sala_2"        # 3:00 PM
}

Sonic_3 = { 
    11: "sala_1",       # 11:00 AM
    11.1: "sala_4"      # 11:06 AM
}

numerosapelicula = {
    "1" : Fight_Club,
    "2" : F1,
    "3" : Destino_Final,
    "4" : El_Lobo_de_Wall_Street,
    "5" : Oppenheimer,
    "6" : Barbie,
    "7" : Interestelar,
    "8" : No_Mires_Arriba,
    "9" : Birdbox_a_ciegas,
    "10" : Scary_Movie,
    "11" : Terrifier,
    "12" : El_Resplandor,
    "13" : Sonic_3
}

while True:  # Bucle principal del programa, se repite hasta que el usuario decida salir
    print(""" ¡Bienvenido a CineMundo! \n 
    ====== MENÚ ====== \n 
    1. Iniciar sesión.  \n  
    2. Crear cuenta.\n
    3. salir. \n""")  # Menú principal mostrado al usuario

    while True:  # Bucle para manejar la opción elegida por el usuario
        opcion = input("Ingrese una de las opciones: ")
        
        if opcion == "1":    # Opción para iniciar sesión
            correo = input("Ingrese su correo: ") 
            while correo == "":    # Mientras el correo esté vacío
                print("El correo no puede estar vacío.")
                correo = input("Ingrese su correo: ")    # Pide el correo de nuevo

            while correo not in base_datos:     # Mientras el correo no esté en la base de datos
                print("El correo es incorrecto, inténtelo de nuevo.")
                correo = input("Ingrese su correo: ")
                while correo == "":    # Mientras el correo esté vacío
                    print("El correo no puede estar vacío.")
                    correo = input("Ingrese su correo: ")     # Pide al usuario que ingrese el correo de nuevo

            # Si el correo es válido se pide la contraseña 
            password = input("Ingrese su contraseña: ")
            while password == "":    # Mientras la contraseña esté vacía
                print("La contraseña no puede estar vacía.")
                password = input("Ingrese su contraseña: ")    # Pide al usuario que ingrese la contraseña de nuevo

            while password != base_datos[correo]:   # Mientras la contraseña sea diferente al valor asignado a la clave del correo 
                print("Contraseña incorrecta")
                password = input("Vuelva a ingresar su contraseña: ")    # Pide al usuario que ingrese la contraseña de nuevo 

            print("Inicio de sesión exitoso.")
            break  # Sale del bucle al iniciar sesión correctamente
            
        elif opcion == "2":     # Crear cuenta nueva
            correo = input("Ingrese su correo: ")    # Pide el correo al usuario
            while correo == "" or correo in base_datos:    # Si en el correo hay un campo vacío o el correo ya está registrado
                
                # Si en el correo hay un campo vacío
                if correo == "":
                    print("El correo no puede estar vacío.")
                # Si el correo ya está registrado
                else:
                    print("El correo ingresado ya está registrado ingrese un nuevo correo.")
                correo = input("Ingrese su correo: ")

            contraseña = input("Ingrese su contraseña: ")
            while contraseña == "":    # Mientras la contraseña ingresada esté vacía
                print("La contraseña no puede estar vacía.")
                contraseña = input("Ingrese su contraseña: ")

            base_datos[correo] = contraseña    # Guarda el nuevo usuario y su contraseña
            print("Cuenta creada exitosamente.")
            break    # Sale del bucle después de crear la cuenta

        elif opcion == "3":     # Salir del programa
            print("Has decidico salir del programa, hasta luego.")
            exit()

        else:     # Si ninguna de las otras condiciones se cumple
            print("La opcion ingresada es inválida inténtelo nuevamente")
    break     # Termina el bucle principal después de procesar la opción

nombre = input("Ingrese el nombre de usuario: ")    # Solicita el nombre del usuario que ha iniciado sesión

while nombre.strip() == "":    # .strip() elimina espacios al principio y al final. Si alguien escribe solo " " también se considera vacío.
    print("El nombre de usuario no puede estar vacío.")
    nombre = input("Ingrese el nombre de usuario: ")     

while True:     # Bucle principal para mostrar cartelera y permitir seleccionar una película
    
    # Muestra la cartelera de películas disponibles 
    print("""
    ============== ¡Bienvenido a CineMundo! ==============\n
    
    ======================================================
    ========= PELÍCULAS DISPONIBLES EN CARTELERA =========
    ====================================================== 
    
    - 1. Fight Club 
    - 2. F1
    - 3. Destino Final
    - 4. El Lobo de Wall Street
    - 5. Oppenheimer
    - 6. Barbie
    - 7. Interestelar
    - 8. No mires arriba
    - 9. Birdbox: a ciegas
    - 10. Scary Movie
    - 11. Terrifier
    - 12. El resplandor
    - 13. Sonic 3 
    
    =========================================================
    ========= ELIGE TU PELÍCULA FAVORITA Y DISFRUTA =========
    =========================================================
    """)      
    
    pelicula_escogida = str(input("\n¿Qué película deseas ver? elige una opción (1-13): \n"))    # Solicita al usuario una opción del 1 al 13
    while True :
        if pelicula_escogida not in numerosapelicula.keys():
            print ("la opcion ingresada no esta entre las opciones disponibles intentelo nuevamente")
            pelicula_escogida = input("\n¿Qué película deseas ver? elige una opción (1-13): \n")
        else:
            break
    nombre_pelicula = list(peliculas_en_cartelera_y_su_duracion.keys())[int(pelicula_escogida) - 1]
    print(f"\nHey {nombre} los horarios disponibles para esta funcion son: \n {numerosapelicula[pelicula_escogida]}\n ")    # Muestra los horarios de Fight Club
    hora_escogida = round(float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): ")),2)    # Pide la hora y redondea a 2 decimales
    while True:
        if hora_escogida not in numerosapelicula[pelicula_escogida]:     # Si la hora ingresada por el usuario no está en los horarios 
            print("La hora ingresada no esta disponible, vuelva a intentarlo.")
            hora_escogida = round(float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): ")),2)
        else:     # Si está rompe el bucle y continua con el código
            break
    
    sala = numerosapelicula[pelicula_escogida][hora_escogida]   # Obtiene la sala según la hora escogida
    print(f"Has escogido ver '{nombre_pelicula}' a las {hora_escogida} en {sala}.")    # Confirma la selección al usuario
    asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    
    if asientos_disponibles <= 0:    # Si ya no hay asientos disponibles
        print ("no quedan mas sillas disponibles")    # Informa al usuario
        break    # Sale del bucle
    else:    # Si hay asientos disponibles
        while True:    # Bucle para validar la cantidad de asientos a comprar
            print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cuántos asientos hay
            compra = int(input("cuantos asientos deseas comprar?: "))    # Pide la cantidad a comprar
            if compra > asientos_disponibles or compra < 1:    # Verifica que la cantidad sea válida
                print("la cantidad seleccionada no es compatible, inténtelo nuevamente.")    # Error si supera o es menor a 1
            else:
                salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta los asientos comprados del total disponible
                break
    subtotal = compra * 10000    #  Calcula el precio total sin descuento
    print(f"Subtotal: ${subtotal}")    #  Muestra el subtotal al usuario
    
    if compra > 4:    
        descuento = subtotal * 0.10    #  Aplica un 10% de descuento por más de 4 entradas
        subtotal -= descuento    #  Resta el descuento al subtotal
        print(f"Descuento (10%): -${int(descuento)}")    #  Muestra el descuento aplicado como número entero
    else:    
        descuento = 0    #  No hay descuento si se compran 4 o menos entradas
        print("Descuento: $0")    #  Informa que no se aplicó ningún descuento
        
    # Imprime la factura final con toda la información de la compra
    print(f"""
    ------ FACTURA DEL CLIENTE ------
    
    Nombre del cliente: {nombre}
    Película: {nombre_pelicula}
    Hora: {hora_escogida}
    Sala: {sala}
    Asientos comprados: {compra}
    Precio unitario: $10.000 
    total a pagar : ${subtotal}
    
    --------------------------------- """) 
    
    print("\n🍿 Esperamos que disfrutes tu función. ¡Nos vemos en la próxima película! 🍿") 
    break    # Sale del bucle principal después de generar la factura