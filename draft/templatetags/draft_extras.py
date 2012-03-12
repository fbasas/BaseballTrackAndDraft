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

@register.filter(name='prev')
def prev(activePage):
    if int(activePage) == 1:
        return 1
    else:
        return int(activePage) - 1

@register.filter(name='next')
def next(activePage, totalPages):
    if int(activePage) == int(totalPages):
        return int(activePage)
    else:
        return int(activePage) + 1
