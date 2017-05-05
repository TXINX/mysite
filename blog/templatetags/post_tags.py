#coding=utf8
from django import template  

register = template.Library()  

@register.filter
def abstract(value, length='100'):  
    import re
    result = re.search("^.{"+length+",}?\n|^(?:.*?\n){3}", value, re.DOTALL)

    return result.group()+"......" if result else value

@register.filter
def rprint(value, num_spaces=4):
    print repr(value)
    return value#.replace('\n', '\n' + '\t'*num_spaces)