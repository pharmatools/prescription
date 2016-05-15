from prescription import is_quantity, Prescription
from nose.tools import assert_true, assert_false, assert_equal, assert_not_equal, raises
import unittest


def test_is_quantity():
    assert_true(is_quantity('10'))
    assert_true(is_quantity('10mg'))
    assert_false(is_quantity('ibuprofen'))


class TestPrescription(unittest.TestCase):
    @staticmethod
    def gen_prescription():
        return Prescription(drug="tylenol",
                            amount=5,
                            unit="mg",
                            frequency="qid")

    def test_str(self):
        assert_equal(str(TestPrescription.gen_prescription()),
                     "5mg of tylenol for qid")

    def test_equal(self):
        assert_equal(TestPrescription.gen_prescription(),
                     TestPrescription.gen_prescription())
        assert_not_equal(TestPrescription.gen_prescription(),
                         Prescription(drug="tylenol",
                                      amount=6,
                                      unit="mg",
                                      frequency="qid"))

    @raises(ValueError)
    def test_unit_match(self):
        TestPrescription.gen_prescription() > Prescription(drug="tylenol",
                                                           amount=5,
                                                           unit="g",
                                                           frequency="qid")
