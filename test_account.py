import pytest

from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Jane')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(30.50) is True
        assert self.p1.get_balance() == pytest.approx(30.50, abs=0.001)

        assert self.p1.deposit(-30) is False
        assert self.p1.get_balance() == pytest.approx(30.50, abs=0.001)

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == pytest.approx(30.50, abs=0.001)

    def test_withdraw(self):
        assert self.p1.deposit(50.50) is True
        assert self.p1.get_balance() == pytest.approx(50.50, abs=0.001)

        assert self.p1.withdraw(100) is False
        assert self.p1.get_balance() == pytest.approx(50.50, abs=0.001)

        assert self.p1.withdraw(20) is True
        assert self.p1.get_balance() == pytest.approx(30.50, abs=0.001)

        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(30.50, abs=0.001)
