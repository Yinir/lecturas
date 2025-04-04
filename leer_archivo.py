import pandas as pd

# Definir el orden de las columnas para medicamentos e insumos
orden_columnas_medicamentos_insumos = [
    't_codif', 'consecutivo', 'tipo_id', 'no_id', 'f_nacto', 'sexo', 'cod_munic', 
    'cod_dx', 'cod_dx_rel', 'f_prestacion', 'cups', 'ambito', 'f_pago', 
    'cantidad', 'dias_tratamiento', 'vr_neto', 'v_cuota_mod', 'v_copago', 'cod_prestador', 'no_factura'
]
# definir orden de las columnas procedimientos # 19 columnas
#orden_columnas_procedimientos = ['t_codif', 'consecutivo', 'tipo_id', 'no_id', 'f_nacto', 'sexo', 'cod_munic', 'cod_dx', 'cod_dx_rel', 'f_prestacion',
                  #'cups', 'ambito', 'f_pago', 'estancia', 'vr_neto', 'v_cuota_mod', 'v_copago', 'cod_prestador', 'no_factura']
# definir orden de las columnas insumos # 20 columnas
#orden_columnas_medicamentos_insumos = ['t_codif', 'consecutivo', 'tipo_id', 'no_id', 'f_nacto', 'sexo', 'cod_munic', 'cod_dx', 'cod_dx_rel', 'f_prestacion',
                  #'cups', 'ambito', 'f_pago', 'cantidad', 'dias_tratamiento', 'vr_neto', 'v_cuota_mod', 'v_copago', 'cod_prestador', 'no_factura']

# Lista de rutas de archivos TXT
rutas_archivos = [
    "C:\\Users\\PracticantePyc2_C\\Desktop\\lecturas\\SUF140RSUB20241231NI000800251440C10.txt"
]

# Función para procesar un archivo y mostrar cómo se organizan las columnas
def procesar_archivo(ruta_archivo):
    # Leer el archivo excluyendo la primera línea, aplicando nombres y seleccionando columnas en el orden correcto
    df = pd.read_csv(
        ruta_archivo, 
        sep=";", 
        skiprows=1,  # Excluir el primer renglón
        names=orden_columnas_medicamentos_insumos,  # Asignar nombres de columnas
        usecols=orden_columnas_medicamentos_insumos  # Usar solo las columnas necesarias
    )

    # Mostrar el nombre del archivo
    print(f"\n=== ARCHIVO: {ruta_archivo} ===")

    # Mostrar el DataFrame para ver cómo se organizan las columnas
    print("\n=== ORGANIZACIÓN DE COLUMNAS CON DATOS ===")
    print(df)  # Imprimir el DataFrame para verificar la asignación de columnas

    # Convertir valores numéricos para evitar errores y asegurar cálculos correctos
    df["vr_neto"] = pd.to_numeric(df["vr_neto"], errors="coerce").fillna(0)
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce").fillna(0)
    df["dias_tratamiento"] = pd.to_numeric(df["dias_tratamiento"], errors="coerce").fillna(0)
    df["v_cuota_mod"] = pd.to_numeric(df["v_cuota_mod"], errors="coerce").fillna(0)
    df["v_copago"] = pd.to_numeric(df["v_copago"], errors="coerce").fillna(0)

    # Contar el número total de registros
    total_registros = len(df)

    # Calcular el costo total sumando la columna "vr_neto"
    costo_total = df["vr_neto"].sum()

    # Mostrar los resultados
    print("\n=== RESUMEN ===")
    print(f"Total de registros: {total_registros}")
    print(f"Costo total: ${costo_total:,.2f}")  # Formato con separadores de miles y dos decimales

# Procesar cada archivo en la lista
for ruta_archivo in rutas_archivos:
    procesar_archivo(ruta_archivo)