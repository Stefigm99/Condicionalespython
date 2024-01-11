#condiciones multiples

sensorNivelAgua=int(input("Digite el nivel de agua de la represa: "))

print(f"El nivel de agua: {sensorNivelAgua}")

if sensorNivelAgua>0 and sensorNivelAgua<=150:
    print("Muy poca agua las puertas estan cerradas")
elif sensorNivelAgua>150 and sensorNivelAgua<=400:
    print("Operando normalmente")
elif sensorNivelAgua>400 and sensorNivelAgua<=420:
    print("Precaucion, mucho cuidado. Rebice el nivel de agua")
elif sensorNivelAgua>420:
    print("Corre loca......")
else:
    print("Revise el sensor, medida no valida")