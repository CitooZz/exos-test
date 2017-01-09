from django.template import Library

register = Library()


@register.filter
def eligible(user):
    if user.age > 13:
        return 'allowed'

    return 'blocked'


@register.filter
def bizzfuzz(user):
    random_number = user.random_number

    if random_number % 5 == 0 and random_number % 3 == 0:
        return 'BizzFuzz'

    elif random_number % 3 == 0:
        return 'Bizz'

    elif random_number % 5 == 0:
        return 'Fuzz'

    else:
        return random_number
