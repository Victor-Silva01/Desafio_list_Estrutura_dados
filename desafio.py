class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE
    
    # Função que serve para definir se o array está vazio ou não
    def isEmpty(self):
        return self.size() == 0
    
    # Função que retorna o número de elementos armazenados no array   
    def size(self):
        return self.insertPosition
        
    # Função que define se precisamos de mais memória
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)
    
    # Função para inserir na lista
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1
    
    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    # Função para limpar as posições
    def clear(self):
        self.elements = [None] * self.SIZE
        self.insertPosition = 0
    
    # Função para remover o último elemento
    def remove(self):
        if self.insertPosition > 0:
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1
    
    # Função para remover um elemento da lista com base em uma posição
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return
        
        # Desloca os elementos à direita para preencher o espaço removido
        for i in range(position, self.insertPosition - 1):
            self.elements[i] = self.elements[i + 1]

        # Define o último elemento como None e reduz o tamanho
        self.elements[self.insertPosition - 1] = None
        self.insertPosition -= 1


# Testando o código com inserções adicionais
array = PersonalArray()

# Adicionando mais elementos ao array
array.append("fusca")
array.append("kombi")
array.append("kwid")
array.append("Ferrari")
array.append("Hilux")
array.append("fusca")
array.append("kombi")
array.append("kwid")
array.append("Ferrari")
array.append("Hilux")
array.append("fusca")
array.append("kombi")
array.append("kwid")
array.append("Ferrari")
array.append("Hilux")

# Exibindo o estado do array antes da remoção
print("Antes de remover a posição 3:")
print(array.elements)

# Teste de remoção de um elemento por posição
array.removePosition(3)  # Removendo o elemento na posição 3 (no caso "Ferrari")

# Exibindo o estado do array após a remoção
print("Após remoção da posição 3:")
print(array.elements)
