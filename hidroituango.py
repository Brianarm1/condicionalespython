#Condiciones multiples

sensorNivelDeAgua = int(input("Digite el nivel de agua de la represa: "))

print(f"El nivel de agua es: {sensorNivelDeAgua}")


if sensorNivelDeAgua > 0 and sensorNivelDeAgua <= 150:
    print("Muy poca agua las puertas estan cerradas")

elif sensorNivelDeAgua > 150 and sensorNivelDeAgua <=400:
    print("Operando normalmente")  

elif sensorNivelDeAgua > 400 and sensorNivelDeAgua <=420:
    print("Mucho cuidado revise el nivel de agua")
    
elif sensorNivelDeAgua > 420:
    print("Este parche se calento corre.....")  

else:
    print("Revise el sensor, medida no valida")

   

