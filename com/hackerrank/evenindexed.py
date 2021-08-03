
if __name__ == '__main__':

    print("enter no of test cases")
    num_test_cases = int(input())

    for i in range(num_test_cases):
        test_string = input()
        even_indexed_Character = ''
        odd_indexed_character = ''
        for j in range (len(test_string)):
            if j % 2 == 0:
                even_indexed_Character += test_string[j]
            else:
                odd_indexed_character += test_string[j]
        print("{} {}".format(even_indexed_Character,odd_indexed_character))


