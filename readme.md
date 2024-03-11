# Cálculo de Médias Móveis

Este projeto envolve o cálculo da média móvel do volume de tráfego em intervalos de
tempo específicos para cada interseção em um sistema de monitoramento de tráfego
em tempo real e tem por objetivo colocar em prática os conceitos aprendidos sobre
Deque.

## Atividade

- Escreva um programa em Python para ler os dados do volume de tráfego e
apresente as média móveis de k períodos de tempo.
- Crie seu próprio Tipo de Dado para resolver o problema ao invés de utilizar tipos
prontos.

## Funcionalidades

1. Ler dados do volume de trafego a partir do teclado
2. Ler dados do volume de trafego a partir de arquivo texto
3. Alterar configuração do valor K de períodos para média móvel. O Padrão deve ser
4. Exibir as médias móveis calculadas para os dados lidos
5. Salvar em arquivo as médias móveis calculadas para os dados lidos

## Implementação e Restrições

1. **Definição do TAD e Funções Auxiliares:**
1.1 Defina um Tipo de Dado que irá armazenar os dados e realizar o cálculo da média
móvel.
1.2 Crie funções auxiliares para inicializar a estrutura de deque e para calcular a
média móvel.
1.3 Não utilize Um tipo Deque pronto da linguagem ou de qualquer módulo/pacote.
1.4 Não utilize estrutura de dados existente para simular o Deque.
1.5 Crie seu TAD Deque a partir do TAD FilaArray apresentado em Sala!
2. **Tratamento dos Primeiros Elementos:**
2.1 Para os primeiros K elementos, onde não há elementos anteriores suficientes,
atribua None para média móvel.
3. **Teste e Validação:**
3.1 Teste o algoritmo com diferentes conjuntos de dados para garantir que ele está
calculando as médias móveis corretamente.

## Critérios de Avaliação

1. Executar sem erros
2. Implementação de acordo com as Funcionalidades e Restrições apresentadas
3. Entregar o que o foi solicitado (código e leiame)
4. Apresentar o projeto

# Solução

## Passos

### Implementar TAD Deque

Comecei criando o construtor da seguinte forma:

```
  class Deque:

    def __init__(self):
    self._capacity = 5
    self._items = [None] * self._capacity
    self._index_first = None

```

Depois que comecei a criar os metódos de inserir e remover, sentir necessidade de adicionar mais alguns atributos:

```
  def __init__(self,  capacity):
    if capacity < 2:
      raise Exception("Capacity must be at least 2")
    self._capacity_init = capacity
    self._capacity = capacity
    self._items = [None] * capacity
    self._size = 0
    self._index_first = None
    self._index_last = None
```

Em seguida criei os seguintes metodos:

```
  def is_empty(self):
    return self._size == 0
  
  
  def size(self):
    return self._size
  

  def is_full(self):
    return self._size == self._capacity
```
Estava com dificudade para assimilar os resultados e de visualizar a mudança dos valores, então criei a seguinte tabela no calc:

![Tabela com valores e resultados dos metodos do deque](./image/Captura%20de%20tela%202024-03-03%20150534.png)

Veja abaixo como a class Deque ficou:

```
  class Deque:

  def __init__(self,  capacity):
    if capacity < 2:
      raise Exception("Capacity must be at least 2")
    self._capacity_init = capacity
    self._capacity = capacity
    self._items = [None] * capacity
    self._size = 0
    self._index_first = None
    self._index_last = None

  
  def is_empty(self):
    return self._size == 0
  
  
  def size(self):
    return self._size
  

  def is_full(self):
    return self._size == self._capacity
  

  def first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    return self._items[self._index_first]
  
    
  def last(self):
    if self.is_empty():
      raise Exception("Deque is empty")

    return self._items[self._index_last]


  def items(self):
    return self._items
  

  def add_first(self, item):

    if self.is_full():
      self._resize(2 * self._capacity)

    
    if self.is_empty():
      self._items[0] = item
      self._index_first = 0
      self._index_last = 0
      self._size += 1
      return

      
    if self._index_first == 0:
      self._index_first = self._capacity - 1
      self._items[self._index_first] = item
      self._size += 1
      return
    
    self._index_first -= 1
    self._items[self._index_first] = item
    self._size += 1
    return
    

  def remove_first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
        
    if (self._size - 1 == self._capacity // 4) and (self._capacity // 2 >= self._capacity_init):
      self._resize(self._capacity // 2)
      
    item = self.first()
    self._items[self._index_first] = None
    
    if self._size == 1:
      self._index_first = None
      self._index_last = None
      self._size = 0
      return item
    
    if self._index_first == self._capacity - 1:
      self._index_first = 0
      self._size -= 1
      return item

    self._index_first += 1
    self._size -= 1
    return item

  
  def add_last(self, item):
    if self.is_full():
      self._resize(2 * self._capacity)

    if self.is_empty():
      self._items[0] = item
      self._index_first = 0
      self._index_last = 0
      self._size += 1
      return

    if self._index_last == self._capacity - 1:
      self._index_last = 0
      self._items[self._index_last] = item
      self._size += 1
      return
    
    self._index_last += 1
    self._items[self._index_last] = item
    self._size += 1
    return

  
  def remove_last(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    
    if (self._size - 1) == (self._capacity // 4) and( self._capacity // 2) >= self._capacity_init:
      self._resize(self._capacity // 2)	
      
    item = self.last()
    self._items[self._index_last] = None
    
    if self._size == 1:
      self._index_first = None
      self._index_last = None
      self._size -= 1
      return item
    
    if self._index_last == 0:
      self._index_last = self._capacity - 1
      self._size -= 1
      return item

    self._index_last -= 1
    self._size -= 1
    return item

  def _resize(self, new_capacity):

    new_items = [None] * new_capacity
    self._capacity = new_capacity
    index = 0
  
    while self._size > 0:
      first = self.remove_first()
      new_items[index] = first
      index += 1
    
    self._items = new_items
    self._capacity = new_capacity
    self._size = index
    self._index_first = 0
    self._index_last = self._size - 1


  def print(self):
    print(self._items)
 
```
## Anotação Big O (Deque)

Como mencionado anteriormente, ao adicionar os índices do primeiro e último elementos, juntamente com o tamanho do deque, conseguimos eliminar a necessidade de loops ao adicionar, remover e acessar elementos do deque, o que torna essas operações O(1). No entanto, é importante notar que há casos em que o deque precisa redimensionar sua capacidade, especialmente quando está cheio ou muito pequeno. Nessas situações, um loop é utilizado para realocar e organizar os elementos no deque, resultando em uma complexidade de O(n) para essas operações.

## Buscar entender o problema de cálculo de médias moveis
[Moving Average (MA): Purpose, Uses, Formula, and Examples](https://www.investopedia.com/terms/m/movingaverage.asp)

## Solução

Inicialmente a solução ficou da seguinte forma:

```
def moving_average(input_list, k):
  deque = Deque()
  for i in range(len(input_list)):
    if i == 0:
      deque.add_last(None)
      deque.add_last(input_list[i])
      continue

    if (i + 1) < k:
      last = deque.remove_last()
      deque.add_last(None)
      deque.add_last(last + input_list[i])
      continue

    last = deque.remove_last()
    sum_step = last + input_list[i]
    deque.add_last(sum_step / 3)

    if i < (len(input_list) - 1):
      del_element = input_list[i - (k - 1)]
      deque.add_last(sum_step - del_element)

  return deque.items()
  
```
Em seguida para melhorar o desempenho do algoritmo, modifiquei o deque para receber a capacidade inicial, com isso, não ocorrerá o loop para aumento da capacidade do deque (resize), pois o deque já começará com o tamanho ideal.

```
def moving_average(input_list, k):
  deque = Deque(len(input_list))
  for i in range(len(input_list)):
    if i == 0:
      deque.add_last(None)
      deque.add_last(input_list[i])
      continue

    if (i + 1) < k:
      last = deque.remove_last()
      deque.add_last(None)
      deque.add_last(last + input_list[i])
      continue

    last = deque.remove_last()
    sum_step = last + input_list[i]
    deque.add_last(sum_step / 3)

    if i < (len(input_list) - 1):
      del_element = input_list[i - (k - 1)]
      deque.add_last(sum_step - del_element)

  return deque.items()
```

## Anotação Big O (Cálculo da média móvel)

Como observado na análise da notação Big O do Deque, nos casos em que há a necessidade de redimensionar a capacidade, a complexidade pode se tornar O(n). No cálculo da média móvel, é informada a capacidade do deque necessário para realizar o cálcula sem a necessidade de redimencionar, porém para o cálculo da média móvel, foi utilizado um loop que percorre toda a lista, tornando a solução O(n).