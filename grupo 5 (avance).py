# Diccionario que contendrá a todos los usuarios registrados
base_datos = {"test@gmail.com" : "qwerty"} 

peliculas_en_cartelera_y_su_duracion = {    # diccionario con peliculas elegidas y su duracion
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
}

hora_y_sillas_disponibles_sala1 = {                      # lo explica  Cadena
    11 : 96,
    13.05 : 96,
    15 : 96,
    17.35 : 96,
    18.55 : 96 
}

hora_y_sillas_disponibles_sala2 = {
    11 : 96,
    12.45 : 96,
    15: 96,
    17.45 : 96,
    20.25 : 96 
}

hora_y_sillas_disponibles_sala3 = {
    11 : 96,
    14.15 : 96,
    17.20 : 96,
    20.10 : 96,
    6.55 : 96 
}

hora_y_sillas_disponibles_sala4 = {
    11 : 96,
    13.05 : 96,
    15.25 : 96,
    18.55 : 96,
    20.10 : 96,
    23.10 : 96
}

salas_y_sus_horarios = {                       
    "sala_1" : hora_y_sillas_disponibles_sala1,
    "sala_2" : hora_y_sillas_disponibles_sala2,
    "sala_3" : hora_y_sillas_disponibles_sala3,
    "sala_4" : hora_y_sillas_disponibles_sala4 
}

# diccionario que contiene de las horas en las que estan disponibles cada pelicula y en que sala para facilitar el mostrarlos en interfaz
Fight_Club = { 
    17.35 : "sala_1",
    18.55 : "sala_4" 
}
F1 = {
    17.20 : "sala_3"
}
Destino_Final = { 
    13.05 : "sala_1" ,
    20.25 : "sala_2 "
}
El_Lobo_de_Wall_Street = {
    20.10 : "sala_4"
}
Oppenheimer = {
    11 : "sala_3"
}
Barbie = {
    15 : "sala_1", 3.25 : "sala_4"
}
interestelar = {
    14.15 : "sala_3"
}
No_Mires_Arriba = { 
    17.45 : "sala_2"
}
Birdbox_a_ciegas = {
    12.45 : "sala_2"
}
Scary_Movie = {
    11 : "sala_ 2",
    20.10 : "sala_3" 
}
Terrifier = {
    13.05 : "sala_4"
}
El_Resplandor = { 
    15 : "sala_2"
}
Sonic_3 = { 
    11 : "sala_1",
    11 : "sala_4"
}

while True:
    print(""" ¡Bienvenido a CineMundo! \n 
    ====== MENÚ ====== \n 
    1. Iniciar sesion.  \n  
    2. Crear cuenta.\n
    3. salir. \n""")

    try:
        opcion = input("Ingrese una de las opciones: ")
        if opcion == "1":
            usuario = input("ingrese su correo: ")
            if usuario in base_datos:
                password = input("ingrese su contraseña: ")
                while password != base_datos[usuario]:
                    print("contraseña incorrecta")
                    password = input("vuelva a ingresar su contraseña: ")
                print("Inicio de sesión exitoso.")
                break
            else:
                print("usuario incorrecto vuelva ha ingresar su usuario")
                while usuario not in base_datos:
                    usuario = input("ingrese su correo: ")
                password = input("ingrese su contraseña: ")
                while password != base_datos[usuario]:
                    print("contraseña incorrecta")
                    password = input("vuelva a ingresar su contraseña: ")
                print("Inicio de sesión exitoso.")
                break
        elif opcion == "2":
            usuario = input("Ingrese su correo: ")
            verificacion_correo = base_datos.keys()
            while usuario in verificacion_correo :
                print("el correo ingresado ya está registrado ingrese un nuevo correo")
                usuario = input("Ingrese su correo: ")
            contraseña = input("ingrese la contraseña a crear ")
            base_datos[usuario] = contraseña
            print("cuenta creada exitosamente")
            break
    
        elif opcion == "3":
            exit()
    except ValueError:
        print("opcion invalida")

nombre = input("Ingrese el nombre de usuario: ")

while True: 
    try:
        print("""
        =========== 🎬 ¡Bienvenido a CineMundo! 🎬 ===========\n
        
        =======================================================
        ====== 📽️ PELÍCULAS DISPONIBLES EN CARTELERA 📽️ ======
        ======================================================= 
        
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
        
        ==========================================================
        ====== 🍿 ELIJE TU PELÍCULA FAVORITA Y DISFRUTA 🍿 ======
        ==========================================================
        """)
        
        pelicula_escogida = input("\n¿Qué película deseas ver? elije una opción (1-13): \n")
        
        if pelicula_escogida == "1":
            nombre_pelicula_factura = "Fight club"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Fight_Club}\n ")
            hora_escogida = round(float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): ")),2)
            if hora_escogida in Fight_Club:
            
                sala = Fight_Club[hora_escogida]
                print(f"Has escogido ver 'Fight Club' a las {hora_escogida} en {sala}.")
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
                        
        elif pelicula_escogida == "2": 
            nombre_pelicula_factura = "F1"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {F1}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in F1:
                sala = F1[hora_escogida]
                print(f"Has escogido ver 'F1' a las {hora_escogida} en {sala}.")
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)

        elif pelicula_escogida == "3": 
            nombre_pelicula_factura = "Destino final"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Destino_Final}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Destino_Final:
                sala = Destino_Final[hora_escogida]
                print(f"Has escogido ver 'Destino Final' a las {hora_escogida} en {sala}.")
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)

        elif pelicula_escogida == "4": 
            nombre_pelicula_factura = "El Lobo de Wall Street"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {El_Lobo_de_Wall_Street}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in El_Lobo_de_Wall_Street:
                sala = El_Lobo_de_Wall_Street[hora_escogida]
                print(f"Has escogido ver 'El Lobo de Wall Street' a las {hora_escogida} en {sala}.")
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida]
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)

        elif pelicula_escogida == "5": 
            nombre_pelicula_factura = "Oppenheimer"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Oppenheimer}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Oppenheimer:
                sala = Oppenheimer[hora_escogida]
                print(f"Has escogido ver 'Oppenheimer' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        
        elif pelicula_escogida == "6": 
            nombre_pelicula_factura = "Barbie"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Barbie}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Barbie:
                sala = Barbie[hora_escogida]
                print(f"Has escogido ver 'Barbie' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        elif pelicula_escogida == "7": 
            nombre_pelicula_factura = "Interestelar"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {interestelar}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in interestelar:
                sala = interestelar[hora_escogida]
                print(f"Has escogido ver 'Intestelar' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        
        elif pelicula_escogida == "8": 
            nombre_pelicula_factura = "No Mires Arribva"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {No_Mires_Arriba}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in No_Mires_Arriba:
                sala = No_Mires_Arriba[hora_escogida]
                print(f"Has escogido ver 'No mires arriba' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        elif pelicula_escogida == "9": 
            nombre_pelicula_factura = "Bird Box: a ciegas"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Birdbox_a_ciegas}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Birdbox_a_ciegas:
                sala = Birdbox_a_ciegas[hora_escogida]
                print(f"Has escogido ver 'Scary Movie' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        elif pelicula_escogida == "10": 
            nombre_pelicula_factura = "Scary Movie"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Scary_Movie}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Scary_Movie:
                sala = Scary_Movie[hora_escogida]
                print(f"Has escogido ver 'Scary Movie' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
                
        elif pelicula_escogida == "11": 
            nombre_pelicula_factura = "Terrifier"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Terrifier}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Terrifier:
                sala = Terrifier[hora_escogida]
                print(f"Has escogido ver 'Terrifier' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        elif pelicula_escogida == "12": 
            nombre_pelicula_factura = "El Resplandora"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {El_Resplandor}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in El_Resplandor:
                sala = El_Resplandor[hora_escogida]
                print(f"Has escogido ver 'El Resplandor' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
        
        elif pelicula_escogida == "13": 
            nombre_pelicula_factura = "Sonic 3"
            print(f"Hey usuario los horarios disponibles para esta funcion son: \n {Sonic_3}\n ")
            hora_escogida = float(input("¿A qué hora desea ver la película? (ingrese el horario en formato 24 horas): "))
            if hora_escogida in Sonic_3:
                sala = Sonic_3[hora_escogida]
                print(f"Has escogido ver 'Sonic_3' a las {hora_escogida} en {sala}.") 
                asientos_disponibles = salas_y_sus_horarios[sala][hora_escogida] 
                if asientos_disponibles <= 0 :
                    print ("no quedan mas sillas disponibles")
                    break
                else:
                    print(f"Asientos disponibles: {asientos_disponibles}")
                    compra = int(input("cuantos asientos deseas comprar? "))
                    asientos_disponibles -= compra
                    if compra > 4 :
                        total = ((compra * 10000)-((10/(10000 * compra))*100)) 
                    else :
                        total = (compra * 10000)
    except KeyError:
        print("Estimado usuario, ingrese una opción válida. Inténtelo de nuevo.")
        
    subtotal = compra * 10000
    (f"Subtotal: ${subtotal}")
    if compra > 4:
        descuento = subtotal * 0.10 
        subtotal -= descuento 
        print(f"Descuento (10%): -${int(descuento)}")
    else:
        descuento = 0 
        print("Descuento: $0")
        
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
    break
