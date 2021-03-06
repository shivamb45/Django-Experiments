from django import template

#register the filter
register = template.Library()

def cutversion2(value,arg):
    """
    This actually is a replica of cut filter already present there

    """

    return value.replace(arg,'$$')

#register the filter and specify the calling name and calling function name
register.filter('cutV2',cutversion2)

@register.filter(name='splitItBy')
def forDecoratorsSake(value,arg):
    """
    This is actually a dummy function | filter just to use and try Decorator
    """

    return value.split(arg)
