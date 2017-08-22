from unittest import expectedFailure

from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ChrTests(TranspileTestCase):
    def test_int(self):
        self.assertCodeExecution("print(chr(40))")

    @expectedFailure
    def test_int_too_small(self):
        self.assertCodeExecution("print(chr(-1))")

    @expectedFailure
    def test_int_too_large(self):
        self.assertCodeExecution("print(chr(260))")


class BuiltinChrFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    function = "chr"

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_list',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]
