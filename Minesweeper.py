def game_field():
    row_column = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9], 4: [1, 2, 3, 4, 5, 6, 7, 8, 9], \
                  5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9], 7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], \
                  9: [1, 2, 3, 4, 5, 6, 7, 8, 9]}

    for key in row_column.keys():
        while True:
            for number in row_column[key]:
                print("({key}, {number})".format(key=key, number=number), end=" ")
            
            print("\n")
            break
game_field()