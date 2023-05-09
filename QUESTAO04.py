print("loja de carros-formação do preço final do veiculo")
cusfabrica = int(input("PREÇO DE FABRICA:"))
porevendedor = cusfabrica * (25/100)
poimposto = cusfabrica * (45/100)
total = cusfabrica+porevendedor + poimposto
print(" PREÇO FINAL DO CARRO:", total )
