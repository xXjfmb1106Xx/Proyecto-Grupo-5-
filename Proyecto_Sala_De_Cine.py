# Diccionario que contiene los usuarios registrados en el sistema (Base de datos)
base_datos = {"test@gmail.com": "qwerty"}  # Su estructura es: {correo electrónico : contraseña}.

# En este caso, ya hay un usuario registrado predeterminado con el correo "test@gmail.com" y la contraseña "qwerty" para hacer testing en el programa.

# Diccionario con las películas disponibles y su duración 
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
    "Sonic 3" : 1.50
}   # La clave representa el nombre de la película y el valor representa la duración en horas.

# Diccionario con los horarios y sillas disponibles para las Salas
hora_y_sillas_disponibles_sala1 = {    # Horarios y sillas para la Sala 1                  
    11 : 96,      # 11:00 am
    13.05 : 96,   # 1:03 pm
    15 : 96,      # 3:00 pm        # Horarios (en horas 24h) y sillas disponibles (96) para cada sala
    17.35 : 96,   # 5:21 pm
    18.55 : 96    # 6:33 pm
}  
# La clave representa la hora en formato 24 horas (como número decimal), y el valor representa cuántas sillas están disponibles (96 en cada horario).


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

# Diccionario que asocia cada sala con sus respectivos horarios y sillas disponibles
# La clave es el nombre de la Sala y el valor es la variable con el diccionario de los horarios
salas_y_sus_horarios = {                       
    "sala_1" : hora_y_sillas_disponibles_sala1,
    "sala_2" : hora_y_sillas_disponibles_sala2,  
    "sala_3" : hora_y_sillas_disponibles_sala3,
    "sala_4" : hora_y_sillas_disponibles_sala4 
}

# Diccionarios que indican en qué horarios y en qué sala se proyecta cada película
# Formato del diccionario: hora (como número decimal) : sala (como texto)

Fight_Club = { 
    17.35: "sala_1",    # A las 5:21 PM se proyecta en la sala 1
    18.55: "sala_4"     # A las 6:33 PM se proyecta en la sala 4
}

F1 = {
    17.20: "sala_3"     # A las 5:12 PM se proyecta en la sala 3
}

Destino_Final = { 
    13.05: "sala_1",    # A la 1:03 PM en la sala 1
    20.25: "sala_2"     # A las 8:15 PM en la sala 2
}

El_Lobo_de_Wall_Street = {
    20.10: "sala_4"     # A las 8:06 PM en la sala 4
}

Oppenheimer = {
    11: "sala_3"        # A las 11:00 AM en la sala 3
}

Barbie = {
    15: "sala_1",       # A las 3:00 PM en la sala 1
    15.25: "sala_4"     # A las 3:25 PM en la sala 4
}

Interestelar = {
    14.15: "sala_3"     # A las 2:09 PM en la sala 3
}

No_Mires_Arriba = { 
    17.45: "sala_2"     # A las 5:27 PM en la sala 2
}

Birdbox_a_ciegas = {
    12.45: "sala_2"     # A las 12:27 PM en la sala 2
}

Scary_Movie = {
    11: "sala_2",       # A las 11:00 AM en la sala 2
    20.10: "sala_3"     # A las 8:06 PM en la sala 3
}

Terrifier = {
    13.05: "sala_4"     # A la 1:03 PM en la sala 4
}

El_Resplandor = { 
    15: "sala_2"        # A las 3:00 PM en la sala 2
}

Sonic_3 = { 
    11: "sala_1",       # A las 11:00 AM en la sala 1
    11.1: "sala_4"      # A las 11:06 AM en la sala 4
}

# Diccionario que asigna un número (como texto) a cada película
# Esto se usa para que el usuario pueda seleccionar una película escribiendo un número

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

while True:  # Bucle principal del programa, se repite hasta que el usuario decida salir por su cuenta
    print(""" ¡Bienvenido a CineMundo! \n 
    ====== MENÚ ====== \n 
    1. Iniciar sesión.  \n  
    2. Crear cuenta.\n
    3. salir. \n""")  # Menú principal mostrado al usuario

    while True:  # Bucle para manejar la opción elegida por el usuario
        opcion = input("Ingrese una de las opciones: ") # Pide al usuario que ingrese una opcion (1/2/3)
        
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
            while True:
                password = input("Ingrese su contraseña: ")

                # Si la contraseña está vacía
                if password == "":
                    print("La contraseña no puede estar vacía.")
                    
                elif password != base_datos[correo]:   # Si la contraseña es incorrecta
                    print("Contraseña incorrecta")
                    
                else:
                    break    # Contraseña válida, salir del bucle

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
            print("Has decidico salir, Gracias por usar nuestro programa.")
            exit()

        else:     # Si ninguna de las otras condiciones se cumple
            print("La opcion ingresada es inválida inténtelo nuevamente.")
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
    
    # str es una función de Python que convierte un valor en una cadena de texto (string).
    pelicula_escogida = str(input("\n¿Qué película deseas ver? elige una opción (1-13): \n"))    # Solicita al usuario una opción del 1 al 13

    while True:    # Inicia un bucle que repetirá la pregunta hasta que se ingrese una opción válida

        if pelicula_escogida not in numerosapelicula.keys():    # Verifica si la opción no está entre las permitidas
            print("La opción ingresada no está entre las opciones disponibles. Inténtelo nuevamente.")  # Muestra mensaje de error
            pelicula_escogida = input("\n¿Qué película deseas ver? elige una opción (1-13): \n")        # Vuelve a pedir la opción al usuario
        else:
            break   # Si la opción es válida, sale del bucle
        
    # Convierte la opción elegida en entero, le resta 1 porque los índices empiezan en 0,
    # y accede a la lista de nombres del diccionario 'peliculas_en_cartelera_y_su_duracion'.
    nombre_pelicula = list(peliculas_en_cartelera_y_su_duracion.keys())[int(pelicula_escogida) - 1]

    # Muestra los horarios disponibles para la película elegida
    print(f"\nHey {nombre} los horarios disponibles para esta función son: \n {numerosapelicula[pelicula_escogida]}\n ")

    # Pide al usuario que ingrese la hora deseada y la redondea a 2 decimales
    hora_escogida = round(float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): ")), 2)

    # Bucle que se repite mientras la hora ingresada no sea válida
    while True:
        if hora_escogida not in numerosapelicula[pelicula_escogida]:
            print("La hora ingresada no está disponible, vuelva a intentarlo.")
            hora_escogida = round(float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): ")), 2)
        else:
            break # Finaliza el bucle
    
    # Obtiene la sala según la hora escogida para esa película
    sala = numerosapelicula[pelicula_escogida][hora_escogida]

    # Muestra un mensaje confirmando la película, hora y sala seleccionadas
    print(f"Has escogido ver '{nombre_pelicula}' a las {hora_escogida} en {sala}.")

    # Consulta cuántos asientos quedan disponibles en esa sala y hora
    asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]

    # Verifica si ya no hay asientos
    if asientos_disponibles <= 0:
        print("No quedan más sillas disponibles.")
        break

    else:
        # Bucle para asegurarse de que el usuario elija una cantidad válida de asientos
        while True:
            print(f"Asientos disponibles: {asientos_disponibles}")
            compra = int(input("¿Cuántos asientos deseas comprar?: "))

            # Valida que la cantidad esté entre 1 y los disponibles
            if compra > asientos_disponibles or compra < 1:
                print("La cantidad seleccionada no es compatible, inténtelo nuevamente.")
            else:
                # Resta los asientos comprados del total disponible
                salas_y_sus_horarios[sala][hora_escogida] -= compra
                break

            
    # Calcula el precio total sin aplicar descuento (cada entrada cuesta $10.000)
    subtotal = compra * 10000
    print(f"Subtotal: ${subtotal}")

    # Aplica un descuento del 10% si se compran más de 4 entradas
    if compra > 4:
        descuento = subtotal * 0.10
        subtotal -= descuento
        print(f"Descuento (10%): -${int(descuento)}")
    else:
        descuento = 0
        print("Descuento: $0")

    # Imprime la factura final con toda la información de la compra
    
     # Imprime la factura final con todos los datos de la compra
    print(f"""
    ------ FACTURA DEL CLIENTE ------

    Nombre del cliente: {nombre}
    Película: {nombre_pelicula}
    Hora: {hora_escogida}
    Sala: {sala}
    Asientos comprados: {compra}
    Precio unitario: $10.000
    Total a pagar: ${int(subtotal)}

    ---------------------------------
    """)

    # Mensaje de despedida para el cliente
    print("\n🍿 Esperamos que disfrutes tu función. ¡Nos vemos en la próxima película! 🍿")

    break    # Sale del bucle principal después de generar la factura