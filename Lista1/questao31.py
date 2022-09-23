h = float(input("Preço da hora trabalhada:"))
hm = float(input("Horas trabalhadas no mês:"))
salario_bruto = h * hm   
ir_disconto = 0
ir_salario = (salario_bruto * ir_disconto)

if salario_bruto <= 900:
    ir_disconto = 0

elif salario_bruto <= 1500:
    ir_disconto = 0.05

elif salario_bruto <= 2500:
    ir_disconto = 0.1

elif salario_bruto > 900:
    ir_salario = (salario_bruto * ir_disconto)

if salario_bruto <= 900:
    ir_salario = 0

inss = 0
inss_salario = (salario_bruto * inss)

fgts = 1.11
fgts_salario = (salario_bruto * fgts) - salario_bruto

total = inss_salario + ir_salario
liquido = salario_bruto - total

print("Salario bruto({:.2f} * {:.2f}): {:.2f}\n IR({:.2f}): {:.2f}\n INSS({:.2f}:{:.2f}\nFGTS({:.2f}):{:.2f}\nDisconto total: {:.2f}\n Salario liquido: {:.2f}".format(h, hm, salario_bruto, ir_disconto, ir_salario,inss, inss_salario,fgts,fgts_salario,total,liquido))