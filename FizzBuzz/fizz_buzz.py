def fizzbuzz_extended():
    number = 1
    while True:
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        if number % 7 == 0:
            output += "Whizz"
        if number % 11 == 0:
            output += "Bang"

        if output == "":
            output = str(number)

        print(output)

        # Parar quando encontrar "FizzBuzzWhizzBang"
        if output == "FizzBuzzWhizzBang":
            break

        number += 1

# Executa o programa FizzBuzz
fizzbuzz_extended()
