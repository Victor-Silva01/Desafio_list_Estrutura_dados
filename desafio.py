class PersonalArray:
    def __init__(self, initial_size=5):
        self.SIZE = initial_size
        self.insert_position = 0
        self.elements = [None] * self.SIZE

    def is_empty(self):
        return self.insert_position == 0

    def is_full(self):
        return self.insert_position == len(self.elements)

    def size(self):
        return self.insert_position

    def append(self, new_element):
        if self.is_full():
            self.expand_memory()
        self.elements[self.insert_position] = new_element
        self.insert_position += 1

    def expand_memory(self):
        new_capacity = len(self.elements) + self.SIZE
        new_elements = [None] * new_capacity
        for i in range(self.insert_position):
            new_elements[i] = self.elements[i]
        self.elements = new_elements

    def clear(self):
        self.elements = [None] * self.SIZE
        self.insert_position = 0

    def remove_last(self):
        if not self.is_empty():
            self.insert_position -= 1
            removed = self.elements[self.insert_position]
            self.elements[self.insert_position] = None
            return removed
        return None

    def remove_at(self, position):
        if position < 0 or position >= self.insert_position:
            print("⚠️ Posição inválida.")
            return None
        removed = self.elements[position]
        for i in range(position, self.insert_position - 1):
            self.elements[i] = self.elements[i + 1]
        self.insert_position -= 1
        self.elements[self.insert_position] = None
        return removed

    def insert_at(self, position, new_element):
        if position < 0 or position > self.insert_position:
            print("⚠️ Posição inválida.")
            return
        if self.is_full():
            self.expand_memory()
        for i in range(self.insert_position, position, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[position] = new_element
        self.insert_position += 1

    def get(self, position):
        if position < 0 or position >= self.insert_position:
            print("⚠️ Posição inválida.")
            return None
        return self.elements[position]

    def __str__(self):
        return str([self.elements[i] for i in range(self.insert_position)])


class PersonalStack:
    def __init__(self):
        self.stack = PersonalArray()

    def push(self, element):
        self.stack.insert_at(0, element)
        print(f"📥 Adicionado: {element}")
        self.show()  # 👈 Mostra a pilha logo após adicionar

    def pop(self):
        removed = self.stack.remove_at(0)
        if removed is not None:
            print(f"✅ Removido: {removed}")
        else:
            print("⚠️ A pilha já está vazia.")

    def show(self):
        if self.stack.is_empty():
            print("📭 Pilha vazia!")
        else:
            print("📌 Tags atuais:", self.stack)


# Interface CLI
if __name__ == "__main__":
    stack = PersonalStack()
    print("\n💬 Digite uma palavra para adicionar à lista de tags.")
    print("Comandos disponíveis:")
    print("  \\pop   → Remove a última tag adicionada.")
    print("  \\show  → Mostra todas as tags.")
    print("  \\exit  → Encerra o programa.\n")

    while True:
        user_input = input("👉 ").strip()
        if user_input == "\\show":
            stack.show()
        elif user_input == "\\pop":
            stack.pop()
        elif user_input == "\\exit":
            print("👋 Encerrando o programa.")
            break
        else:
            stack.push(user_input)
