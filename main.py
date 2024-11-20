import os
import matplotlib.pyplot as plt
import time

def formatacao(variavel):
    return variavel.replace("/", "")


def verificarData(data):
    try:
        time.strptime(data, "%d/%m/%Y")
        x = 'correto'
        return (x)

    except ValueError:
        print("Data inválida! Insira uma data no formato DD/MM/YYYY.")
        x = 'incorreto'
        return (x)


def limparTela():
    input("Digite qualquer tecla para voltar ao menu: ")
    os.system("cls")


def textoInicio():
    print("""
██████╗ ███████╗███╗   ███╗    ██╗   ██╗██╗███╗   ██╗██████╗  ██████╗     
██╔══██╗██╔════╝████╗ ████║    ██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗    
██████╔╝█████╗  ██╔████╔██║    ██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║    
██╔══██╗██╔══╝  ██║╚██╔╝██║    ╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║    
██████╔╝███████╗██║ ╚═╝ ██║     ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝    
╚═════╝ ╚══════╝╚═╝     ╚═╝      ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝""")


def criar(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas,num):

    if os.path.exists(f"Treino{num}{dataFormatada}.txt"):
        print("Já existe um arquivo para essa data.")

        data = input("Digite a data do seu treino (DD/MM/YYYY): ")
        validacao = verificarData(data)
        num=int(input("Digite outro número para o treino: "))
        dataFormatada = formatacao(data)

    try:
        with open(f"Treino{num}{dataFormatada}.txt", "w", encoding="utf-8") as file:
            file.write(f"""Data: {data}
Distancia percorrida: {distanciaPercorrida}km
Tempo: {tempo}min
Localização: {localizacao}
Condições climaticas: {condicoesClimaticas}
""")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")


def criarCOMP(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas, nomeCOMP,num):

    if os.path.exists(f"Competição{num}{dataFormatada}.txt"):
        print("Já existe um arquivo para essa data.")

        data = input("Digite a data do seu treino (DD/MM/YYYY): ")
        validacao = verificarData(data)
        num=int(input("Digite outro número para a competição: "))
        dataFormatada = formatacao(data)

    try:
        with open(f"Competição{num}{dataFormatada}.txt", "w", encoding="utf-8") as file:
            file.write(f"""Data: {data}
Distancia percorrida: {distanciaPercorrida}km
Tempo: {tempo}min
Localização: {localizacao}
Condições climaticas: {condicoesClimaticas}
Nome da Competição: {nomeCOMP}
""")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")


def selecionartudo(comeco, fim, caminho):
    arquivosTreinos = []
    for arquivo in os.listdir(caminho):
        if arquivo.startswith(comeco) and arquivo.endswith(fim):
            arquivosTreinos.append(arquivo)
    return arquivosTreinos


def leitura(arquivosTreinos):
    if not arquivosTreinos:
        print("Nenhum arquivo encontrado.")
        return
    for arquivo in arquivosTreinos:
        try:
            with open(arquivo, "r", encoding="utf-8") as file:
                print(f"\nArquivo: {arquivo}")
                print(file.read())
                print("-" * 30)
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo}: {e}")


def leituraFiltrada(filtro, arquivosTreinos, linha, medida): 
    for arquivo in arquivosTreinos:
        with open(arquivo, "r", encoding="utf-8") as file:
            conteudo = file.read()
            if linha in conteudo:
                try:
                    filtroStr = conteudo[conteudo.index(linha):]
                    filtroStr = filtroStr.split(":")[1].strip()
                    filtroStr = filtroStr.split()[0]
                    valorFiltrado = float(filtroStr.replace(medida, "").strip())
                    
                    if valorFiltrado >= filtro:
                        print(f"\nArquivo: {arquivo}") 
                        print(conteudo)
                        print("-" * 30)
                        file.close()  
                except ValueError:
                    print("Erro em processar o valor do arquivo")    


def atualizar(conteudo, formatacao, valorPraAtualizar, medida): 
    for i in range(len(conteudo)):
        if formatacao in conteudo[i]:
            conteudo[i] = f"{formatacao}{valorPraAtualizar}{medida}\n"
    return conteudo


def atualizarArquivo(nomeArquivo, conteudo):
    try:
        with open(nomeArquivo, "w", encoding="utf-8") as file:
            file.writelines(conteudo)
    except Exception as e:
        print(f"Erro ao atualizar o arquivo {nomeArquivo}: {e}")


def lerArquivo(nomeArquivo):
    with open(nomeArquivo, "r", encoding="UTF-8") as file:
        conteudo = file.readlines()
    return conteudo


def deletar(dataNomeArquivo,num):
    while True:
        try:
            op = int(input('Essa data se refere a um [1]treino ou [2]competição? '))
            
            match op:

                case 1:

                    nomeArquivo = f"Treino{num}{dataNomeArquivo}.txt"
                    if os.path.exists(nomeArquivo):
                        try:
                            os.remove(nomeArquivo)
                            print("Arquivo excluído com sucesso!")

                            limparTela()
                            break

                        except Exception as e:
                            print(f"Erro ao excluir o arquivo {nomeArquivo}: {e}")
                    else:
                        print("Arquivo não encontrado!")
                
                case 2:

                    nomeArquivo = f"Competição{num}{dataNomeArquivo}.txt"
                    if os.path.exists(nomeArquivo):
                        try:
                            os.remove(nomeArquivo)
                            print("Arquivo excluído com sucesso!")

                            limparTela()
                            break

                        except Exception as e:
                            print(f"Erro ao excluir o arquivo {nomeArquivo}: {e}")
                    else:
                        print("Arquivo não encontrado!")
                
                case _ :
                    
                    print('Digite um número inteiro, sendo ele 1 ou 2.')

        except ValueError:
            print('Erro! Digite um valor inteiro.')
            continue


def cadastroMetas(data,meta):
    with open(f'Metas.txt','a') as file:
          file.write(f"Data da meta:{data} | Meta:{meta}\n")
          file.close()


def lerMetas():
    try:
        with open(f"Metas.txt","r") as file:
            conteudo=file.read()
            
            print(conteudo)

    except FileNotFoundError:
        print('Esse arquivo não existe')  


def concluirmeta(num):
    novonum = num - 1
    try:
        with open("Metas.txt", "r") as file:
            linhas = file.readlines()

        quant = len(linhas)

        if novonum < 0 or novonum >= quant:
            print("Número inválido. Por favor, escolha um número dentro do intervalo.")
            return

        with open("Metaconcluida.txt", "a") as concluida:
            concluida.write(linhas[novonum])

        with open("Metas.txt", "w") as metas:
            for i, linha in enumerate(linhas):
                if i != novonum:
                    metas.write(linha)

        print(f"Meta {num} marcada como concluída e removida das pendentes.")

    except FileNotFoundError:
        print('O arquivo "Metas.txt" não existe. Verifique se ele foi criado.')


def lermetasconcluidas():
    try:
        with open(f"Metaconcluida.txt","r") as file:
            conteudo=file.read()
            print(conteudo)
    except FileNotFoundError:
        print('Esse arquivo não existe')  

def gerarRelatorioVisual(arquivosTreinos, arquivosCompeticoes):
    if not arquivosTreinos and not arquivosCompeticoes:
        print("Nenhum treino ou competição encontrado para gerar o relatório.")
        return

    datasTreinos = []
    distanciasTreinos = []
    temposTreinos = []

    datasCompeticoes = []
    distanciasCompeticoes = []
    temposCompeticoes = []

    for arquivo in arquivosTreinos:
        try:
            with open(arquivo, "r", encoding="utf-8") as file:
                conteudo = file.read()
                data = conteudo.split("\n")[0].split(":")[1].strip()
                distancia = float(conteudo.split("\n")[1].split(":")[1].strip().replace("km", ""))
                tempo = int(conteudo.split("\n")[2].split(":")[1].strip().replace("min", ""))

                datasTreinos.append(data)
                distanciasTreinos.append(distancia)
                temposTreinos.append(tempo)
        except Exception as e:
            print(f"Erro ao processar o arquivo de treino {arquivo}: {e}")

    for arquivo in arquivosCompeticoes:
        try:
            with open(arquivo, "r", encoding="utf-8") as file:
                conteudo = file.read()
                data = conteudo.split("\n")[0].split(":")[1].strip()
                distancia = float(conteudo.split("\n")[1].split(":")[1].strip().replace("km", ""))
                tempo = int(conteudo.split("\n")[2].split(":")[1].strip().replace("min", ""))

                datasCompeticoes.append(data)
                distanciasCompeticoes.append(distancia)
                temposCompeticoes.append(tempo)
        except Exception as e:
            print(f"Erro ao processar o arquivo de competição {arquivo}: {e}")

    if datasTreinos and distanciasTreinos and temposTreinos:
        plt.figure(figsize=(10, 5))
        plt.plot(datasTreinos, distanciasTreinos, marker='o', label="Distância (km)")
        plt.title("Evolução de Distâncias - Treinos")
        plt.xlabel("Datas")
        plt.ylabel("Distância (km)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10, 5))
        plt.bar(datasTreinos, temposTreinos, color='blue', label="Tempo (min)")
        plt.title("Tempo em Treinos")
        plt.xlabel("Datas")
        plt.ylabel("Tempo (min)")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.legend()
        plt.tight_layout()
        plt.show()

    if datasCompeticoes and distanciasCompeticoes and temposCompeticoes:
        plt.figure(figsize=(10, 5))
        plt.plot(datasCompeticoes, distanciasCompeticoes, marker='o', color='red', label="Distância (km)")
        plt.title("Evolução de Distâncias - Competições")
        plt.xlabel("Datas")
        plt.ylabel("Distância (km)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10, 5))
        plt.bar(datasCompeticoes, temposCompeticoes, color='orange', label="Tempo (min)")
        plt.title("Tempo em Competições")
        plt.xlabel("Datas")
        plt.ylabel("Tempo (min)")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.legend()
        plt.tight_layout()
        plt.show()


treinos = {"Data":[], "DistanciaPercorrida":[], "Tempo":[], "Localizacao":[], "CondicoesClimaticas":[]}

os.system("cls")
while True:  
    try:
        textoInicio()
        print(f"""
{("="*70)}        
Digite [1] para adicionar um registro de treino/competição
Digite [2] para visualizar um registro de treino/competição
Digite [3] para atualizar um registro de treino /competição
Digite [4] para excluir um registro de treino e competição
Digite [5] para registrar/visualizar suas metas;
Digite [6] para ver sugestões de treinos aleatorios
Digite [7] para ver a evolução dos treinos
Digite [0] para encerrar o programa
{("="*70)}""")
    
        opcao = int(input("Digite sua opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break
        
            case 1:
                op = int(input("Você deseja adicionar um [1]treino ou [2]competição: "))
                
                match op:

                    case 1:              
                        try:     
                            while True: 
                                
                                data = input("Digite a data do seu treino (DD/MM/YYYY): ")
                                validacao = verificarData(data)
                                num=int(input("Digite o número do treino: "))
                                
                                dataFormatada = formatacao(data)
                                if os.path.exists(f"Treino{num}{dataFormatada}.txt"):
                                    print("Já existe um arquivo com essas informações,redigite os dados!")
                                    continue

                                if validacao == 'correto':
                                    break
                                if validacao == 'incorreto':
                                    continue

                            treinos["Data"] = data
                            distanciaPercorrida = float(input("Digite a distancia percorrida (KM): "))
                            treinos["DistanciaPercorrida"] = distanciaPercorrida
                            tempo = int(input("Digite o tempo em minutos que você levou para concluir esse treino: "))
                            treinos["Tempo"] = tempo
                            localizacao = input("Digite a localizacao do seu treino: ")
                            treinos["Localizacao"] = localizacao
                            condicoesClimaticas = input("Digite as condições climaticas na hora do treino: ")
                            treinos["CondicoesClimaticas"] = condicoesClimaticas
                            
                            criar(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas,num) 

                        except ValueError:
                            print("Você digitou um número errado, por favor digite novamente!")

                        limparTela()
            
                    case 2:
                        
                        try: 
                            
                            while True: 
                                
                                data = input("Digite a data da sua competição (DD/MM/YYYY): ")
                                validacao = verificarData(data)
                                num=int(input("Digite o número da competição: "))

                                dataFormatada = formatacao(data)
                                if os.path.exists(f"Treino{num}{dataFormatada}.txt"):
                                    print("Já existe um arquivo com essas informações,redigite os dados!")
                                    continue

                                if validacao == 'correto':
                                    break
                                if validacao == 'incorreto':
                                    continue

                            treinos["Data"] = data
                            distanciaPercorrida = float(input("Digite a distancia percorrida (KM): "))
                            treinos["DistanciaPercorrida"] = distanciaPercorrida
                            tempo = int(input("Digite o tempo em minutos que você levou para concluir essa competição: "))
                            treinos["Tempo"] = tempo
                            localizacao = input("Digite a localizacao da sua competição: ")
                            treinos["Localizacao"] = localizacao
                            condicoesClimaticas = input("Digite as condições climaticas na hora do treino/competição: ")
                            treinos["CondicoesClimaticas"] = condicoesClimaticas
                            nomeCOMP = input('Digite o nome da competição: ')
                            treinos["nomeCOMP"] = nomeCOMP
                            
                            criarCOMP(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas, nomeCOMP,num) 

                        except ValueError:
                            print("Você digitou um número errado, por favor digite novamente!")

                        limparTela()

            case 2:
                op = int(input("Você deseja visualizar [1]treinos ou [2]competições: "))
                os.system("cls")

                match op:
                    
                    case 1:

                        while True:
                            filtro = input("Você deseja filtrar na hora da visualização de seus treinos (Sim/Nao)? ").lower()

                            arquivosTreinos = selecionartudo("Treino", ".txt", ".")

                            if filtro == "nao" or filtro == "não":
                                leitura(arquivosTreinos)
                                limparTela()
                                break

                            elif filtro == "sim":
                                criterio = int(input("Você deseja filtrar por distancia ou tempo? Digite 1 ou 2, respectivamente: "))
                                
                                if criterio == 1:
                                    distanciaFiltro = float(input("Digite a distancia mínima para filtrar (em km): "))
                                    leituraFiltrada(distanciaFiltro, arquivosTreinos, "Distancia percorrida:", "km")

                                elif criterio == 2:
                                    tempoFiltro = int(input("Digite a o tempo mínimo para filtrar (em min): "))

                                    leituraFiltrada(tempoFiltro, arquivosTreinos, "Tempo:", "min")

                                else:
                                    print("Opção invalida, por favor digite novamente!!")
                                break
                            
                            else: 
                                print("Opção invalida, por favor, digite-a corretamente!")
                            
                
                    case 2:

                        while True:
                                filtro = input("Você deseja filtrar na hora da visualização das suas competições (Sim/Nao)? ").lower()

                                arquivosTreinos = selecionartudo("Competição", ".txt", ".")

                                if filtro == "nao" or filtro == "não":
                                    leitura(arquivosTreinos)
                                    limparTela()
                                    break

                                elif filtro == "sim":
                                    criterio = int(input("Você deseja filtrar por distancia ou tempo? Digite 1 ou 2, respectivamente: "))
                                    
                                    if criterio == 1:
                                        distanciaFiltro = float(input("Digite a distancia mínima para filtrar (em km): "))
                                        leituraFiltrada(distanciaFiltro, arquivosTreinos, "Distancia percorrida:", "km")

                                    elif criterio == 2:
                                        tempoFiltro = int(input("Digite a o tempo mínimo para filtrar (em min): "))

                                        leituraFiltrada(tempoFiltro, arquivosTreinos, "Tempo:", "min")

                                    else:
                                        print("Opção invalida, por favor digite novamente!!")
                                    break

                                else: 
                                    print("Opção invalida, por favor, digite-a corretamente!")
                    
                limparTela()
                                
            case 3:
                op = int(input("Você deseja alterar um [1]treino ou [2]competição:"))
                match op:
                    case 1:
                        os.system("cls")
                        while True:        
                            dataArquivo = input("Digite a data do treino que você deseja alterar: ")
                            validacao = verificarData(dataArquivo)
                            num=int(input("Digite o número do treino: "))

                            if validacao == 'correto':
                                break

                            if validacao == 'incorreto':
                                continue
                        
                        dataArquivo = formatacao(dataArquivo)
                        nomeArquivo = f"Treino{num}{dataArquivo}.txt"
                        if os.path.isfile(nomeArquivo):

                            print(f"""
{("="*70)}
Digite [1] para alterar a data
Digite [2] para alterar a distancia percorrida
Digite [3] para alterar o tempo
Digite [4] para alterar a localização
Digite [5] para alterar as condições climaticas
{("="*70)}""")
                            opcaoAtualizar = int(input("Digite a opção que você deseja alterar: "))

                            conteudo = lerArquivo(nomeArquivo)

                            match opcaoAtualizar:
                                case 1:
                                    while True:
                                        novaData = input("Digite a nova data: ")
                                        validacao = verificarData(novaData)
                                        
                                        if validacao == 'correto':
                                            break

                                        if validacao == 'incorreto':
                                            continue    
                                    
                                    conteudo = atualizar(conteudo, "Data: ", novaData, "")

                                case 2: 
                                    novaDistanciaPercorrida = float(input("Digite a nova distancia percorrida: "))
                                    
                                    conteudo = atualizar(conteudo, "Distancia percorrida: ", novaDistanciaPercorrida, "km")

                                case 3: 
                                    novoTempo = int(input("Digite o novo tempo: "))

                                    conteudo = atualizar(conteudo, "Tempo: ", novoTempo, "min")
                                
                                case 4:
                                    novaLocalizacao = input("Digite a nova localização: ")
                                    
                                    conteudo = atualizar(conteudo, "Localização: ", novaLocalizacao, "")
                                
                                case 5:
                                    novaCondicaoClimatica = input("Digite uma nova condição climatica: ")
                                    
                                    conteudo = atualizar(conteudo, "Condições climaticas: ", novaCondicaoClimatica, "")
                            
                            atualizarArquivo(nomeArquivo, conteudo)

                            if opcaoAtualizar == 1:
                                os.rename(nomeArquivo, f"Treino{formatacao(novaData)}.txt")

                            print("Alteração realizada com sucesso!")
                        
                        else:
                            print("Arquivo não localizado, por favor tente novamente")
                    
                        limparTela()
                    
                    case 2:
                        os.system("cls")
                        while True: 
                                dataArquivo = input("Digite a data da competição que você deseja alterar: ")
                                validacao = verificarData(dataArquivo)
                                num=int(input("Digite o número da competição: "))

                                if validacao == 'correto':
                                    break

                                if validacao == 'incorreto':
                                    continue

                        dataArquivo = formatacao(dataArquivo)
                        nomeArquivo = f"Competição{num}{dataArquivo}.txt"
                        if os.path.isfile(nomeArquivo):

                            print(f"""
{("="*70)}
Digite [1] para alterar a data
Digite [2] para alterar a distancia percorrida
Digite [3] para alterar o tempo
Digite [4] para alterar a localização
Digite [5] para alterar as condições climaticas
Digite [6] para alterar o nome da competição
{("="*70)}""")
                            opcaoAtualizar = int(input("Digite a opção que você deseja alterar: "))

                            conteudo = lerArquivo(nomeArquivo)

                            match opcaoAtualizar:
                                case 1:
                                    while True:
                                        novaData = input("Digite a nova data: ")
                                        validacao = verificarData(novaData)
                                        
                                        if validacao == 'correto':
                                            break

                                        if validacao == 'incorreto':
                                            continue    
                                    
                                    conteudo = atualizar(conteudo, "Data: ", novaData, "")

                                case 2: 
                                    novaDistanciaPercorrida = float(input("Digite a nova distancia percorrida: "))
                                    
                                    conteudo = atualizar(conteudo, "Distancia percorrida: ", novaDistanciaPercorrida, "km")

                                case 3: 
                                    novoTempo = int(input("Digite o novo tempo: "))

                                    conteudo = atualizar(conteudo, "Tempo: ", novoTempo, "min")
                                
                                case 4:
                                    novaLocalizacao = input("Digite a nova localização: ")
                                    
                                    conteudo = atualizar(conteudo, "Localização: ", novaLocalizacao, "")
                                
                                case 5:
                                    novaCondicaoClimatica = input("Digite uma nova condição climatica: ")
                                    
                                    conteudo = atualizar(conteudo, "Condições climaticas: ", novaCondicaoClimatica, "")
                                
                                case 6:
                                    novoNomeCOMP = input("Digite o nome correto da competição: ")

                                    conteudo = atualizar(conteudo, "Nome da Competição: ", novoNomeCOMP, "")

                            
                            atualizarArquivo(nomeArquivo, conteudo)

                            if opcaoAtualizar == 1:
                                os.rename(nomeArquivo, f"Competição{formatacao(novaData)}.txt")

                            print("Alteração realizada com sucesso!")
                        
                        else:
                            print("Arquivo não localizado, por favor tente novamente")
                    
                        limparTela()

            case 4:
                os.system("cls")
                while True:
                                
                    dataNomeArquivo = input("Digite a data da corrida que você deseja excluir: ")
                    validacao = verificarData(dataNomeArquivo)
                    
                    if validacao == 'correto':
                        break

                    if validacao == 'incorreto':
                        continue    
                
                dataNomeArquivo = formatacao(dataNomeArquivo)
                
                num=int(input("Digite o número da corrida que você deseja excluir: "))

                deletar(dataNomeArquivo,num)
                
                limparTela()

            case 5:
                os.system("cls")
                while True:
                    opção=input(f"""
{("="*70)}
Digite [1] para criar uma meta
Digite [2] para ler as metas atuais
Digite [3] para marcar uma meta como conluida
Digite [4] para ver as metas concluidas
Digite [5] para voltar para o menu principal
{("="*70)}\nDigite o que deseja fazer:""")

                    if(opção=='1'):
                        os.system("cls")    
                        data=str(input("Digite a data em que a meta foi criada:"))
                        while True:  
                            data=str(input("Digite a data em que a meta foi criada:"))
                            validacao = verificarData(data)

                            if validacao == 'correto':
                                break

                            if validacao == 'incorreto':
                                continue  

                        meta=str(input("Digite sua meta:"))
                        cadastroMetas(data,meta)
                    
                    elif(opção=='2'):
                        os.system("cls")
                        lerMetas()
                    
                    elif(opção=='3'):
                        os.system("cls")
                        lerMetas()
                        num=int(input("Digite o numero da meta que deseja marcar como concluida:"))
                        concluirmeta(num)
                    
                    elif(opção=='4'):
                        os.system("cls")
                        lermetasconcluidas()
                    
                    elif(opção=='5'):
                        os.system("cls")
                        break
                    
                    else:
                        print("digito errado")
            
            case 6:
                os.system("cls")

                listaAleatorios =  selecionartudo("treinoAleatorio", ".txt", ".")
                
                for treinosAleatorios in listaAleatorios:
                    caminhoArquivo = treinosAleatorios 
                    with open(caminhoArquivo, "r", encoding="UTF-8") as file:
                        print(f"\nArquivo: {treinosAleatorios}")
                        print(file.read())
                        print("-" * 30)
                        file.close() 
                
                while True:
                    print("Você fez algum dos treinos aleatorios?")
                    fazer = int(input("Se sim, digite o número de 1 a 20 para marcar como feito, se nao, digite 0: "))
                    
                    if 1 <= fazer <= 20:
                        treinoFeito = "treinoAleatorio" + str(fazer) + ".txt"
                        arquivoCaminho = treinoFeito
                        
                        conteudo = lerArquivo(arquivoCaminho)

                        atualizar(conteudo, "Status: ", "feito✔️", "")

                        atualizarArquivo(arquivoCaminho, conteudo)
                        
                        print(f"{treinoFeito} foi atualizado como feito!!")
                        break

                    elif fazer == 0:
                        break
                    else:
                        print("Opção incorreta, por favor digite novamente!")
                
                limparTela()
            
            case 7:
                os.system("cls")
                arquivosTreinos = selecionartudo("Treino", ".txt", ".")
                arquivosCompeticao = selecionartudo("Competição", ".txt", ".")
                gerarRelatorioVisual(arquivosTreinos, arquivosCompeticao)
                limparTela()

            case _:
                print("Opção invalido, por favor digite novamente!")
    
    except ValueError:
        os.system('cls')
        print("Opção Inválida! Informe um valor inteiro, de 0 a 6.")
        limparTela()