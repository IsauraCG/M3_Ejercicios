list_of_list = [[0, 2, 4, 5], [4, 5, 6], [7, 0, 8]]
list_without_zeros = list(filter(lambda x: x[0] != 0, list_of_list))
final_list = list(filter(lambda x: x != 0, [
                  item for sublist in list_without_zeros for item in sublist]))
print(final_list)
