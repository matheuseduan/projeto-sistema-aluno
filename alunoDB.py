from aluno import Aluno # pega do arquivo aluno.py a classe Aluno()

class AlunoDB: # classe AlunoDB
    def __init__(self): # construtor
        self.alunos = [] # cria uma lista

    def adicionarAluno(self): # metodo adicionarAluno(self)
        nome = input("Nome: ") # pega o nome do aluno
        matricula = input("Matrícula: ") # pega a matricula do aluno

        try:
            nota = float(input("Nota: ")) # pega a nota do aluno
        except ValueError:
            print("Ocorreu um erro de no valor da nota")
            return

        for aluno in self.alunos: # coloca em "aluno" um por um elemento da lista "self.alunos"
            if matricula == aluno.matricula: # verifica se a "matricula" já está na lista, se sim mostra como erro
                print(f"O aluno {aluno.nome} já está cadastrado com essa matrícula ({matricula})") # imprime uma mensagem
                return # para a execução
        
        if nota < 0 or nota > 10:
            print("Nota invalida")
            return

        aluno = Aluno(nome, matricula, nota) # utiliza a classe Aluno(nome, matricula, nota) para criar um aluno e atribui a "aluno"

        self.alunos.append(aluno) # adiciona "aluno" na lista

        print(f"Aluno {nome} cadastrado!") # imprime uma mensagem

    def removerAluno(self): # metodo removerAluno(self)
        if not self.alunos: # verifica se a lista "self.alunos" está vazio, se sim mostra como erro
            print("Nenhum aluno") # imprime uma mensagem
            return # para a execução

        matricula = input("Matrícula: ") # pede a matricula do aluno

        for aluno in self.alunos: # coloca em "aluno" um por um elemento da lista "self.alunos"
            if aluno.matricula == matricula: # verifica todas as matriculas da lista pela a "matricula" digitada, se sim remove o aluno
                self.alunos.remove(aluno) # remove o aluno da lista
                print(f"Aluno {aluno.nome} removido com sucesso.") # imprime uma mensagem
                return # para a execução
        
        print("Aluno não encontrado.") # se não encontra a matricula imprime essa mensagem

    def listarAlunos(self): # metodo listarAlunos(self):
        if not self.alunos: # verifica se a lista "self.alunos" está vazio, se sim mostra como erro
            print("Nenhum aluno") # imprime uma mensagem
            return # para a execução
        
        print(f"\n#--- ALUNOS ---#") # imprime uma mensagem
        for aluno in self.alunos: # coloca em "aluno" um por um elemento da lista "self.alunos"
            print(f"Nome: {aluno.nome} | Matrícula: {aluno.matricula} | Nota: {aluno.nota}") # imprime todas as informações dos alunos
    
    def atualizarNotaAluno(self): # metodo atualizarNotaAluno(self)
        if not self.alunos: # verifica se a lista "self.alunos" está vazio, se sim mostra como erro
            print("Nenhum aluno") # imprime uma mensagem
            return # para a execução

        matricula = input("Matrícula: ") # pede a matricula do aluno

        for aluno in self.alunos: # coloca em "aluno" um por um elemento da lista "self.alunos"
            if aluno.matricula == matricula: # verifica se a matricula do aluno existe
                
                try:
                    novaNota = float(input(f"Nova nota de {aluno.nome}: ")) # nova nota do aluno
                except ValueError:
                    print("Ocorreu um erro de no valor da nota")
                    return
                
                if novaNota < 0 or novaNota > 10:
                    print("Nota invalida")
                    return
                
                aluno.nota = novaNota # atribui a nova nota para a nota atual do aluno
                print(f"Nota do aluno {aluno.nome} foi atualizada para {novaNota}.") # imprime uma mensagem
                return # para a execução
        
        print("Aluno não encontrado.") # se não encontra a matricula imprime essa mensagem
    
    def menu(self):
        while(True):
            print("""
            === SISTEMA DE CADASTRO ===
            1. Cadastrar aluno
            2. Listar alunos
            3. Atuaizar nota
            4. Excuir aluno
            Qualquer tecla. Sair""")
    
            opcao = input("Escolha a opção: ")

            match opcao:
                case "1":
                    self.adicionarAluno()
                case "2":
                    self.listarAlunos()
                case "3":
                    self.atualizarNotaAluno()
                case "4":
                    self.removerAluno()
                case _:
                    break

if __name__ == "__main__":
    bancoDados = AlunoDB()
    bancoDados.menu()