x = int(input("Введіть значення x: ")) 
y = int(input("Введіть значення y: "))
z = int(input("Введіть значення z: "))

step1 = y and z 
print("Перша дія y ∧ z: ")
print("Результат першої дії: ", int(step1))

step2 = not y or not z
print("Друга дія ¬y ∨ ¬z: ")
print("Результат другої дії: ", int(step2))

step3 = (x == step1)
print("Третя дія x⇔(y ∧ z):")
print("Результат третьої дії: ", int(step3))

step4 = (x == step2)
print("Четверта дія x⇔(¬y ∨ ¬z):")
print("Результат четвертої дії: ", int(step4))

step5 = (step3 == step4)
print("П'ята дія (x⇔¬y ∨ ¬z)⇔(x⇔y ∨ z):")
print("Результат п'ятої дії: ", int(step5))

print()
print("Таблиця істинності")
print(" x | y | z | y∧z | ¬y∨¬z| (x⇔¬y∨¬z) | (x⇔y∧z) | Результат")
print("-" * 70)

for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            d = b and c
            e = (not b) or (not c) 
            f = (a == d)
            g = (a == e)
            h = (f == g)
            print(f"  {a} | {b} | {c} |   {int(d)}   |  {int(e)}  |     {int(f)}     |    {int(g)}    |    {int(h)}")

print()
print("Висновок: програма перевіряє формулу (x⇔¬y∨¬z)⇔(x⇔y∧z)")