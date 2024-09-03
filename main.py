import math


class ConversorAngulos:
    def __init__(self, valor: float):
        self.valor = valor

    def grados_a_radianes(self) -> float:
        """
        Convierte de grados sexagesimales a radianes.
        """
        return math.radians(self.valor)

    def radianes_a_grados(self) -> float:
        """
        Convierte de radianes a grados sexagesimales.
        """
        return math.degrees(self.valor)


def main():
    # Solicitar al usuario que ingrese el tipo de conversión
    tipo_conversion = input("Elija el tipo de conversión (1 para Grados a Radianes, 2 para Radianes a Grados): ")

    # Verificar el tipo de conversión seleccionado
    if tipo_conversion == "1":
        valor = float(input("Ingrese el valor en grados: "))
        conversor = ConversorAngulos(valor)
        resultado = conversor.grados_a_radianes()
        print(f"{valor} grados son {resultado} radianes")

    elif tipo_conversion == "2":
        valor = float(input("Ingrese el valor en radianes: "))
        conversor = ConversorAngulos(valor)
        resultado = conversor.radianes_a_grados()
        print(f"{valor} radianes son {resultado} grados")

    else:
        print("Opción no válida. Por favor, elija 1 o 2.")


if __name__ == "__main__":
    main()
