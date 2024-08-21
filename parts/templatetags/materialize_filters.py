from django import template

register = template.Library()

@register.filter(name='as_materialize')
def as_materialize(field):
    return field.as_widget(attrs={"class": "materialize-class"})