import io
import unittest
from contextlib import redirect_stdout
from print_diamond import print_diamond  # Ajuste o nome do módulo se necessário

class TestPrintDiamond(unittest.TestCase):
    
    def test_diamond_A(self):
        expected_output = "A\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            print_diamond('A')
            self.assertEqual(buf.getvalue(), expected_output)

    def test_diamond_B(self):
        expected_output = " A\nB B\n A\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            print_diamond('B')
            self.assertEqual(buf.getvalue(), expected_output)

    def test_diamond_C(self):
        expected_output = "  A\n B B\nC   C\n B B\n  A\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            print_diamond('C')
            self.assertEqual(buf.getvalue(), expected_output)

    def test_diamond_E(self):
        expected_output = (
            "    A\n"
            "   B B\n"
            "  C   C\n"
            " D     D\n"
            "E       E\n"
            " D     D\n"
            "  C   C\n"
            "   B B\n"
            "    A\n"
        )
        with io.StringIO() as buf, redirect_stdout(buf):
            print_diamond('E')
            self.assertEqual(buf.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

