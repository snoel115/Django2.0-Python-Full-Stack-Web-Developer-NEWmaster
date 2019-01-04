
# snoel practice filter=========================
from django import template
register = template.Library()

def cutThis(value, arg):
    """
    this cut out all value or "arg" from a string
    """
    return value.replace(arg, '')

register.filter('cut', cutThis)

# ============================================
