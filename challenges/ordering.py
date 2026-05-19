unordered_numbers = [12, 3, 4, 45, 89, 23, 56, 103, 5]

# def get_max(numbers:list)->int:
#      for digit in numbers:
#          if digit <= numbers[0]:
#              continue
#          else:
#              return digit


# def get_max(numbers:list)->int:
#     max_number = numbers[0]
#     for digit in numbers:
#         if max_number > digit:
#             pass
#         else:
#             max_number = digit
#     return max_number

def get_max(numbers:list)->int:
    max_number = 0
    for digit in numbers:
        if digit > max_number:
            max_number = digit
    return max_number

print(get_max(unordered_numbers))
