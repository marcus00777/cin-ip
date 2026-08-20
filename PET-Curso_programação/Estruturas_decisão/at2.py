A, B, C, D, E, F = True, False, 10.0, 2, "True", 10

resposta1 = A and B
print(f"A and B: {resposta1}")

resposta2 = A or B
print(f"A or B: {resposta2}")

resposta3 = (A and B) or A
print(f"(A and B) or A: {resposta3}")

resposta4 = (A and B) or B
print(f"(A and B) or B: {resposta4}")

resposta5 = A and (B or A)
print(f"A and (B or A): {resposta5}")

resposta6 = B or (not B and A)
print(f"B or (not B and A): {resposta6}")

resposta7 = C == F
print(f"C == F: {resposta7}")

resposta8 = A == E
print(f"A == E: {resposta8}")

resposta9 = A != E
print(f"A != E: {resposta9}")

resposta10 = (C != F) or (A != E)
print(f"(C != F) or (A != E): {resposta10}")

resposta11 = (C == F) or (A == E)
print(f"(C == F) or (A == E): {resposta11}")

resposta12 = C/5 == D
print(f"C/5 == D: {resposta12}")

resposta13 = C/5 > D
print(f"C/5 > D: {resposta13}")

resposta14 = C/5 < D
print(f"C/5 < D: {resposta14}")

resposta15 = C/5 <= D
print(f"C/5 <= D: {resposta15}")

resposta16 = (C/5 > D) or (not A)
print(f"(C/5 > D) or (not A): {resposta16}")

resposta17 = (C/5 > D) or (not B)
print(f"(C/5 > D) or (not B): {resposta17}")