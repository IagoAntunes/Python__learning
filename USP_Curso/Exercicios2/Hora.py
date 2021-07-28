segundos = int(input("Numero de Segundos:"))

dia = segundos//86400
segundos = segundos % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(dia,"dias,",horas," horas,",minutos," minutos e ",segundos," segundos.")
