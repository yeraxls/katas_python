# Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
#  - Un Anagrama consiste en formar una palabra reordenando TODAS
#  las letras de otra palabra inicial.
#  - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.



def is_anagram(word1:str, word2:str) -> bool:
    if len(word1) != len(word2):
        return False
    letters = [i for i in word1 if i not in word2]
    if len(letters) > 0:
        return False
    return True


result = is_anagram("hola","alvh")
print(result)