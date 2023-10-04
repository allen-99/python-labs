import random

def minor(array, i, j):
  c = array
  c = c[:i] + c[i+1:]
  for k in range(0,len(c)):
      c[k] = c[k][:j]+c[k][j+1:]
  return c

def det(array, n):
  if n == 1 :return array[0][0]
  if n == 2 :return array[0][0]*array[1][1] - array[0][1]*array[1][0]
  sum = 0
  for i in range(0,n):
      m = minor(array,0,i)
      sum =sum + ((-1)**i)*array[0][i] * det(m,n-1)
  return sum

n = int(input("Введите n: "))
m = int(input("Введите m: "))

a = [random.choices(range(0,100), k=n) for _ in range(m)]

print('Исходная матрица:')
for row in a:
  print(row)

a_trans = [[a[k][i] for k in range(m)] for i in range(n)]

print('Транпонированная матрица:')
for row in a_trans:
  print(row)

if (n != m):
  print('Невозможно найти определитель')
else:
  print('Определитель исходной матрицы: ', det(a, n))
  print('Определитель транпонированной матрицы: ', det(a_trans, n))

