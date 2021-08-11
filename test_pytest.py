import Tarea_micros as tm
import random

''' It is expected from methods ending in _true to pass,
and from methods ending in _false to fail
'''


def test_multiple_op_true():
    num = random.randrange(10)  # number from 0 to 9
    assert tm.multiple_op(num)[0] == 0, 'Error: Se esperaba un entero'


def test_multiple_op_false():
    assert tm.multiple_op('a')[0] == 0, 'E001: Se esperaba un entero'


def test_verify_array_op_true():
    lista = []
    for i in range(3):
        lista.append(random.randrange(10))
    assert tm.verify_array_op(lista)[0] == 0, 'Error: No es lista de enteros'


def test_verify_array_op_false():
    lista = ['a', 'b', 1]
    assert tm.verify_array_op(lista)[0] == 0, 'Error: No es lista de enteros'
