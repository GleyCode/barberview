from django import template

register = template.Library()

@register.filter
def format_phone(value):
    """Formata o telefone do cliente."""
    phone = str(value).strip()
    
    # Formato: 00 00000-0000 (11 dígitos)
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    
    # Formato: 00 0000-0000 (10 dígitos), telefone fixo.
    if len(phone) == 10:
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
    
    return value

@register.filter
def format_cpf(value):
    """Formata o cpf do cliente."""
    cpf = str(value).strip()
    
    # Formato: 000.000.000-00 (11 dígitos).
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    return value
