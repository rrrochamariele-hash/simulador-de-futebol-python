import random

print("⚽ BEM-VINDO AO SIMULADOR DE FUTEBOL INTERATIVO ⚽\n")

# Lista inicial de times disponíveis
times = ['Bahia', 'Corinthians', 'Santos', 'Flamengo', 'Palmeiras', 'São Paulo']

# Dicionário para armazenar os pontos de cada time
tabela = {time: 0 for time in times}

def mostrar_tabela():
    print("\n--- 📊 TABELA DE CLASSIFICAÇÃO ATUALIZADA ---")
    tabela_ordenada = sorted(tabela.items(), key=lambda x: x[1], reverse=True)
    for posicao, (time, pontos) in enumerate(tabela_ordenada, start=1):
        print(f"{posicao}º {time}: {pontos} pts")
    print("-" * 42)

# Loop principal do menu interativo
while True:
    print("\nO que você deseja fazer?")
    print("1 - Ver times disponíveis")
    print("2 - Simular uma partida personalizada")
    print("3 - Ver tabela de classificação")
    print("4 - Sair do simulador")
    
    opcao = input("\nEscolha uma opção (1-4): ").strip()
    
    if opcao == '1':
        print("\nTimes disponíveis no campeonato:")
        for i, t in enumerate(times, 1):
            print(f"[{i}] {t}")
            
    elif opcao == '2':
        print("\n--- ESCOLHA OS CONFRONTO ---")
        for i, t in enumerate(times, 1):
            print(f"[{i}] {t}")
            
        try:
            # Pede para o usuário digitar o número dos times
            escolha1 = int(input("Digite o número do 1º time (Mandante): ")) - 1
            escolha2 = int(input("Digite o número do 2º time (Visitante): ")) - 1
            
            if 0 <= escolha1 < len(times) and 0 <= escolha2 < len(times):
                time1 = times[escolha1]
                time2 = times[escolha2]
                
                if time1 == time2:
                    print("⚠️ Um time não pode jogar contra si mesmo! Escolha times diferentes.")
                    continue
                
                # Simula a partida
                gols1 = random.randint(0, 4)
                gols2 = random.randint(0, 4)
                
                print(f"\n⚡ APITO FINAL: {time1} {gols1} x {gols2} {time2} ⚡")
                
                # Atualiza os pontos
                if gols1 > gols2:
                    tabela[time1] += 3
                    print(f"Vitória do {time1}!")
                elif gols2 > gols1:
                    tabela[time2] += 3
                    print(f"Vitória do {time2}!")
                else:
                    tabela[time1] += 1
                    tabela[time2] += 1
                    print("Empate!")
            else:
                print("❌ Número inválido! Escolha um número da lista.")
        except ValueError:
            print("❌ Por favor, digite apenas números inteiros válidos.")
            
    elif opcao == '3':
        mostrar_tabela()
        
    elif opcao == '4':
        print("\nEncerrando o simulador. Obrigado por jogar! ⚽👋")
        break
    else:
        print("❌ Opção inválida! Escolha um número entre 1 e 4.")
