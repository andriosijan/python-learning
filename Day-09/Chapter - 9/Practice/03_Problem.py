# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. place these files in a folder for 13 - years old.

for x in range(2,21):
    table = ''

    for y in range(1,11):
        table += f"{x} X {y} = {x*y}\n"
    with open(f"tables/table_{x}.txt","w") as f:
        f.write(table)

