segundosParaConverter = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundosParaConverter)
minutos = segundos // 60 
horas = minutos // 60
dias = horas // 24
print(dias, "dias,", horas % 24, "horas,", minutos % 60, "minutos e", segundos % 60, "segundos.")