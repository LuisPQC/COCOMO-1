# Datos de entrada
def entrada_datos():
    print("Seleccione el tipo de software:")
    print("1. Orgánico")
    print("2. Semi-acoplado")
    print("3. Acoplado")
    tipo_software = int(input("Ingrese el número correspondiente al tipo de software: "))
    
    loc = int(input("Ingrese el número de líneas de código (LOC): "))
    personas = int(input("Ingrese el número de personas que trabajarán en el proyecto: "))
    salario_por_persona = float(input("Ingrese el salario mensual por persona (Bs): "))
    horas_trabajo_por_mes = float(input("Ingrese las horas de trabajo mensuales por persona: "))
    
    return tipo_software, loc, personas, salario_por_persona, horas_trabajo_por_mes

# Función para calcular el factor de ponderación
def calcular_factor_ponderacion(tipo_software):
    if tipo_software == 1:
        return 2.4  # Factor para software Orgánico
    elif tipo_software == 2:
        return 3.0  # Factor para software Semi-acoplado
    elif tipo_software == 3:
        return 3.6  # Factor para software Acoplado
    else:
        print("Tipo de software inválido")
        return 0

# Cálculo del esfuerzo nominal
def calcular_esfuerzo_nominal(loc, factor_ponderacion):
    return loc * factor_ponderacion

# Cálculo del tiempo de desarrollo
def calcular_tiempo_desarrollo(esfuerzo, personas):
    return esfuerzo / personas

# Cálculo de la estimación de productividad
def calcular_productividad(loc, personas, tiempo_desarrollo):
    return loc / (personas * tiempo_desarrollo)

# Cálculo del costo de desarrollo
def calcular_costo(salario_por_persona, horas_trabajo_por_mes, tiempo_desarrollo, personas):
    return salario_por_persona * horas_trabajo_por_mes * tiempo_desarrollo * personas

# Función principal
def main():
    tipo_software, loc, personas, salario_por_persona, horas_trabajo_por_mes = entrada_datos()
    
    # Calcular el factor de ponderación
    factor_ponderacion = calcular_factor_ponderacion(tipo_software)
    
    # Calcular el esfuerzo nominal
    esfuerzo_nominal = calcular_esfuerzo_nominal(loc, factor_ponderacion)
    
    # Calcular el tiempo de desarrollo
    tiempo_desarrollo = calcular_tiempo_desarrollo(esfuerzo_nominal, personas)
    
    # Calcular la productividad estimada
    productividad = calcular_productividad(loc, personas, tiempo_desarrollo)
    
    # Calcular el costo de desarrollo
    costo = calcular_costo(salario_por_persona, horas_trabajo_por_mes, tiempo_desarrollo, personas)
    
    # Mostrar los resultados
    print("\nResultados:")
    print(f"Factor de Ponderación: {factor_ponderacion}")
    print(f"Esfuerzo Nominal: {esfuerzo_nominal} horas")
    print(f"Tiempo de Desarrollo: {tiempo_desarrollo} meses")
    print(f"Productividad Estimada: {productividad} LOC/persona/mes")
    print(f"Costo de Desarrollo: ${costo:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
