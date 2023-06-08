from django.test import TestCase

# Create your tests here.
r = 'это тестовое слово'

for i in r.split():
    if i == 'тестовое':
        r = r.replace(i, '*')

print(r)

