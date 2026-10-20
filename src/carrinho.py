class Produto:
  def __init__(self, nome, preco, quantidade=1):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

  def __str__(self):
    return f"{self.nome} - R$ {self.preco:.2f}, quantidade {self.quantidade}"

class Carrinho:

  def __init__(self):
    self.produtos = []

  def adicionar_item(self, produto):
    self.produtos.append(produto)
    print(f"Produto '{produto.nome}' adicionado ao carrinho.")

  def remover_itens(self, nome_produto):
    for p in self.produtos:
      if p.nome.lower() == nome_produto.lower():
        self.produtos.remove(p)
        print(f"Produto '{p.nome}' removido do carrinho.")
        return
    print(f"Produto '{nome_produto}' não encontrado no carrinho.")

  def calcular_total(self):
    total = sum(p.preco for p in self.produtos)
    return total

  def exibir_carrinho(self):
    if not self.produtos:
      print("O carrinho está vazio.")
      return

    print("\n--- Itens no Carrinho ---")
    for i, produto in enumerate(self.produtos, 1):
      print(f"{i}. {produto}")
    print(f"Total: R$ {self.calcular_total():.2f}")
    print("--------------------------\n")


if __name__ == "__main__":
  prod1 = Produto("Notebook", 3500.00)
  prod2 = Produto("Mouse Gamer", 150.50)
  prod3 = Produto("Teclado Mecânico", 280.00)

  carrinho = Carrinho()

  carrinho.adicionar_produto(prod1)
  carrinho.adicionar_produto(prod2)
  carrinho.adicionar_produto(prod3)

  carrinho.exibir_carrinho()


  carrinho.remover_item("Mouse Gamer")

  carrinho.exibir_carrinho()
