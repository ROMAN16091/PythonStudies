import numpy as np

arr1 = np.random.randint(1, 15,[5,5])
arr2 = np.random.randint(1, 15, [5,5])
print(arr1)
print()
print(arr2)
print(np.sum(arr1))
print(np.sum(arr2))
print(f'Сума різниці: {(arr2 - arr1).sum()}')
print()
print(f'Масив різниці: {(arr2 - arr1)}')
print()
print(arr1 * arr2)
print()
print(arr1 ** arr2)
print()
print()


black_row = np.array([[0,1,0,1]])
white_row = np.array([[1,0,1,0]])
black_cells = np.vstack([black_row, white_row] * 2)
white_cells = np.vstack([white_row, black_row] * 2)
chess_board = np.concatenate((black_cells, white_cells), axis=0)
chess_board = np.hstack([chess_board] * 2)
print(chess_board)
print()
print(chess_board[2])
print()
print(chess_board[:, 4:5])
print(chess_board[0:3, 0:3])


from PIL import Image

img = Image.open('image.jpg')

arr_img = np.array(img)
print()
print()
R, G, B = arr_img[:, :, 0], arr_img[:, :, 1], arr_img[:, :, 2]
print(f'Середнє: {R.mean()}\n'
      f'Максимальне: {R.max()}\n'
      f'Мінімальне: {R.min()}\n')
print(f'Середнє: {G.mean()}\n'
      f'Максимальне: {G.max()}\n'
      f'Мінімальне: {G.min()}\n')
print(f'Середнє: {B.mean()}\n'
      f'Максимальне: {B.max()}\n'
      f'Мінімальне: {B.min()}\n')


pixels_intensity_sum = arr_img.sum()
print(pixels_intensity_sum)
print()
print(arr_img/arr_img.max())
