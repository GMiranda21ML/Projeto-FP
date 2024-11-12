treinos = {"Data":[], "DistanciaPercorrida":[], "Tempo":[], "Localizacao":[], "CondicoesClimaticas":[]}

os.system("cls")
while True:
    print("""
Digite 1 para adicionar um registro de treino e competição
Digite 2 para visualizar um registro de treino e competição
Digite 3 para atualizar um registro de treino e competição
Digite 4 para excluir um registro de treino e competição
Digite 6 para vê sugestões de treinos aleatorios
Digite 0 para encerrar o programa""")
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

                print("""
Digite 1 para alterar a data
Digite 2 para alterar a distancia percorrida
Digite 3 para alterar o tempo
Digite 4 para alterar a localização
Digite 5 para alterar as condições climaticas""")
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