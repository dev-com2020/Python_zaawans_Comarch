from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(repr(str).replace('\n','<br>\n'))
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner +'</li>\n</ul>'





htmlize({1, 2, 3})
htmlize(abs)
#print(htmlize('Programowanie w HTML \n - ale i w Python'))
print(htmlize(40))
# print(htmlize(['kolory', 66, {3, 2, 1}]))
