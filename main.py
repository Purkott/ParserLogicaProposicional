# Aluno: Fernando Purkott

'''
Enunciado
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional 
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma 
da expressão (sintaxe).  
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando, 
com a seguinte formatação:  
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões 
lógicas estão no arquivo.  
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.  
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída 
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais. 
Gramática:  
Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.  
Constante="T"|"F". 
Proposicao=[a−z0−9]+ 
FormulaUnaria=AbreParen OperadorUnario Formula FechaParen 
FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen 
AbreParen="(" 
FechaParen=")" 
OperatorUnario="¬" 
OperatorBinario="∨"|"∧"|"→"|"↔" 
 
Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, 
conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações. 
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em 
qualquer expressão de entrada. 
Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arquivos  contendo 
números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arquivo  de  testes  extra 
para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu 
programa carregando o arquivo de testes. 
'''

validos = "abcdefghijklmnopqrstuvwxyz1234567890↔→∧∨TF¬()"
proposicao = "abcdefghijklmnopqrstuvwxyz1234567890"


def start():
  global arquivo
  global arquivos
  global arquivo1
  global arquivo2
  global arquivo3
  global expressao
  expressao = []
  txt1 = open('arquivos/1.txt', 'r')
  arquivo1 = []
  arquivo1.append(txt1.readline().strip())
  for x in range(int(arquivo1[0])):
    arquivo1.append(txt1.readline().strip())
  txt1.close()
  '''
  txt2 = open('arquivos/2.txt', 'r')
  arquivo2 = []
  arquivo2.append(txt2.readline().strip())
  for x in range(int(arquivo2[0])):
    arquivo2.append(txt2.readline().strip())
  txt2.close()

  txt3 = open('arquivos/3.txt', 'r')
  arquivo3 = []
  arquivo3.append(txt3.readline().strip())
  for x in range(int(arquivo3[0])):
    arquivo3.append(txt3.readline().strip())
  txt3.close()
  '''
  global RESULTADO 
  global ESTADO
  global contadorString 
  global contadorLinhas 
  global contadorArquivo 
  RESULTADO = " "
  ESTADO = "ESTADO0"
  contadorString = 0
  contadorLinhas = 1
  contadorArquivo = 1
  #arquivos = [arquivo1,arquivo2,arquivo3]
  arquivo = arquivo1.copy()
  formula = ""
  for x in arquivo[1]:
    if x != " ":
      formula = formula + "" + x
      if arquivo[1][-1] == x:
        expressao.append(formula)
        
    else:
      expressao.append(formula)
      formula = ""
    
  print(expressao)

def checaconstante(expressao):
    if (expressao[0] == "T" or expressao[0] == "F"):
        if len(expressao) < 2:
          return True
        elif len(expressao) >1:
          return False
    else:
      return False

def checaproposicao(expressao):
  if expressao[0] in proposicao:
    if len(expressao) < 2:
      return True
    elif len(expressao) >1:
      return False
  else:
    return False

def checaformulaunaria(expressao):
  if expressao[0] != "(":
    return False
  else:
    if expressao[1] != "¬":
      return False
    else:
      if not checaconstante(expressao[2]) and not checaproposicao(expressao[2]) and not expressao[2] == "(":
        return False
      else:
        if
    
    


def checaformula(expressao):
  for i in range(len(expressao)):
    if expressao[i] not in validos:
      if len(expressao[i]) >1:
        if expressao[i][0] not in validos or expressao[i][1] not in validos:
          expressao.append(": invalida")
          return print(*expressao)
      else:
        expressao.append(": invalida")
        return print(*expressao)
  if checaconstante(expressao):
    expressao.append(": valida")
    return print(*expressao)
  else:
    if checaproposicao(expressao):
      expressao.append(": valida")
      return print(*expressao)
    else:
      if expressao[0] == "(":
        if checaformulaunaria(expressao):
          expressao.append(": valida")
          return print(*expressao)
      else:
        expressao.append(": invalida")
        return print(*expressao)

  

start()
checaformula(expressao)