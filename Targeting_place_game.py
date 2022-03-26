# Targeting The Place Game.

row1 = [" 1 ", " 2 ", " 3 "]
row2 = [" 4 ", " 5 ", " 6 "]
row3 = [" 7 ", " 8 ", " 9 "]
row_map = [row1, row2, row3]
target = input("Please enter target Column and row number")
colno = int(target[0])-1
rowno = int(target[1])-1
# newword = map[rowno][colno]
row_map[rowno][colno]= "X"
print(f"{row1}\n{row2}\n{row3}")