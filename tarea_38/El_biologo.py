#Algoritmo del biólogo

from difflib import SequenceMatcher #Importamos la libreria necesaria

print("Introduce la primera secuencia de ADN: ")
Secuencia_ADN_1 = input()

print("Introduce la SEGUNDA secuencia de ADN: ")
Secuencia_ADN_2 = input()

match = SequenceMatcher(None, Secuencia_ADN_1, Secuencia_ADN_2).find_longest_match(0, len(Secuencia_ADN_1), 0, len(Secuencia_ADN_2))
print(Secuencia_ADN_1[match.a: match.a + match.size])
