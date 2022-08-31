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
constante = ["T","F"]
abreParen = "("
fechaParen = ")"
operadorUn = "\\neg"
operadorBin = ["\\vee", "\\wedge", "\\rightarrow", "\\leftrightarrow"]
proposicao1 = "abcdefghijklmnopqrstuvwxyz"
proposicao2 = "0123456789"


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

def checaConstante(formula):
  if len(formula) == 1:
    if formula[0] == constante[0] or formula[0] == constante[1]:
      return True
    else:
      return False
  else:
    return False

def checaProposicao(formula):
  if len(formula) == 1: 
    if len(formula[0]) < 3:
      if len(formula[0]) == 1:
        if formula[0] in proposicao1 or formula[0] in proposicao2:
          return True
        else: 
          return False
      else:
        if formula[0][0] in proposicao1 and formula[0][1] in proposicao2:
          return True
        else: 
          return False
    else:
      return False
  else:
    return False
    
def checaFormulaUn(formula):
  if formula[0] == abreParen and formula[1] == operadorUn:
    formula1 = arrumaFormula1(formula[2:])
    if len(formula) - len(formula1) != 3:
      return False
    else:
      if checaformula(formula1) and formula[-1] == ")":
        return True
      else:
        return False
  else:
    return False

def checaFormulaBin(formula):
  formula1 = []
  formula2 = []
  formula3 = []
  if formula[0] == abreParen and formula[1] in operadorBin:
    formula1 = arrumaFormula1(formula[2:])
    formula2 = arrumaFormula2(formula[2:])
    formula3.append(formula1)
    formula3.append(formula2)
    if len(formula) - len(formula3) != 3:
      return False
    else:
      if checaformula(formula1) and checaformula(formula2) and formula[-1] == ")":
        return True
      else:
        return False
  else:
    return False
      


def checaformula(expressao):
  if type(expressao) == type("abcd"):
    formula = expressao.rsplit(" ")
  else:
    formula = expressao
  if (checaConstante(formula) or checaProposicao(formula) or checaFormulaUn(formula) or checaFormulaBin(formula)): 
    return True
  else:
    return False
  
    
def arrumaExpressao(expressao):
  formula = expressao.rsplit(" ")
  return print(formula)

def arrumaFormula1(expressao):
  formula = []
  if expressao.count("(") > 0 and expressao.index("(") == 0:
    if expressao.count(")") > 0:
      contador = 1
      formula = ["("]
      while formula.count("(") != formula.count(")") and contador < len(expressao):
        formula.append(expressao[contador])
        contador = contador + 1
    else:
      formula = ["invalida"]
  else:
    formula = expressao[0]
  
  return formula

def arrumaFormula2(expressao):
  formula = []
  formula1 = []
  formula1 = arrumaFormula1(expressao)
  formula = arrumaFormula1(limpaLista(expressao, formula1))
  return formula
  

def limpaLista(lista1,lista2):
  lista = []
  n = len(lista2)
  while n < len(lista1):
    lista.append(lista1[n])
    n = n + 1 
 

  
  return lista
  
  
start()
arrumaExpressao(arquivo[1])
print(checaformula(arquivo[1]))
arrumaExpressao(arquivo[2])
print(checaformula(arquivo[2]))
arrumaExpressao(arquivo[3])
print(checaformula(arquivo[3]))