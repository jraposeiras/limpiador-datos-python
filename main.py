import pandas as pd

def limpiar_datos(archivo_entrada, archivo_salida):
    # 1. Cargar datos
    df = pd.read_csv(archivo_entrada)
    
    # 2. Eliminar filas duplicadas
    df = df.drop_duplicates()
    
    # 3. Limpiar texto (Espacios y mayúsculas)
    df['Nombre'] = df['Nombre'].str.strip().str.title()
    df[' Email'] = df[' Email'].str.strip().str.lower()
    
    # 4. Normalizar fechas a formato estándar YYYY-MM-DD
    df[' Fecha_Registro'] = pd.to_datetime(df[' Fecha_Registro'], dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d')
    
    # 5. Guardar resultado limpio
    df.to_csv(archivo_salida, index=False)
    print(f"✅ ¡Proceso completado! Archivo guardado en: {archivo_salida}")

if __name__ == "__main__":
    limpiar_datos('datos_muestra.csv', 'datos_limpios.csv')
