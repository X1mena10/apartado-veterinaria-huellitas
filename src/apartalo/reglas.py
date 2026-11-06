def calcular_total_cita(consultas: list, vacunas: int = 0, pesos: list = None) -> float:
    """
    Calcula el total de la cita según R1:
    - Consulta: $350, Vacuna: $280 c/u.
    - Recargo de $80 en consulta para perros > 25 kg.
    - 10% de descuento en consultas (incluido recargo) si hay 2+ mascotas en la misma cita.
    """
    if pesos is None:
        pesos = []
        
    total_consultas = 0.0
    num_consultas = len(consultas)
    
    for peso in pesos:
        costo_consulta = 350.0
        if peso > 25.0:
            costo_consulta += 80.0
        total_consultas += costo_consulta
        
    if not pesos and num_consultas > 0:
        total_consultas = 350.0 * num_consultas

    if num_consultas >= 2:
        total_consultas *= 0.90

    total_vacunas = 280.0 * vacunas
    
    return round(total_consultas + total_vacunas, 2)


def calcular_cancelacion(horas_anticipacion: float, asistio: bool = True) -> float:
    """
    Calcula el costo de cancelación según R2:
    - Con 12 horas o más: gratis ($0).
    - Con menos de 12 horas o no se presenta (asistio = False): cargo fijo de $100.
    """
    if not asistio or horas_anticipacion < 12.0:
        return 100.0
    return 0.0
