n=[int(x) for x in raw_input().split(" ")]
for i in range(len(n)-2):
    if n[i]+n[i+1]!=n[i+2]:
        print("No sequence found!!")
        break
    if i== len(n)-3:print("Sequence found")
    

        