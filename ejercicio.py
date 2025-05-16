'''
Hecho por Ramcess / Fecha: 15-05 

Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de la UAM,
durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por sección. El programa 
deberá contabilizar y mostrar el total de asistencias registradas por sección, así como el total general de la semana.

'''

asistencia_sec1 = [] # Aqui creamos 3 listas vacias donde almacenaremos las asistencias de cada seccion 
asistencia_sec2 = []
asistencia_sec3 = []

for i in range (1, 4, 1): # Primer bucle for donde decimos que iniciara en 1 y terminara en 3, este ciclo es para las secciones
    print (f'Pasando asistencia de la seccion {i}')
    for n in range (1, 6, 1): # Segundo ciclo for donde iniciara igual y terminara en 5, este ciclo es para los dias 
        print(f'Seccion {i} dia {n}')
        for x in range (1, 7, 1): # Ultimo ciclo for que incia igual y terminar en 6, este ciclo es para los estudiantes 
            while True: # Empezamos un bucle para las validaciones de datos
                try: # Aqui empezamos la validaciones con el try , except 
                    attend = int(input(f'''El estudiante {x} de la seccion {i} esta presente el dia {n}
                    >>> 1) - Si 
                    >>> 2) - No
                    >>> '''))
                    if attend < 1 or attend > 2: # Si la variable attend es menor a 1 o mayor a 3 entonces pasamos al bloque except 
                        raise ValueError
                    elif not isinstance(attend, int): # Aqui decimos que si la variable attend almacena otro tipo de dato que no sea entero dara un error y llamamos al bloque except
                        raise TypeError 
                    break #  Si ninguna condicion se cumple, quiere decir que las validaciones son correctos y terminamos el bucle while 
                except (ValueError, TypeError) as e: # Este es el bloque de errores importamos los errores Value y Type como variable e para luego imprimirla en consola
                    print(e)
                    print('Por favor ingrese un rango de numeros acorde (1-2)')
                
                    
            if attend == 1: # Cuando pasamos todas las validaciones declaramos que si el estudiante esta presente, entonces tenemos una nueva variable que tendra como valor 1
                asistencia = 1 
            else: # De lo contrario si el usuario esta ausente la variable sera 0, esto nos sirve despues para sumar estos valores y ver cuantas asistencias tenemos en cada lista
                asistencia = 0
            match i: # Tenemos un bloque match - case donde decimos que cuando la variable i que es en el primer bucle for (secciones) pasara por los valores 1 - 2 y 3 para cada seccion 
                case 1: # Cuando i sea 1 entonces agregaremos a la lista asistencia_sec1 el resultado de la variable asistencia 
                    asistencia_sec1.append(asistencia) # Usamos la funcion append() y le pasamos como parametro la variable asistencia 
                case 2: # Misma logica que el case 1
                    asistencia_sec2.append(asistencia)
                case 3: # Misma logica que el case 2
                    asistencia_sec3.append(asistencia)

# Declaramos 3 nuevas variables para sacar el total de asistencias por cada lista, esto se hace porque anteriormente solo teniamos una secuencia de unos y ceros, ahora debemos sumar todo eso
# Esto lo hacemos con la funcion sum() y le pasamos como parametro la lista asistencia_sec1, 2 y 3 
total_sec1 = sum(asistencia_sec1) 
total_sec2 = sum(asistencia_sec2)
total_sec3 = sum(asistencia_sec3)

# Ahora que tenemos el total por cada seccion, creamos una variable nueva para almacenar el total general, donde solo sumamos el total de cada seccion 
total = total_sec1 + total_sec2 + total_sec3

# Fase final donde imprimimos los resultados. Si se deseara podria importarse el operative_system para hacer una limpieza de consola, pero eso es a gusto propio. 
print(f'Seccion 1: {total_sec1} asistencias')
print(f'Seccion 2: {total_sec2} asistencias')
print(f'Seccion 3: {total_sec3} asistencias')
print(f'Total general: {total} asistencias')
           
            
