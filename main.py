from typing import List



def read_list() -> List[int]:
    '''
    Functia de citire a listei.
    :return: lista citita
    '''
    lst = []
    lst_str= input('Introduceti numerele separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def get_longest_prime_digits(lst: list[int]) -> List[int]:
    '''
    Functia determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt formate din cifre prime.
    :param list: lista de numere
    :return: cea mai lunga subsecventa
    '''


    n = len(lst)
    result= []
    for stanga in range(n):
        for dreapta in range(stanga, n):
            all_digit_prime = True
            for num in lst[stanga:dreapta+1]:
                if prime_digits(num) == False:
                    all_digit_prime = False
                    break
            if all_digit_prime == True:
                if dreapta - stanga + 1 > len(result):
                    result = lst[stanga:dreapta + 1]
    return result



def test_get_longest_prime_digits():
    '''
    Functia testeaza si returneaza cea mai lunga subsecventa de numere cu toate cifrele prime din lista introdusa.
    :return: subsecventa care indeplineste proprietatea
    '''
    assert get_longest_prime_digits([22, 35, 57, 65, 99, 555, 2345]) == [22, 35, 57]
    assert get_longest_prime_digits([84, 22, 35, 79, 99, 25, 68, 67, 2576798]) == [22, 35]
    assert get_longest_prime_digits([13, 25, 35, 57, 76]) == [25, 35, 57]
    assert get_longest_prime_digits([5723, 5555, 7372, 2375, 4567, 6789, 4567]) == [5723, 5555, 7372, 2375]


def prime_digits(n):
    '''
    Functia determina daca numarul are toate cifrele numere prime.
    :param n: numarul studiat
    :return: True daca numarul este format doar din cifre prime si False in caz contrar
    '''

    while n != 0:
        if n % 10 != 7 and n % 10 != 5 and n % 10 != 2 and n % 10 != 3:
            return False
        n = int(n / 10)
    return True

def test_prime_digits():
    '''
    Functia testeaza daca numarul este format doar din cifre prime.
    :return: 1 daca numarul indeplineste conditia si 0 in caz contrar
    '''
    assert test_prime_digits(22) == True
    assert test_prime_digits(35) == True
    assert test_prime_digits(46) == False

def get_longest_all_palindromes(lst: list[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    n=len(lst)
    result= []
    for stanga in range(n):
        for dreapta in range(stanga, n):
            all_num_palindroame = True
            for num in lst[stanga:dreapta+1]:
                if is_palindrome(num) == False:
                    all_num_palindroame = False
                    break
            if all_num_palindroame:
                if dreapta-stanga+1 > len(result):
                    result = lst[stanga:dreapta+1]
    return result

def test_get_longest_all_palindromes():
    '''
    Functia testeaza si returneaza cea mai lunga subsecventa de numere care sunt palindroame.
    :return: subsecventa care indeplineste proprietatea
    '''
    assert get_longest_all_palindromes([11, 121, 22, 23, 45, 111, 212]) == [11, 121, 22]
    assert get_longest_all_palindromes([1221, 393, 12, 141, 150,1001, 9889]) == [1221, 393]
    assert get_longest_all_palindromes([1567, 2345, 5775, 11, 232, 787, 22, 19]) == [5775, 11, 232, 787, 22]
    assert get_longest_all_palindromes([44, 191,1243,5453, 5436,3325, 333, 212, 909,1001]) == [333, 212, 909, 1001]


def is_palindrome(n) ->bool:
    '''
    Functia determina daca un numar este palindrom.
    :param n: numarul care trebuie studiat
    :return: True daca numarul este palindrom si False in caz contrar
    '''
    palindrom=0
    palindromcopie=n
    while n!=0:
        ultima=int(n%10)
        palindrom=palindrom*10+ultima
        n=int(n/10)
    if palindrom==palindromcopie:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(12) == False
    assert is_palindrome(1001) == True


def main():

    lst=[]
    while True:
        print('1.Citire lista')
        print('2.Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt palindroame.')
        print('3.Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt formate din cifre prime.')
        print('x Iesire.')
        optiune=input('Optiunea: ')
        if optiune == '1':
            lst= read_list()
        elif optiune == '2':
            print('Cea mai lunga subsecventa cu toate numerele palindroame este:', get_longest_all_palindromes(lst))
            test_get_longest_all_palindromes()
        elif optiune=='3':
            print('Cea mai lunga subsecventa cu toate numerele formate din cifre prime este:', get_longest_prime_digits(lst))
            test_get_longest_prime_digits()
        elif optiune=='x':
            break
        else:
            print('Optiune invalida.')

if __name__ == '__main__':
    main()
