import re

# Função que encontra o intervalo da parte selecionada do nome do arquivo
def find_selection_range(filename):
    # Palavras-chave e extensões a serem preservadas
    keywords = ['test', 'tests', 'spec', 'step']
    
    # Extrair a extensão do arquivo
    base_name = filename.rsplit('/', 1)[-1]  # Retira o diretório, se houver
    name, ext = re.split(r'(\.[^\.]+$)', base_name)[0], re.split(r'(\.[^\.]+$)', base_name)[1:]
    ext = ext[0] if ext else ''  # Extensão se existir
    
    # Localizar keywords
    keyword_pattern = re.compile(rf'\b({"|".join(keywords)})\b', re.IGNORECASE)
    
    # Se o arquivo estiver em um diretório, queremos manter essa parte
    if '/' in filename:
        name_with_path = filename.rsplit('/', 1)[0]
        dir_offset = len(name_with_path) + 1  # Compensar o diretório com "/"
    else:
        dir_offset = 0
    
    # Se houver keyword, selecionamos até essa palavra e qualquer separador
    match = keyword_pattern.search(name)
    if match:
        keyword_end = match.end()
        # Manter caracteres separadores após a keyword
        while keyword_end < len(name) and name[keyword_end] in ['_', '-', '.']:
            keyword_end += 1
        return (dir_offset, dir_offset + match.start())
    
    # Caso contrário, selecionamos tudo antes da extensão
    return (dir_offset, dir_offset + len(name))

# Função de testes usando JSON
test_data = {
    "src/Hiker_spec.re": [4, 9],
    "test/hiker_test.exs": [5, 10],
    "wibble/test/hiker_spec.rb": [12, 17],
    "hiker_steps.rb": [0, 5],
    "hiker_spec.rb": [0, 5],
    "test_hiker.rb": [5, 10],
    "test_hiker.py": [5, 10],
    "test_hiker.sh": [5, 10],
    "tests_hiker.sh": [6, 11],
    "test_hiker.coffee": [5, 10],
    "hiker_spec.coffee": [0, 5],
    "hikerTest.chpl": [0, 5],
    "hiker.tests.c": [0, 5],
    "hiker_tests.c": [0, 5],
    "hiker_test.c": [0, 5],
    "hiker_Test.c": [0, 5],
    "HikerTests.cpp": [0, 5],
    "hikerTests.cpp": [0, 5],
    "HikerTest.cs": [0, 5],
    "HikerTest.java": [0, 5],
    "DiamondTest.kt": [0, 7],
    "HikerTest.php": [0, 5],
    "hikerTest.js": [0, 5],
    "hiker-test.js": [0, 5],
    "hiker-spec.js": [0, 5],
    "hiker.test.js": [0, 5],
    "hiker.tests.ts": [0, 5],
    "hiker_tests.erl": [0, 5],
    "hiker_test.clj": [0, 5],
    "fizzBuzz_test.d": [0, 8],
    "hiker_test.go": [0, 5],
    "hiker.tests.R": [0, 5],
    "hikertests.swift": [0, 5],
    "HikerSpec.groovy": [0, 5],
    "hikerSpec.feature": [0, 5],
    "hiker.feature": [0, 5],
    "hiker.fun": [0, 5],
    "hiker.t": [0, 5],
    "hiker.plt": [0, 5],
    "hiker": [0, 5],
}

# Função para rodar os testes
def run_tests():
    for filename, expected_range in test_data.items():
        result = find_selection_range(filename)
        assert result == tuple(expected_range), f"Failed for {filename}: Expected {expected_range}, got {result}"
    print("All tests passed!")

# Executar os testes
run_tests()
