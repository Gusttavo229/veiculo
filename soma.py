class Calculadora:
    @staticmethod
    def somar(a, b):
        try:
            return a + b
        except TypeError:
            return None

# Exemplos de uso:
calc = Calculadora()

# Somando dois números inteiros
resultado_int = calc.somar(5, 3)
print("Soma de inteiros:", resultado_int)  # Saída: 8

# Somando duas strings
resultado_str = calc.somar("Olá, ", "mundo!")
print("Concatenação de strings:", resultado_str)  # Saída: Olá, mundo!


