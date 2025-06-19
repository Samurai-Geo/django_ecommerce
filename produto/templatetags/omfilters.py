from django.template import Library
from decimal import Decimal, InvalidOperation
from utils import utils

register = Library()


@register.filter
def formata_preco(val):
    try:
        valor = Decimal(val)
        return utils.formata_preco(val)
    except (ValueError, InvalidOperation):
        return val


@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)


@register.filter
def cart_total_cash(carrinho):
    return utils.cart_total_cash(carrinho)
