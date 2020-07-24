from django import template

register = template.Library()


# this function cuts the arg from the value string.
# we can also use decorator which i have studied in py level 2 int the place of calling register.filter() separately.

@register.filter(name = 'cut1')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('cut1',cut) # here 1st arg is the name from which this operation is to be performed and
                            # the 2nd arg is the function name
