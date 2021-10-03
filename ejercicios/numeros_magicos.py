"""
El profesor Xyoby del área de matemáticas está pidiendo tu ayuda para
encontrar números mágicos. Un número mágico (N) es aquel que la suma de
todos los numeros primos entre 1 y N (incluyendo N) es divisible entre
3. Para encontrar dichos números ustedes deben hacer un programa el
cual reciba un número N y de como respuesta si el número es mágico o
no.
- La entrada es un número positivo.
- Si el total de la suma de números primos es divisible entre 3,
    deberías de imprimir el resultado de la suma y 'El número es
    mágico'
- Si el total de la suma de números primos no es divisible entre 3,
    deberías de imprimir el resultado de la suma y 'El número no es
    mágico'
- Recordar que el número 1 no es primo.

Ejemplo:

    Input:
    N: 10

    Output:
    17
    El numero es magico

Explicación: Los números primos que se encuentran dentro del rango 1 a
    10 son 2, 3, 5, 7. Estos números se suman y dan como resultado 17.
    Si se divide 17 entre 3 da como residuo 2, por lo que no es un
    número mágico.

TODO: add testcases.
"""

# Mejores implementaciones de la función es_primo en:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
def es_primo(n: int) -> bool: 
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    total = []
    N = int(input("N: "))
    for x in range(N+1):
        if es_primo(x):
            total.append(x)
    resultado = sum(total)
    print(resultado)
    if resultado % 3 == 0:
        print("El número es mágico")
    else:
        print("El número no es mágico")


def main_alt():
    N = int(input("N: "))
    R = sum([x for x in range(N+1) if es_primo(x)])
    print(R)
    print("El número es mágico" if R % 3 == 0 else "El número no es mágico")


if __name__ == "__main__":
    main()