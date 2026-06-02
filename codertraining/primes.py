def check_if_prime(number):
    is_prime = True
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            is_prime = False
    return is_prime

def goldbach(even_number):
    list_of_primes = []
    primes = [x for x in range(even_number) if check_if_prime(x)]
    # print(primes)
    # return primes
#     for i in range(even_number):
#         for j in range(i+1, even_number):
#             list_of_primes.append([i, j])
#     return list_of_primes
    print(primes)
    pass


print(goldbach(10))
# test.assert_equals(goldbach(2),[])
# test.assert_equals(goldbach(4),[[2,2]])
# test.assert_equals(goldbach(6),[[3,3]])
# test.assert_equals(goldbach(8),[[3,5]])