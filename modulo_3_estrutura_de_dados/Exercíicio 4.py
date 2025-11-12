# Estoque inicial
estoque = {
    'arroz': 5,
    'feijão': 2,
    'macarrão': 0,
    'açúcar': 3,
    'óleo': 7
}

print('=== ATUALIZAÇÃO DE ESTOQUE ===')

# Atualiza as quantidades
for item in estoque:
    nova_qtd = int(input(f'Informe a nova quantidade de {item}: '))
    estoque[item] = nova_qtd

# Relatório final
print('\n=== RELATÓRIO DE ESTOQUE ===')
for item, quantidade in estoque.items():
    print(f'\nProduto: {item} | Quantidade: {quantidade}')
    if quantidade == 0:
        print('Item indisponível!')
    elif quantidade <= 3:
        print('Repor o estoque!')
    else:
        print('Estoque suficiente.')
