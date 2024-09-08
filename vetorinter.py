vetora = []
vetorb = []

def enter():
    print("write 10 element")
    for i in range(10):
        number = int(input(f"element {i+1}:"))
        vetora.append(number)
    
    print("write 10 element")
    for i in range(10):
        number = int(input(f"element {i+1}:"))
        vetorb.append(number)
    
    vetorinter = []
    for i in range(10):
        vetorinter.append(vetora[i])
        vetorinter.append(vetorb[i])

    print("\nResult vector of intercalation.")
    print(vetorinter)
    
enter()