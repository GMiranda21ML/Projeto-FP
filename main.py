import os
import matplotlib.pyplot as plt

def formatacao(variavel):
    return variavel.replace("/", "")


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


def create(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas):
    try:
        with open(f"Treino{dataFormatada}.txt", "w", encoding="utf-8") as file:
            file.write(f"""Data: {data}
Distancia percorrida: {distanciaPercorrida}km
Tempo: {tempo}min
Localização: {localizacao}
Condições climaticas: {condicoesClimaticas}
""")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")

def createCOMP(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas, nomeCOMP):
    try:
        with open(f"Competição{dataFormatada}.txt", "w", encoding="utf-8") as file:
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


def read(arquivosTreinos):
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


def readFiltrado(filtro, arquivosTreinos, linha, medida): 
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


def update(conteudo, formatacao, valorProUpdate, medida): 
    for i in range(len(conteudo)):
        if formatacao in conteudo[i]:
            conteudo[i] = f"{formatacao}{valorProUpdate}{medida}\n"
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


def delete(dataNomeArquivo):
    while True:
        try:
            op = int(input('Essa data se refere a um [1]treino ou [2]competição? '))
            
            match op:

                case 1:

                    nomeArquivo = f"Treino{dataNomeArquivo}.txt"
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

                    nomeArquivo = f"Competição{dataNomeArquivo}.txt"
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


def gerarRelatorioVisual(arquivosTreinos):
    if not arquivosTreinos:
        print("Nenhum treino encontrado para gerar o relatório.")
        return

    datas = []
    distancias = []
    tempos = []

    for arquivo in arquivosTreinos:
        try:
            with open(arquivo, "r", encoding="utf-8") as file:
                conteudo = file.read()
                
                data = conteudo.split("\n")[0].split(":")[1].strip()
                distancia = float(conteudo.split("\n")[1].split(":")[1].strip().replace("km", ""))
                tempo = int(conteudo.split("\n")[2].split(":")[1].strip().replace("min", ""))

                datas.append(data)
                distancias.append(distancia)
                tempos.append(tempo)

        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")

    if not datas or not distancias or not tempos:
        print("Dados insuficientes para gerar o relatório.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(datas, distancias, marker='o', label="Distância (km)")
    plt.title("Evolução de Distâncias")
    plt.xlabel("Datas")
    plt.ylabel("Distância (km)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(datas, tempos, color='orange', label="Tempo (min)")
    plt.title("Tempo em Provas e Treinos")
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
        mensagem = textoInicio()
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
                            data = input("Digite a data do seu treino (DD/MM/YYYY): ")
                            treinos["Data"] = data
                            distanciaPercorrida = float(input("Digite a distancia percorrida (KM): "))
                            treinos["DistanciaPercorrida"] = distanciaPercorrida
                            tempo = int(input("Digite o tempo em minutos que você levou para concluir esse treino: "))
                            treinos["Tempo"] = tempo
                            localizacao = input("Digite a localizacao do seu treino: ")
                            treinos["Localizacao"] = localizacao
                            condicoesClimaticas = input("Digite as condições climaticas na hora do treino: ")
                            treinos["CondicoesClimaticas"] = condicoesClimaticas
                            dataFormatada = formatacao(data)
                            create(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas) 

                        except ValueError:
                            print("Você digitou um número errado, por favor digite novamente!")

                        limparTela()
            
                    case 2:
                        try: 
                            data = input("Digite a data da sua competição (DD/MM/YYYY): ")
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
                            dataFormatada = formatacao(data)
                            createCOMP(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas, nomeCOMP) 

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
                                read(arquivosTreinos)
                                limparTela()
                                break

                            elif filtro == "sim":
                                criterio = int(input("Você deseja filtrar por distancia ou tempo? Digite 1 ou 2, respectivamente: "))
                                
                                if criterio == 1:
                                    distanciaFiltro = float(input("Digite a distancia mínima para filtrar (em km): "))
                                    readFiltrado(distanciaFiltro, arquivosTreinos, "Distancia percorrida:", "km")

                                elif criterio == 2:
                                    tempoFiltro = int(input("Digite a o tempo mínimo para filtrar (em min): "))

                                    readFiltrado(tempoFiltro, arquivosTreinos, "Tempo:", "min")

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
                                    read(arquivosTreinos)
                                    limparTela()
                                    break

                                elif filtro == "sim":
                                    criterio = int(input("Você deseja filtrar por distancia ou tempo? Digite 1 ou 2, respectivamente: "))
                                    
                                    if criterio == 1:
                                        distanciaFiltro = float(input("Digite a distancia mínima para filtrar (em km): "))
                                        readFiltrado(distanciaFiltro, arquivosTreinos, "Distancia percorrida:", "km")

                                    elif criterio == 2:
                                        tempoFiltro = int(input("Digite a o tempo mínimo para filtrar (em min): "))

                                        readFiltrado(tempoFiltro, arquivosTreinos, "Tempo:", "min")

                                    else:
                                        print("Opção invalida, por favor digite novamente!!")
                                    break

                                else: 
                                    print("Opção invalida, por favor, digite-a corretamente!")
                                
                

            case 3:
                op = int(input("Você deseja alterar um [1]treino ou [2]competição:"))
                match op:
                    case 1:
                        os.system("cls")
                        dataArquivo = input("Digite a data do treino que você deseja alterar: ")

                        dataArquivo = formatacao(dataArquivo)
                        nomeArquivo = f"Treino{dataArquivo}.txt"
                        if os.path.isfile(nomeArquivo):

                            print(f"""
{("="*70)}
Digite [1] para alterar a data
Digite [2] para alterar a distancia percorrida
Digite [3] para alterar o tempo
Digite [4] para alterar a localização
Digite [5] para alterar as condições climaticas
{("="*70)}""")
                            opcaoUpdate = int(input("Digite a opção que você deseja alterar: "))

                            conteudo = lerArquivo(nomeArquivo)

                            match opcaoUpdate:
                                case 1:
                                    novaData = input("Digite a nova data: ")
                                    
                                    conteudo = update(conteudo, "Data: ", novaData, "")

                                case 2: 
                                    novaDistanciaPercorrida = float(input("Digite a nova distancia percorrida: "))
                                    
                                    conteudo = update(conteudo, "Distancia percorrida: ", novaDistanciaPercorrida, "km")

                                case 3: 
                                    novoTempo = int(input("Digite o novo tempo: "))

                                    conteudo = update(conteudo, "Tempo: ", novoTempo, "min")
                                
                                case 4:
                                    novaLocalizacao = input("Digite a nova localização: ")
                                    
                                    conteudo = update(conteudo, "Localização: ", novaLocalizacao, "")
                                
                                case 5:
                                    novaCondicaoClimatica = input("Digite uma nova condição climatica: ")
                                    
                                    conteudo = update(conteudo, "Condições climaticas: ", novaCondicaoClimatica, "")
                            
                            atualizarArquivo(nomeArquivo, conteudo)

                            if opcaoUpdate == 1:
                                os.rename(nomeArquivo, f"Treino{formatacao(novaData)}.txt")

                            print("Alteração realizada com sucesso!")
                        
                        else:
                            print("Arquivo não localizado, por favor tente novamente")
                    
                        limparTela()
                    
                    case 2:
                        os.system("cls")
                        dataArquivo = input("Digite a data da competição que você deseja alterar: ")

                        dataArquivo = formatacao(dataArquivo)
                        nomeArquivo = f"Competição{dataArquivo}.txt"
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
                            opcaoUpdate = int(input("Digite a opção que você deseja alterar: "))

                            conteudo = lerArquivo(nomeArquivo)

                            match opcaoUpdate:
                                case 1:
                                    novaData = input("Digite a nova data: ")
                                    
                                    conteudo = update(conteudo, "Data: ", novaData, "")

                                case 2: 
                                    novaDistanciaPercorrida = float(input("Digite a nova distancia percorrida: "))
                                    
                                    conteudo = update(conteudo, "Distancia percorrida: ", novaDistanciaPercorrida, "km")

                                case 3: 
                                    novoTempo = int(input("Digite o novo tempo: "))

                                    conteudo = update(conteudo, "Tempo: ", novoTempo, "min")
                                
                                case 4:
                                    novaLocalizacao = input("Digite a nova localização: ")
                                    
                                    conteudo = update(conteudo, "Localização: ", novaLocalizacao, "")
                                
                                case 5:
                                    novaCondicaoClimatica = input("Digite uma nova condição climatica: ")
                                    
                                    conteudo = update(conteudo, "Condições climaticas: ", novaCondicaoClimatica, "")
                                
                                case 6:
                                    novoNomeCOMP = input("Digite o nome correto da competição: ")

                                    conteudo = update(conteudo, "Nome da Competição: ", novaCondicaoClimatica, "")

                            
                            atualizarArquivo(nomeArquivo, conteudo)

                            if opcaoUpdate == 1:
                                os.rename(nomeArquivo, f"Competição{formatacao(novaData)}.txt")

                            print("Alteração realizada com sucesso!")
                        
                        else:
                            print("Arquivo não localizado, por favor tente novamente")
                    
                        limparTela()


            case 4:
                os.system("cls")
                dataNomeArquivo = input("Digite a data da corrida que você deseja excluir: ")

                dataNomeArquivo = formatacao(dataNomeArquivo)
                
                delete(dataNomeArquivo)
                
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

                        update(conteudo, "Status: ", "feito✔️", "")

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
                gerarRelatorioVisual(arquivosTreinos)
                limparTela()

            case _:
                print("Opção invalido, por favor digite novamente!")
    
    except ValueError:
        os.system('cls')
        print("Opção Inválida! Informe um valor inteiro, de 0 a 6.")
        limparTela()