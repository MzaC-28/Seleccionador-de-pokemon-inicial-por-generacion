# Bienvenida al sistema
while True:
    print("="*56)
    print("BIENVENIDO AL BUSCADOR DE POKEMONES INICIALES")
    print("="*56)
    # Elegir una generación
    while True:
        try:
            print("="*35)
            print("Generaciones a elegir")
            print("1. Gen 1\n2. Gen 2\n3. Gen 3\n4. Gen 4\n5. Gen 5 \n6. Gen 6\n7. Gen 7\n8. Gen 8\n9. Gen 9\n10. Salir")
            print("="*35)
            generacion_pokemon = int(input("Por favor, elija número de generación a elegir (1 a 10): "))
            if 0 < generacion_pokemon <= 10:
                break
            else:
                print("Por favor, solo números del 1 al 10.")
        except ValueError:
            print("Por favor, solamente dígitos ")
    # Comienza con eleccion de generación        
    match generacion_pokemon:
        case 1:
            print("Opciones:")
            print("1. Buscar un pokemon inicial")
            print("2. Pokemon especial")
            while True:
                try:
                    print("="*35)
                    opcion = int(input("Ingrese una opcion, por favor: "))
                    print("="*35)
                    if 0 < opcion <= 2:
                        break
                    else:
                        print("-"*42)
                        print("Por favor seleccione del 1 al 2 por favor")
                        print("-"*42)
                except ValueError:
                    print("-"*20)
                    print("Solamente digitos")
                    print("-"*20)
            match opcion:
                case 1:
                    while True:
                        while True:
                            try:
                                print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                                tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                                if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                                    break
                                else:
                                    print("Por favor, elija solamente una de las tres opciones.")
                            except ValueError:
                                None
                        match tipo_pokemon:
                            case "Fuego":
                                print("Usted eligió tipo: Fuego.")
                                print("Su pokemon será: Charmander")
                                print("Número en la pokedex: 004")
                                            
                            case "Agua":
                                print("Usted eligió tipo: Agua.")
                                print("Su pokemon será: Squirtle")
                                print("Número en la pokedex: 007")
                                        
                            case "Planta":
                                print("Usted eligió tipo: Planta.")
                                print("Su pokemon será: Bulbasaur")
                                print("Número en la pokedex: 001") 
                        break        
                case 2:          
                    print("El pokemon especial que eligio es tipo: Eléctrico.")
                    print("Su pokemon será: Pikachu")
                    print("Número en la pokedex: 025")
                    print("Nota: Pokemon raro")
                        
                case _:
                    print("Por favor elija una opcion de (1 a 2)")
        case 2: 
            while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Cyndaquil")
                        print("Número en la pokedex: 155")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Totodile")
                        print("Número en la pokedex: 158")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Chikorita")
                        print("Número en la pokedex: 152")
                break        
            
        case 3:
            while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Torchic")
                        print("Número en la pokedex: 255")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Mudkip")
                        print("Número en la pokedex: 258")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Treecko")
                        print("Número en la pokedex: 252")
                break    
        case 4:
            while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Chimchar")
                        print("Número en la pokedex: 390")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Piplup")
                        print("Número en la pokedex: 393")
                                            
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Turtwig")
                        print("Número en la pokedex: 387")
                break
        case 5:
             while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Tepig")
                        print("Número en la pokedex: 498")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Oshawott")
                        print("Número en la pokedex: 501")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Snivy")
                        print("Número en la pokedex: 495")
            
                    case _:
                        print("Ese tipo no se encuentra disponible")
                    
        case 6:
             while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Fennekin")
                        print("Número en la pokedex: 653")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Froakie")
                        print("Número en la pokedex: 656")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Chespin")
                        print("Número en la pokedex: 650")
            
                    case _:
                        print("Ese tipo no se encuentra disponible")
                    
        case 7:
            while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Litten")
                        print("Número en la pokedex: 725")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Popplio")
                        print("Número en la pokedex: 728")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta/Volador.")
                        print("Su pokemon será: Rowlet")
                        print("Número en la pokedex: 722")
                break

        case 8:
             while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Scorbunny")
                        print("Número en la pokedex: 813")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Sobble")
                        print("Número en la pokedex: 816")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Grookey")
                        print("Número en la pokedex: 810")
                break    
        case 9:
             while True:
                while True:
                    try:
                        print("Elija un tipo entre (Fuego)(Agua)(Planta)\nTipo:")
                        tipo_pokemon = str(input("Ingrese el tipo del pokemon: ")).replace(" ","")
                        if tipo_pokemon.isalpha() and tipo_pokemon.startswith("F") or tipo_pokemon.startswith("A") or tipo_pokemon.startswith("P"):
                            break
                        else:
                            print("Por favor, elija una de las tres opciones.")
                    except ValueError:
                        None
                match tipo_pokemon:
                    case "Fuego":
                        print("Usted eligió tipo: Fuego.")
                        print("Su pokemon será: Fuecoco")
                        print("Número en la pokedex: 909")
                                            
                    case "Agua":
                        print("Usted eligió tipo: Agua.")
                        print("Su pokemon será: Quaxly")
                        print("Número en la pokedex: 912")
                                        
                    case "Planta":
                        print("Usted eligió tipo: Planta.")
                        print("Su pokemon será: Sprigatito")
                        print("Número en la pokedex: 906")
                break
                    
        case 10:
            print("Gracias por usar el buscador de pokemon inicial.")
            break            
                            
                            
                           
            
        
    
               
                               