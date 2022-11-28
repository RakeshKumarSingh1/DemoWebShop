import pytest


class TestCalculator:
    a=6
    b=2

    @pytest.mark.skipif(reason="simply to check")
    def test_add(self):
        assert  self.a + self.b == 8, "invalid output"

    def test_div(self):
        assert self.a/self.b == 3,    "invalid division"


class TestCalculator1:
    a = 6
    b = 2

    @pytest.mark.skipif(b==2,reason="simply to check")
    def test_add(self):
        assert self.a + self.b == 8, "invalid output"

    def test_div(self):
        assert self.a / self.b == 3, "invalid division"