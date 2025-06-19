import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def formata_preco(val):
    return f'{locale.currency(val, True, True)}'


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def cart_total_cash(carrinho):
    total = 0
    for item in carrinho.values():
        if item['preco_quantitativo_promocional']:
            total += item['preco_quantitativo_promocional']
        else:
            total += item['preco_quantitativo']
    return total
