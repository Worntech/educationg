from django import template

register = template.Library()

@register.filter
def divide_to_dollar(value):
    try:
        result = value / 2685
        return f"{result:.2f}"  # Format to 2 decimal places
    except (ValueError, ZeroDivisionError):
        return "0.00"
