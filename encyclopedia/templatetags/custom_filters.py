from django import template
import markdown2

register = template.Library()


@register.filter(name='markdown_to_html')
def markdown_to_html(value):
    html_output = markdown2.markdown(value)
    return html_output
