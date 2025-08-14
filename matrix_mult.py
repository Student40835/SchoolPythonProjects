#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 8/13/2025
#Description: 1 a function named dot_prod that takes two lists of numbers (vectors) as arguments and returns their dot product
# and 2 a function named dot_prod that takes two lists of numbers (vectors) as arguments and returns their dot product
def dot_prod(vector_list_1, vector_list_2):
    loops = 0
    dot_actual_product = 0
    dot_product = []
    while loops < len(vector_list_1):
        dot_product.append(vector_list_1[loops] * vector_list_2[loops])
        loops += 1
    for item in dot_product:
        dot_actual_product += item
    return dot_actual_product



def matrix_mult(matrix_1,matrix_2):
    matrix_3 = []
    starter = 0
    starter_2 = 0
    starter_0 = 0
    b_colum_matrixes = []
    for column_of_b in matrix_2[starter]:
        b_colum_matrixes.append([])
        for row_of_b in matrix_2:
            b_colum_matrixes[starter_0].append(matrix_2[starter][starter_0])
            starter += 1
        starter = 0
        starter_0 += 1
    starter_0 = 0
    for lists in matrix_1:
        matrix_3.append([])
        for column in range(len(matrix_2[starter])):
            matrix_3[starter_0].append(dot_prod(lists, b_colum_matrixes[starter_2]))
            starter_2 += 1
        starter_0 += 1
        starter_2 = 0
    return matrix_3