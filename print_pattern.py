"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# rows = 5
#
# for i in range(1, rows + 1):
#
#     for j in range(1, i + 1):
#        print(j, end= ' ')
#
#     print('')






# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")