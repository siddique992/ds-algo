def matrix_mul(A, B):
  mult = []
  for i in range(len(A)):
      mult.append([])
      for j in range(len(A[i])):
          for k in range(len(B)):
              for l in range(len(B[k])):
                  if j == k:
                      if len(mult[i])-1 < l:
                          mult[i].append(A[i][j] * B[k][l])
                      else:
                          mult[i][l] += A[i][j] * B[k][l]

  return mult

if __name__ == '__main__':
    A = [[1, 3, 4],
        [2, 5, 7],
        [5, 9, 6]]
    B = [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]
    mult = matrix_mul(A, B)
    print(mult)

    out1 = [[1], 
        [0, 5],
        [0, 0, 6]]

    out2 = [[1, 3, 4],
        [2, 5, 7],
        [5, 9, 6]]
