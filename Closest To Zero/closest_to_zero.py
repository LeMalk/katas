def closest_to_zero(numbers):
    if not numbers:
        return None
    
    closest = numbers[0]
    for num in numbers:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest

def closest_to_zero_word(words):
    target = "zero"
    target_set = set(target)
    
    def is_close(word):
        return set(word) == target_set
    
    def similarity(word):
        return sum(1 for a, b in zip(word, target) if a == b)
    
    closest_word = None
    for word in words:
        if is_close(word):
            if (closest_word is None or
                len(word) < len(closest_word) or
                (len(word) == len(closest_word) and similarity(word) > similarity(closest_word))):
                closest_word = word
    return closest_word

# Exemplos de uso
numbers = [6, -9, 15, -2, 2, 11]
print(closest_to_zero(numbers))  # Saída esperada: 2

words = ["rez", "zero", "zreo", "eorz", "zore"]
print(closest_to_zero_word(words))  # Saída esperada: "zero"