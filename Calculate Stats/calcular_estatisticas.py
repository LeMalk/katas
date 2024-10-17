def calcular_estatisticas(sequencia):
    """
    Calcula estatísticas básicas de uma sequência de números.
    Args:
        sequencia (list): Uma lista de números.
    Returns:
        dict: Um dicionário contendo as seguintes estatísticas:
            - "valor_minimo" (float): O menor valor na sequência.
            - "valor_maximo" (float): O maior valor na sequência.
            - "numero_elementos" (int): O número de elementos na sequência.
            - "valor_medio" (float): A média dos valores na sequência.
        Se a sequência estiver vazia, retorna a mensagem "A sequência está vazia".
    """
    if not sequencia:
        return "A sequência está vazia"
    
    valor_minimo = min(sequencia)
    valor_maximo = max(sequencia)
    numero_elementos = len(sequencia)
    valor_medio = sum(sequencia) / numero_elementos
    
    return {
        "valor_minimo": valor_minimo,
        "valor_maximo": valor_maximo,
        "numero_elementos": numero_elementos,
        "valor_medio": valor_medio
    }

# Exemplo de uso
sequencia = [6, 9, 15, -2, 92, 11]
estatisticas = calcular_estatisticas(sequencia)
print(estatisticas)