from django import template


register = template.Library()

censor_list = ['блять', 'Блять', 'ебать', 'Ебать', 'хуй', 'Хуй',]


@register.filter()
def censor(word):
    if isinstance(word, str):
        for a in word.split():
            if a in censor_list:
                word = word.replace(a[1:-1], '*' * (len(a) - 2))
    else:
        raise ValueError('censored')
    return word