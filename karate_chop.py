def karate_chop(target, nums):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = nums[mid]
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def main():
    print("Bienvenido a la aplicacion de busqueda binaria (Karate Chop)")

    # Ingreso de la lista de números
    nums_input = input("Ingrese una lista de numeros ordenados separados por comas: ")
    nums = list(map(int, nums_input.split(',')))

    # Ingreso del número objetivo a buscar
    target = int(input("Ingrese el numero que desea buscar: "))

    # Llamada a la función karate_chop
    result = karate_chop(target, nums)

    # Mostrar el resultado
    if result != -1:
        print(f"El numero {target} se encuentra en la posicion {result}.")
    else:
        print(f"El numero {target} no se encuentra en la lista.")

if __name__ == "__main__":
    main()
