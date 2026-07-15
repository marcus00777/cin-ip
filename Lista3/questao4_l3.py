print("Bem vindos, exploradores! Começaremos à Missão Lazarus!")

# Fase 1
planetas_candidatos = input()
planetas = planetas_candidatos.split(", ")
print("Planetas armazenados. Fim da Missão Lazarus.")

print("Hora de escolher os melhores planetas para habitarmos!")

total_inicial = len(planetas)
#missão 1
pos = 0

for i in range(len(planetas)):
    dados_pla = planetas[i].split(" - ")
    nome = dados_pla[0]
    nivel = int(dados_pla[1])
    sonda = dados_pla[2]

    if sonda != "falha" and nivel >= 6:
        planetas[pos] = [nome, nivel, sonda]
        pos += 1

planetas[:] = planetas[:pos]
num_planetas_removidos = total_inicial - len(planetas)
#missão 2
trocou = True
while trocou:
    trocou = False

    for i in range(len(planetas) - 1):
        atual = planetas[i]
        proximo = planetas[i + 1]

        nivel_atual = atual[1]
        nivel_proximo = proximo[1]

        nome_atual = atual[0]
        nome_proximo = proximo[0]

        trocar = False

        if nivel_atual < nivel_proximo:
            trocar = True
        elif nivel_atual == nivel_proximo:
            if nome_atual > nome_proximo:
                trocar = True

        if trocar:
            planetas[i], planetas[i + 1] = planetas[i + 1], planetas[i]
            trocou = True

if len(planetas) >= 1:
    nomes = []
    for p in planetas:
        nomes.append(p[0])
    print("Planetas habitáveis encontrados: " + ", ".join(nomes) + ".")
else:
    print("Planetas habitáveis encontrados: nenhum.")

print(f"Quantidade de planetas desconsiderados: {num_planetas_removidos}.")