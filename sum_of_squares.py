from abc import ABC, abstractmethod


# def recursive_sum_of_positive_square(numbers):
#     if not numbers:
#         return 0
#     if numbers[0]>0:
#         return recursive_sum_of_positive_square(numbers[1:]) + numbers[0] * numbers[0]
#     else:
#         return recursive_sum_of_positive_square(numbers[1:])


class IRecursiveMethods(ABC):
    @abstractmethod
    def sum_of_positive_squares(self, numbers):
        pass

class RecursiveMethods(IRecursiveMethods):
    def sum_of_positive_squares(self, numbers):
        if not numbers:
            return 0
        if numbers[0] > 0:
            return self.sum_of_positive_squares(numbers[1:]) + numbers[0] * numbers[0]
        else:
            return self.sum_of_positive_squares(numbers[1:])


def get_numbers_array(numbers):
    strings_array=numbers.split(' ')
    int_array = recursive_cast(strings_array)
    return int_array

def recursive_cast(arr):
    if not arr:
        return []
    return [int(arr[0])] + recursive_cast(arr[1:])

def recursive_data_request_and_process(recursive:IRecursiveMethods, data):
    if not data:
        return []
    number_of_numbers = int(input("").strip())
    numbers = input("").strip()
    int_numbers = get_numbers_array(numbers)
    return [recursive.sum_of_positive_squares(int_numbers)] + recursive_data_request_and_process(recursive, data[1:])

def recursive_print(result):
    if not result:
        return
    print(result[0])
    recursive_print(result[1:])

def main():
    number_of_tests = int(input("").strip())
    recursive_methods = RecursiveMethods()
    if 1<=number_of_tests<=100:
        data = [0]*number_of_tests
        result = recursive_data_request_and_process(recursive_methods, data)
        recursive_print(result)


if __name__== "__main__":
    main()