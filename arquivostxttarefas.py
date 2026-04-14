#Arquivo (TXT): salvar e ler tarefas

while True:
  print("\n--- Lista de Tarefas ---")
  print("1 - Adicionar tarefa")
  print("2 - Listar tarefas")
  print("0 - Sair")

  opcao = input("Escolha uma opção:")

  if opcao == "1":
    tarefa = input("Digite a tarefa:")

    with open("tarefas.txt", "a") as arquivo:
      arquivo.write(tarefa + "\n")

    print("Tarefa adicionada!")

  elif opcao == "2":
    try:
      with open("tarefas.txt", "r") as arquivo:
        tarefas = arquivo.readlines()

        if len(tarefas) == 0:
          print("Nenhuma tarefa cadastrada.")
        else:
          print("\n--- Tarefas ---")
          for i, t in enumerate(tarefas, start=1):
              print(f"{i} - {t.strip()}")


    except FileNotFoundError:
      print("Nenhum arquivo de tarefas encontrado.")

  elif opcao == "0":
    print("Saindo...")
    break
  else:
    print("Opção inválida!")