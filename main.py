from math_function import add, mul, div

def get_input(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Input harus berupa bilangan bulat. Silahkan coba lagi.")

def get_operator():
    while True:
        operator = input("Masukkan operator (+, *, /): ")
        if operator in ["+", "*", "/"]:
            return operator
        else:
            print("Operator tidak valid. Silahkan coba lagi.")

def calculate(data_1, data_2, operator):
    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":
        result = mul(data_1, data_2)
    elif operator == "/":
        if data_2 == 0:
            result = "Error: Pembagian dengan nol!"
        else:
            result = div(data_1, data_2)
    else:
        result = "Operator Tidak Valid"

    return result

def main():
    data_1 = get_input("Masukkan input 1: ")
    data_2 = get_input("Masukkan input 2: ")
    operator = get_operator()

    result = calculate(data_1, data_2, operator)

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))

if __name__ == "__main__":
    print("Hello Main!")
    main()
