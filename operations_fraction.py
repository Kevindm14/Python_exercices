from datetime import datetime

file = open("[kevin_diazmerino]01.txt", "r")
date = datetime.now()
date_now = date.strftime("%Y-%B-%A-%I:%M:%S%P")

try:
    array = list(file)

    name = input("¿Cual es tu nombre? => ")
    last_name = input("¿Cual es tu apellido? => ")

    file_save = open(f'[{name}{last_name}]{date_now}.txt', "w")

    for operation in range(len(array)):
        # Separate for string
        opt = array[operation].rstrip()
        op_join = ",".join(opt)
        op_split = op_join.split(",")

        # Delete empty position
        array2 = []
        for i in op_split:
            if (i != ' '):
                array2.append(i)

        # N(a/b) op M(x/y)
        n = int(array2[0])
        a = int(array2[2])
        b = int(array2[4])
        op = array2[6]
        m = int(array2[7])
        x = int(array2[9])
        y = int(array2[11])

        # Convertir fraction impropia a mixta propia
        if (a > b):
            n = (a // b) + n
            a = a % b
        
        if (x > y):
            m = (x // y) + m
            x = x % y

        # Operaciones
        fraction1 = n * b + a
        fraction2 = m * y + x

        if (op == "+"):
            denominador = b * y
            op1 = fraction1 * y
            op2 = b * fraction2
            numerador = op1 + op2
        
        elif (op == "-"):
            denominador = b * y
            op1 = fraction1 * y
            op2 = b * fraction2
            numerador = op1 - op2
        
        elif (op == "*"):
            numerador = fraction1 * fraction2
            denominador = b * y

        elif (op == "/"):
            numerador = fraction1 * y
            denominador = b * fraction2
        
        # Convert fraction to number mixt
        division = numerador // denominador
        residuo = numerador % denominador

        file_save.write(f'{n}({a}/{b}) {op} {m}({x}/{y}) = {division}({residuo}/{denominador}) \n')

finally:    
    file.close()
    file_save.close()

    print("----------------")
    print("Archivo guardado")
    print("----------------")       