dias_validos = ['1', '2', '3', '4', '5', '6', '7']
dia_semana = input("Digite o seu dia da semana com base em numero (1-7)\n")

while dia_semana not in dias_validos:
    dia_semana = input("Digite um dia da semana válido (1-7)\n")

if dia_semana == '1' :
    print("segunda")
if dia_semana == '2':
    print("terça")
if dia_semana == '3':
    print("quarta")
if dia_semana == '4':
    print("quinta")
if dia_semana == '5':
    print("sexta")
if dia_semana == '6':
    print("sabado")
if dia_semana == '7':
    print("domingo")