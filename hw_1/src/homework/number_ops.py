def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n #caso base
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2) #perchè il passo n-esimo è proprio la somma dei numeri calcolati agli ultimi due passi che lo precedono


def sum_of_digits_recursive(num: int) -> int:
    if num == 0:
        return 0 #caso base
    else:
        return (num % 10) + sum_of_digits_recursive(num // 10)


def is_palindrome_number(num: int) -> bool:
    num_str = str(num) #cast
    return num_str == num_str[::-1] #faccio il confronto con la stringa invertita
