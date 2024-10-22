from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        if self.numerator == 0:
            return "0"
        elif self.numerator == self.denominator:
            return "1"
        elif self.numerator > self.denominator:
            whole_part = self.numerator // self.denominator
            remainder = self.numerator % self.denominator
            if remainder == 0:
                return f"{whole_part}"
            else:
                return f"{whole_part} {remainder}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"

# Exemplo de uso
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
result = fraction1.add(fraction2)
print(result)  # Saída esperada: 1 1/4