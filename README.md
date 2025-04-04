📦 Projeto: Estrutura de Dados - Pilha com Array Dinâmico em Python
Este repositório apresenta a implementação de uma pilha (stack) utilizando uma estrutura de array dinâmico personalizada em Python, sem uso de bibliotecas prontas. É um ótimo exercício para quem está aprendendo estruturas de dados e deseja compreender a lógica por trás de pilhas e arrays com expansão de memória.

⚙️ Funcionalidades Implementadas
📌 Classe PersonalArray
Simula um array com capacidade de expansão automática:

Adição com expansão automática:
append() adiciona elementos ao final; insert_at() insere em posições específicas.

Remoção de elementos:
remove_last() remove o último elemento; remove_at() remove por posição.

Gerenciamento de memória:
expand_memory() aumenta a capacidade de armazenamento quando necessário.

Utilitários extras:
Métodos como clear(), get(), is_empty() e is_full().

🧱 Classe PersonalStack
Utiliza o PersonalArray para implementar o comportamento de uma pilha (LIFO):

push(element): insere no topo da pilha.

pop(): remove o elemento do topo.

show(): exibe os elementos atuais da pilha em ordem.

💻 Interface CLI
O sistema roda no terminal e aceita comandos interativos:

\\pop → Remove a última tag adicionada.

\\show → Mostra todas as tags atuais.

\\exit → Encerra o programa.

Qualquer outro texto será adicionado como nova tag.

🎯 Objetivo do Projeto
O projeto tem como objetivo reforçar o aprendizado de:

Estruturas de dados (Pilha)

Manipulação direta de arrays

Expansão dinâmica de memória

Boas práticas em Python com orientação a objetos

📸 Exemplo de Uso
bash
Copiar
Editar
💬 Digite uma palavra para adicionar à lista de tags.
Comandos disponíveis:
  \pop   → Remove a última tag adicionada.
  \show  → Mostra todas as tags.
  \exit  → Encerra o programa.

👉 Python
📥 Adicionado: Python
📌 Tags atuais: ['Python']

👉 Java
📥 Adicionado: Java
📌 Tags atuais: ['Java', 'Python']

👉 \pop
✅ Removido: Java
📌 Tags atuais: ['Python']
