bateria=int(input("digite o nivel de bateria (de 0 a 100%): "))
temperatura=float(input("digite a temperatura do ambiente em graus C°: "))
umidade=int(input("digite a umidade do solo (de 0 a 100): "))
modo=input("digite o modo de operação (plantio, colheita ou irrigação): ")

if bateria<20:
    print("bateria muito baixa, retorne para a base.")

if 20<=bateria<50:
        print("Atenção: bateria em nível moderado.") 

if bateria>=50:
      print("bateria suficiente para operação.")


if temperatura>40:
      print("Temperatura crítica! Operação suspensa.")

if temperatura<5:
      print("Frio extremo! Modo de economia ativado.")


if umidade<30:
      print("Solo muito seco. Recomendado iniciar irrigação.")

if umidade>80:
      print("Solo encharcado! Suspenda irrigação imediatamente.")


if bateria>=50:
      
      if 10<temperatura<35:
            
            if 30<umidade<80:
                print("Robõ autorizado a iniciar operação.")

                if modo=="plantio":
                      print("iniciando modo plantio.")

                if  modo=="colheita":
                      print("iniciando modo colheita.")

                if  modo=="irrigação":
                      print("iniciando modo irrigação.")

            if 30>umidade>80:
                  print("operação negada! Verifique as condições do ambiente.")

      if  10>temperatura>35:
            print("operação negada! Verifique as condições do ambiente.")

if bateria<50:
      print("operação negada! Verifique as condições do ambiente.")            