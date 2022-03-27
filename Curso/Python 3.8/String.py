nome: str = 'José Victor'

# Antes
print(f"nome = '{nome}'")

# Agora - ótimo para debbugar
print(f'{nome = }')
print(f'{nome.upper()[::-1] = }')