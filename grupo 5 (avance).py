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
    3.25: "sala_4"      # 3:15 AM 
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
    try:
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
        
        pelicula_escogida = input("\n¿Qué película deseas ver? elige una opción (1-13): \n")    # Solicita al usuario una opción del 1 al 13

        if pelicula_escogida == "1":   
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Fight club"    # Guarda el nombre para la factura o resumen
                print(f"\nHey usuario los horarios disponibles para esta funcion son: \n {Fight_Club}\n ")    # Muestra los horarios de Fight Club
                hora_escogida = round(float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): ")),2)    # Pide la hora y redondea a 2 decimales

                if hora_escogida not in Fight_Club:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Fight_Club:    # Verifica si la hora ingresada está en los horarios válidos
                sala = Fight_Club[hora_escogida]    # Obtiene la sala según la hora escogida
                print(f"Has escogido ver 'Fight Club' a las {hora_escogida} en {sala}.")    # Confirma la selección al usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta cuántos asientos quedan en esa sala y hora

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
                            if compra > 4:    # Si compra más de 4 sillas, aplica descuento
                                total = compra * 10000 * 0.9    # Aplica 10% de descuento
                                break    # Sale del bucle
                            else:
                                total = (compra * 10000)    # Precio sin descuento
                                break    # Sale del bucle
                            
        elif pelicula_escogida == "2": 
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "F1"    # Guarda el nombre de la película para factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {F1}\n ")    # Muestra los horarios de F1
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora en formato 24h

                if hora_escogida not in F1:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in F1:    # Verifica si la hora ingresada es válida
                sala = F1[hora_escogida]    # Obtiene la sala según la hora
                print(f"Has escogido ver 'F1' a las {hora_escogida} en {sala}.")    # Confirma la selección
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta los asientos disponibles

                if asientos_disponibles <= 0:    # Si ya no hay sillas
                    print("No quedan más sillas disponibles")    # Informa al usuario
                    break

                else:
                    while True:    # Bucle para validar y procesar la compra de sillas
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cantidad disponible
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita la cantidad

                        if compra > asientos_disponibles or compra < 1:    # Verifica que sea válido
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Error si es inválido
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta los asientos del total
                            if compra > 4:    # Si compró más de 4, aplica descuento
                                total = compra * 10000 * 0.9    # 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal
                                break

        elif pelicula_escogida == "3":  
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Destino final"    # Guarda el nombre de la película para factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Destino_Final}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Pide la hora

                if hora_escogida not in Destino_Final:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Destino_Final:    # Verifica si la hora es válida
                sala = Destino_Final[hora_escogida]    # Obtiene la sala según la hora
                print(f"Has escogido ver 'Destino Final' a las {hora_escogida} en {sala}.")    # Confirma al usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta asientos disponibles

                if asientos_disponibles <= 0:    # Si no hay asientos
                    print("No quedan más sillas disponibles")    # Informa que no hay cupos
                    break

                else:
                    while True:    # Bucle para validar compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cantidad actual
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita cantidad a comprar

                        if compra > asientos_disponibles or compra < 1:    # Verifica si es una cantidad válida
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Descuenta los asientos reservados
                            if compra > 4:    # Si compró más de 4, se aplica descuento
                                total = compra * 10000 * 0.9    # Aplica 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio sin descuento
                                break

        elif pelicula_escogida == "4":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "El Lobo de Wall Street"    # Guarda el nombre para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {El_Lobo_de_Wall_Street}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora deseada

                if hora_escogida not in El_Lobo_de_Wall_Street:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in El_Lobo_de_Wall_Street:    # Verifica si la hora es válida
                sala = El_Lobo_de_Wall_Street[hora_escogida]    # Obtiene la sala asignada
                print(f"Has escogido ver 'El Lobo de Wall Street' a las {hora_escogida} en {sala}.")    # Confirma selección al usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta asientos disponibles

                if asientos_disponibles <= 0:    # Si ya no hay asientos
                    print("No quedan más sillas disponibles")    # Informa al usuario
                    break

                else:
                    while True:    # Bucle para validar la compra de asientos
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cantidad disponible
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita cantidad

                        if compra > asientos_disponibles or compra < 1:    # Valida cantidad ingresada
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta la cantidad comprada
                            if compra > 4:    # Si compra más de 4, se aplica descuento
                                total = compra * 10000 * 0.9    # Aplica 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal
                                break

        elif pelicula_escogida == "5":   
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Oppenheimer"    # Guarda el nombre para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Oppenheimer}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora

                if hora_escogida not in Oppenheimer:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Oppenheimer:    # Verifica si la hora es válida
                sala = Oppenheimer[hora_escogida]    # Obtiene la sala asignada
                print(f"Has escogido ver 'Oppenheimer' a las {hora_escogida} en {sala}.")    # Confirma al usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta los asientos disponibles

                if asientos_disponibles <= 0:    # Si no hay asientos disponibles
                    print("No quedan más sillas disponibles")    # Informa al usuario
                    break

                else:
                    while True:    # Bucle para gestionar la compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cuántos hay disponibles
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita cantidad a comprar

                        if compra > asientos_disponibles or compra < 1:    # Verifica que sea válido
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Descuenta del total disponible
                            if compra > 4:    # Aplica descuento si compró más de 4
                                total = compra * 10000 * 0.9    # 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal
                                break
        
        elif pelicula_escogida == "6":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Barbie"    # Guarda el nombre para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Barbie}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora deseada

                if hora_escogida not in Barbie:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Barbie:    # Verifica si la hora está en el diccionario
                sala = Barbie[hora_escogida]    # Obtiene la sala correspondiente
                print(f"Has escogido ver 'Barbie' a las {hora_escogida} en {sala}.")    # Confirma selección al usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta los asientos disponibles

                if asientos_disponibles <= 0:    # Si no hay sillas
                    print("No quedan más sillas disponibles")    # Mensaje informativo
                    break

                else:
                    while True:    # Bucle de compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cuántos asientos hay
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita la cantidad al usuario

                        if compra > asientos_disponibles or compra < 1:    # Verifica si la cantidad es válida
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta del total disponible
                            if compra > 4:    # Aplica descuento si son más de 4
                                total = compra * 10000 * 0.9    # Descuento del 10%
                                break
                            else:
                                total = compra * 10000    # Precio sin descuento
                                break   # Rompe el while True
                            
        elif pelicula_escogida == "7":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Interestelar"    # Guarda el nombre para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Interestelar}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora deseada

                if hora_escogida not in Interestelar:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Interestelar:    # Verifica si la hora es válida
                sala = Interestelar[hora_escogida]    # Obtiene la sala correspondiente
                print(f"Has escogido ver 'Interestelar' a las {hora_escogida} en {sala}.")    # Confirma la selección
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta asientos disponibles

                if asientos_disponibles <= 0:    # Si no quedan sillas
                    print("No quedan más sillas disponibles")    # Informa al usuario
                    break

                else:
                    while True:    # Bucle de validación de compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra disponibilidad actual
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita cantidad

                        if compra > asientos_disponibles or compra < 1:    # Verifica si la cantidad es válida
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta los asientos comprados
                            if compra > 4:    # Si compró más de 4, aplica descuento
                                total = compra * 10000 * 0.9    # Aplica 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal sin descuento
                                break    # Rompe el while True
        
        elif pelicula_escogida == "8":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "No Mires Arriba"    # Guarda el nombre para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {No_Mires_Arriba}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora deseada

                if hora_escogida not in No_Mires_Arriba:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in No_Mires_Arriba:    # Verifica si la hora ingresada es válida
                sala = No_Mires_Arriba[hora_escogida]    # Obtiene la sala correspondiente
                print(f"Has escogido ver 'No mires arriba' a las {hora_escogida} en {sala}.")    # Confirma la selección
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta asientos disponibles

                if asientos_disponibles <= 0:    # Si no quedan sillas
                    print("No quedan más sillas disponibles")    # Informa al usuario
                    break

                else:
                    while True:    # Bucle de validación de compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra disponibilidad actual
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita cantidad

                        if compra > asientos_disponibles or compra < 1:    # Verifica si la cantidad es válida
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta los asientos comprados
                            if compra > 4:    # Si compró más de 4, aplica descuento
                                total = compra * 10000 * 0.9    # Aplica 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal sin descuento
                                break
                            
        elif pelicula_escogida == "9":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Bird Box: a ciegas"    # Guarda el nombre para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Birdbox_a_ciegas}\n ")    # Muestra horarios disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita la hora deseada

                if hora_escogida not in Birdbox_a_ciegas:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Birdbox_a_ciegas:    # Verifica si la hora es válida
                sala = Birdbox_a_ciegas[hora_escogida]    # Obtiene la sala correspondiente
                print(f"Has escogido ver 'Bird Box: a ciegas' a las {hora_escogida} en {sala}.")    # Corrige el nombre mostrado
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta asientos disponibles

                if asientos_disponibles <= 0:    # Si no hay sillas disponibles
                    print("No quedan más sillas disponibles")    # Informa al usuario
                    break

                else:
                    while True:    # Bucle de validación de compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra la disponibilidad actual
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita la cantidad

                        if compra > asientos_disponibles or compra < 1:    # Verifica si la cantidad es válida
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta los asientos comprados
                            if compra > 4:    # Aplica descuento si son más de 4
                                total = compra * 10000 * 0.9    # 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal sin descuento
                                break

        elif pelicula_escogida == "10":    
            while True: #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Scary Movie"    # Guarda el nombre de la película seleccionada
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Scary_Movie}\n ")    # Muestra en pantalla los horarios de esta comedia/parodia
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Captura la hora deseada por el usuario

                if hora_escogida not in Scary_Movie:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Scary_Movie:    # Verifica si esa hora está en cartelera para Scary Movie
                sala = Scary_Movie[hora_escogida]    # Obtiene la sala asignada a esa hora
                print(f"Has escogido ver 'Scary Movie' a las {hora_escogida} en {sala}.")    # Muestra al usuario su selección final
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Consulta cuántas sillas hay en esa sala a esa hora

                if asientos_disponibles <= 0:    # Valida si no quedan sillas disponibles
                    print("No quedan más sillas disponibles")    # Mensaje directo si está agotado el cupo
                    break

                else:
                    while True:    # Repite hasta que la compra de sillas sea válida
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra en tiempo real cuántos hay disponibles
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita la cantidad deseada

                        if compra > asientos_disponibles or compra < 1:    # Controla errores como cantidades negativas o muy grandes
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Advierte que la compra no es válida
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Actualiza la disponibilidad restando lo comprado
                            if compra > 4:    # Si compra más de 4, se le otorga un descuento automático
                                total = compra * 10000 * 0.9    # Descuento aplicado del 10% por compra grupal
                                break
                            else:
                                total = compra * 10000    # Precio estándar por entrada sin descuento
                                break
                
        elif pelicula_escogida == "11":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Terrifier"    # Guarda el nombre de la película para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Terrifier}\n ")    # Muestra al usuario los horarios disponibles
                print("Advertencia: Esta película contiene escenas fuertes.")    # Mensaje especial por ser de terror
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita al usuario la hora deseada

                if hora_escogida not in Terrifier:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Terrifier:    # Verifica si esa hora está disponible para la película
                sala = Terrifier[hora_escogida]    # Obtiene la sala correspondiente
                print(f"Has escogido ver 'Terrifier' a las {hora_escogida} en {sala}.")    # Muestra un resumen de la elección del usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Verifica cuántos asientos quedan en esa función

                if asientos_disponibles <= 0:    # Si ya no quedan sillas disponibles
                    print("No quedan más sillas disponibles")    # Mensaje directo si está agotada
                    break

                else:
                    while True:    # Bucle hasta que se haga una compra válida
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Informa la cantidad de sillas que aún hay
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita la cantidad de entradas

                        if compra > asientos_disponibles or compra < 1:    # Verifica que la cantidad tenga sentido
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Informa del error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta del total de sillas disponibles
                            if compra > 4:    # Aplica descuento por compra grande
                                total = compra * 10000 * 0.9    # Descuento del 10%
                                break
                            else:
                                total = compra * 10000    # Precio estándar
                                break

        elif pelicula_escogida == "12":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "El Resplandor"    # Se guarda el nombre correcto para la factura
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {El_Resplandor}\n ")    # Muestra las funciones disponibles
                print("Prepárate para un clásico del suspenso.")    # Mensaje especial por el género
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita al usuario la hora deseada

                if hora_escogida not in El_Resplandor:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in El_Resplandor:    # Verifica si esa hora está disponible
                sala = El_Resplandor[hora_escogida]    # Obtiene la sala asignada a esa hora
                print(f"Has escogido ver 'El Resplandor' a las {hora_escogida} en {sala}.")    # Confirmación de la selección
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Obtiene los asientos disponibles

                if asientos_disponibles <= 0:    # Verifica si ya no hay sillas
                    print("No quedan más sillas disponibles")    # Informa que está llena
                    break

                else:
                    while True:    # Repite hasta que la compra sea válida
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra disponibilidad actual
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Solicita cantidad de entradas

                        if compra > asientos_disponibles or compra < 1:    # Valida que la cantidad tenga sentido
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Advierte si hay error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Resta los asientos comprados
                            if compra > 4:    # Aplica descuento por grupo
                                total = compra * 10000 * 0.9    # 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio sin descuento
                                break
        
        elif pelicula_escogida == "13":    
            while True : #se inicia un bucle para en caso de ingresar una hora no valida vuelva a solicitar la hora
                nombre_pelicula_factura = "Sonic 3"    # Guarda el título para la factura final
                print(f"\nHey usuario, los horarios disponibles para esta función son: \n {Sonic_3}\n ")    # Muestra las funciones disponibles
                hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))    # Solicita el horario deseado

                if hora_escogida not in Sonic_3:     # Si la hora ingresada por el usuario no está en los horarios 
                    print("La hora ingresada no esta disponible, vuelva a intentarlo.")
                else:     # Si está rompe el bucle y continua con el código
                    break
                
            if hora_escogida in Sonic_3:    # Verifica si esa hora está programada
                sala = Sonic_3[hora_escogida]    # Asigna la sala correspondiente
                print(f"Has escogido ver 'Sonic 3' a las {hora_escogida} en {sala}.")    # Confirmación visual al usuario
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]    # Verifica disponibilidad en esa sala y horario

                if asientos_disponibles <= 0:    # Si no hay asientos disponibles
                    print("No quedan más sillas disponibles")    # Informa que ya no hay cupo
                    break

                else:
                    while True:    # Bucle para validar compra
                        print(f"Asientos disponibles: {asientos_disponibles}")    # Muestra cuántos puestos quedan
                        compra = int(input("¿Cuántos asientos deseas comprar? "))    # Pregunta cuántas entradas desea comprar

                        if compra > asientos_disponibles or compra < 1:    # Valida que sea una cantidad lógica
                            print("La cantidad seleccionada no es compatible, inténtelo nuevamente")    # Mensaje de error
                        else:
                            salas_y_sus_horarios[sala][hora_escogida] -= compra    # Actualiza los asientos disponibles
                            if compra > 4:    # Si compra más de 4, aplica un descuento automático
                                total = compra * 10000 * 0.9    # Precio con 10% de descuento
                                break
                            else:
                                total = compra * 10000    # Precio normal
                                break
                            
    # Maneja errores cuando la clave/hora no está en el diccionario                        
    except KeyError:    
        print("Estimado usuario, ingrese una opción válida. Inténtelo de nuevo.")  
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
    -------- FACTURA DEL CLIENTE --------
    
    Nombre del cliente: {nombre}
    Película: {nombre_pelicula_factura}
    Hora: {hora_escogida}
    Sala: {sala}
    Asientos comprados: {compra}
    Precio unitario: $10.000 
    total a pagar : {subtotal}
    
    ------------------------------------ """) 
    
    print("\n🍿 Esperamos que disfrutes tu función. ¡Nos vemos en la próxima película! 🍿") 
    break    # Sale del bucle principal después de generar la factura