from apartalo.reglas import calcular_total_cita, calcular_cancelacion

def test_cita_simple_normal():
    assert calcular_total_cita(consultas=[20.0], vacunas=0, pesos=[20.0]) == 350.0

def test_cita_con_recargo_peso():
    assert calcular_total_cita(consultas=[30.0], vacunas=0, pesos=[30.0]) == 430.0

def test_cita_multiples_mascotas_con_descuento():
    assert calcular_total_cita(consultas=[15.0, 28.0], vacunas=1, pesos=[15.0, 28.0]) == 982.0

def test_cancelacion_gratis():
    assert calcular_cancelacion(12.0, asistio=True) == 0.0
    assert calcular_cancelacion(24.0, asistio=True) == 0.0

def test_cancelacion_con_cargo():
    assert calcular_cancelacion(5.5, asistio=True) == 100.0
    assert calcular_cancelacion(10.0, asistio=False) == 100.0
