def reverse_matrix(M):
    M.reverse()
    for row in M:
        row.reverse()

M = [[1, 2],
     [3, 4],
     [5, 6]]

#M is mutable

reverse_matrix(M)
print(M)