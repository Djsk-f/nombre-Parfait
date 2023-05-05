
# NOMBRE PARFAIT

def nombre_parfait(nombre):
       liste_nombre = []
       for number in range(1, int(nombre)):
        list = []
        sol = 0
        for nombre_div in range(1,int(round(number/2))):
            if number%nombre_div == 0:
             list.append(nombre_div)

        for n  in list:
         sol = sol + n
         if sol == number:
          liste_nombre.append(sol)
       print(liste_nombre)

number = int(input("entrer un nombre \t"))
nombre_parfait(number)
