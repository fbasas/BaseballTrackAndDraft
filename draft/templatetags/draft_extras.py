from django import template

register = template.Library()

@register.filter(name='getVal')
def getVal(line, columnConfig):
    attrList = columnConfig[1].split('.')
    val = line
    for attr in attrList:
        val = getattr(val, attr)

    if len(columnConfig) == 3:
        formatStr = "%(num)." + str(columnConfig[2]) + "f"
        return formatStr % {'num' : val}
    else:
        return val

@register.filter(name='getHeader')
def getHeader(columnConfig):
    return columnConfig[0]
