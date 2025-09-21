import time

def elegir_alfabeto():
    print("Elige un alfabeto:")
    print(" 1) Dígitos (0-9)")
    print(" 2) Letras minúsculas (a-z)")
    print(" 3) letras mayusculas (A-Z)")
    print(" 4) Minúsculas + dígitos")
    print(" 5) mayusculas + digitos")
    print(" 6) Minúsculas + mayúsculas + dígitos")
    print(" 7) todo + simbolos")
    case = input("Opción (1-7): ").strip()

    if case == "1":
        return "0123456789"
    if case == "2":
        return "qwertyuiopasdfghjklñzxcvbnm"
    if case == "3":
        return "QWERTYUIOPASDFGHJKLÑZXCVBNM"
    if case == "4":
        return "qwertyuiopasdfghjklñzxcvbnm0123456789"
    if case == "5":
        return "QWERTYUIOPASDFGHJKLÑZXCVBNM0123456789"
    if case == "6":
        return "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0123456789"
    if case == "7":
        return input("para lo simbolos elija los simbolos a utilizar (;:,.-_@!""''$%&/)")
    print("Opción no válida, usando letras minúsculas por defecto.")
    return "abcdefghijklmnopqrstuvwxyz"

def intentar_alfabeto_odometro(password, alphabet, max_len):
    base = len(alphabet)
    attempts = 0
    start = time.time()

    for length in range(1, max_len + 1):
        indices = [0] * length
        finished = False
        while not finished:
        
            guess = "".join(alphabet[i] for i in indices)
            attempts += 1
            if guess == password:
                elapsed = time.time() - start
                print("\n=== Contraseña encontrada ===")
                print("Contraseña:", guess)
                print("Intentos:", attempts)
                print(f"Tiempo: {elapsed:.4f} segundos")
                return True
            pos = length - 1
            while pos >= 0:
                if indices[pos] < base - 1:
                    indices[pos] += 1
                    break
                else:
                    indices[pos] = 0
                    pos -= 1
            if pos < 0:
                finished = True  

    elapsed = time.time() - start
    print("\nNo se encontró la contraseña con el alfabeto y longitudes probadas.")
    print("Intentos:", attempts)
    print(f"Tiempo: {elapsed:.4f} segundos")
    return False

def main():
    print("=== Demo fuerza bruta muy simple (educativa) ===")
    password = input("Introduce la contraseña a adivinar: ").strip()
    alphabet = elegir_alfabeto()


    faltantes = set(password) - set(alphabet)
    if faltantes:
        print("\nATENCIÓN: la contraseña tiene caracteres fuera del alfabeto elegido:", "".join(sorted(faltantes)))
        respuesta = input("¿Deseas añadir esos caracteres al alfabeto para buscarlos? (s/N): ").strip().lower()
        if respuesta == "s":
            alphabet += "".join(faltantes)
            print("Alfabeto ampliado.")
        else:
            print("Continuando, pero no se encontrará la contraseña si falta algún carácter.")


    max_len_input = input(f"Longitud máxima a probar (por defecto = {len(password)}): ").strip()
    try:
        max_len = int(max_len_input) if max_len_input else len(password)
        if max_len < 1:
            max_len = len(password)
    except ValueError:
        max_len = len(password)

    print("\nIniciando... (presiona Ctrl+C para detener si tarda demasiado)\n")
    try:
        intentar_alfabeto_odometro(password, alphabet, max_len)
    except KeyboardInterrupt:
        print("\nProceso detenido por el usuario.")

if __name__ == "__main__":

    main()
