import os

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
    with open(f"Treino{dataFormatada}.txt", "w", encoding="utf-8") as file:
        file.write(f"""Data: {data}
Distancia percorrida: {distanciaPercorrida}km
Tempo: {tempo}min
Localização: {localizacao}
Condições climaticas: {condicoesClimaticas}
""")


def selecionartudo(comeco, fim, caminho):
    arquivosTreinos = []
    for arquivo in os.listdir(caminho):
        if arquivo.startswith(comeco) and arquivo.endswith(fim): #and os.path.isfile(arquivo):
            arquivosTreinos.append(arquivo)
    return arquivosTreinos


def read():
    for arquivo in arquivosTreinos:
        with open(arquivo, "r", encoding="utf-8") as file:
            print(f"\nArquivo: {arquivo}")
            print(file.read())
            print("-" * 30)
            file.close()


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


#obs: tlvz eu consiga juntar o update com o atualizarArquivo
def update(conteudo, formatacao, valorProUpdate, medida): 
    for i in range(len(conteudo)):
        if formatacao in conteudo[i]:
            conteudo[i] = f"{formatacao}{valorProUpdate}{medida}\n"
    return conteudo


def atualizarArquivo(nomeArquivo, conteudo):
    with open(nomeArquivo, "w", encoding="utf-8") as file:
        file.writelines(conteudo)


def lerArquivo(nomeArquivo):
    with open(nomeArquivo, "r", encoding="UTF-8") as file:
        conteudo = file.readlines()
    return conteudo


def delete():
    if os.path.exists(f"Treino{dataNomeArquivo}.txt"):
        os.remove(f"Treino{dataNomeArquivo}.txt")
        print("Arquivo excluido com sucesso!")
    else:
        print("Arquivo não encontrado! por favor tente novamente")


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
    novonum=num-1
    try:
        with open("Metas.txt", "r") as file:
            linhas = file.readlines()

        quant = len(linhas)  
        
        if novonum >= quant:
            print("Número inválido, excede o número de metas.")
            return

        with open("Metaconcluida.txt", "a") as concluida:
            concluida.write(linhas[novonum])
        
        with open("Metas.txt", "w") as metas:
            for i in range(quant):
                if i != novonum:
                    metas.write(linhas[i])
        
        print(f"Meta {num} marcada como concluída")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    except FileNotFoundError:
        print('Esse arquivo não existe') 

def lermetasconcluidas():
    try:
        with open(f"Metaconcluida.txt","r") as file:
            conteudo=file.read()
            print(conteudo)
    except FileNotFoundError:
        print('Esse arquivo não existe')  

treinos = {"Data":[], "DistanciaPercorrida":[], "Tempo":[], "Localizacao":[], "CondicoesClimaticas":[]}

os.system("cls")
while True:
    
    try:
        mensagem = textoInicio()
        print(f"""
{("="*70)}        
Digite [1] para adicionar um registro de treino e competição
Digite [2] para visualizar um registro de treino e competição
Digite [3] para atualizar um registro de treino e competição
Digite [4] para excluir um registro de treino e competição
Digite [5] para registrar/visualizar suas metas;
Digite [6] para vê sugestões de treinos aleatorios
Digite [0] para encerrar o programa
{("="*70)}""")
    
        opcao = int(input("Digite sua opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break
        
            case 1:
                try: 
                    data = input("Digite a data do seu treino/competição (DD/MM/YYYY): ") # LEMBRAR DA TRATAÇÃO DO USUARIO EX: DATA > 10
                    treinos["Data"] = data
                    distanciaPercorrida = float(input("Digite a distancia percorrida (KM): "))
                    treinos["DistanciaPercorrida"] = distanciaPercorrida
                    tempo = int(input("Digite o tempo em minutos que você levou para concluir esse treino/competição: "))
                    treinos["Tempo"] = tempo
                    localizacao = input("Digite a localizacao do seu treino/competição: ")
                    treinos["Localizacao"] = localizacao
                    condicoesClimaticas = input("Digite as condições climaticas na hora do treino/competição: ")
                    treinos["CondicoesClimaticas"] = condicoesClimaticas
                    dataFormatada = formatacao(data)
                    create(dataFormatada, data, distanciaPercorrida, tempo, localizacao, condicoesClimaticas) 

                except ValueError:
                    print("Você digitou um número errado, por favor digite novamente!")

                limparTela()
    

            case 2:
                os.system("cls")
                while True:
                    filtro = input("Você deseja filtrar na hora da visualização de seus treinos (Sim/Nao)? ").lower()
                    
                    arquivosTreinos = selecionartudo("Treino", ".txt", ".")

                    if filtro == "nao" or filtro == "não":
                        read()
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
                    
                limparTela()


            case 3:
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


            case 4:
                os.system("cls")
                dataNomeArquivo = input("Digite a data do treino que você deseja excluir: ")

                dataNomeArquivo = formatacao(dataNomeArquivo)
                
                delete()
                
                limparTela()

            case 5:
                os.system("cls")
                opção=input(f"""
{("="*70)}
Digite [1] para criar uma meta
Digite [2] para ler as metas atuais
Digite [3] para marcar uma meta como conluida
Digite [4] para ver as metas concluidas
{("="*70)}\nDigite o que deseja fazer:""")
                if(opção=='1'):
                    data=str(input("Digite a data em que a meta foi criada:"))
                    meta=str(input("Digite sua meta:"))
                    cadastroMetas(data,meta)
                elif(opção=='2'):
                    lerMetas()
                elif(opção=='3'):
                    lerMetas()
                    num=int(input("Digite o numero da meta que deseja marcar como concluida:"))
                    concluirmeta(num)
                elif(opção=='4'):
                    lermetasconcluidas()
                else:
                    print("digito errado")
            
            case 6:
                os.system("cls")
                
                caminhoDaPasta = "treinosAleatorios"

                listaAleatorios =  selecionartudo("treinoAleatorio", ".txt", caminhoDaPasta)
                
                for treinosAleatorios in listaAleatorios:
                    caminhoArquivo = os.path.join(caminhoDaPasta, treinosAleatorios) #caminhoDaPasta + "/" + treinoAleatorio
                    with open(caminhoArquivo, "r", encoding="UTF-8") as file:
                        print(f"\nArquivo: {treinosAleatorios}")
                        print(file.read())
                        print("-" * 30)
                        file.close() 
                
                while True:
                    print("Você fez algum dos treinos aleatorios?")
                    fazer = int(input("Se sim, digite o número de 1 a 5 para marcar como feito, se nao, digite 0: "))
                    
                    if 1 <= fazer <= 5:
                        treinoFeito = "treinoAleatorio" + str(fazer) + ".txt"
                        arquivoCaminho = os.path.join(caminhoDaPasta, treinoFeito)
                        
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

            case _:
                print("Opção invalido, por favor digite novamente!")
    
    except ValueError:
        os.system('cls')
        print("Opção Inválida! Informe um valor inteiro, de 0 a 6.")
        limparTela()