#4) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Digite as notas bimestrais para obter a média:")    
a, b, c ,d = float(input("1 bimestre:")), float(input("2 bimestre:")),float(input("3 bimestre:")), float(input("4 bimestre:"))
notas = (a + b + c + d) / 4
print("A média de notas é {:.1f}".format(notas))
