import requests
import pandas as pd
import json



# ================================================================
# CONFIGURACIÓN 
# ================================================================
 
URL_TIENDA  = "https://labarricavinoteca.myshopify.com"   # URL base de la tienda
PAIS        = "USA"                                       # País de la tienda
MONEDA      = "USD"                                       # Moneda (ARS, USD, EUR, UYU)
NOMBRE_CSV  = "labarrica_products.csv"                    # Nombre del archivo de salida
 

# ----- 1. TRAER LOS DATOS -----


todos_los_productos = []
pagina = 1

while True:
    url = f"{URL_TIENDA}/products.json?limit=250&page={pagina}"
    print(f"Descargando página {pagina}...")
    
    
    respuesta = requests.get(url)
    datos = respuesta.json()
    productos = datos["products"]
    
    if not productos:  # Si la página está vacía, terminamos
        print("No hay más productos.")
        break
    
    todos_los_productos.extend(productos)
    print(f"  → {len(productos)} productos encontrados")
    pagina += 1

print(f"\nTotal de productos descargados: {len(todos_los_productos)}")

# ----- 2. CONVERTIR A TABLA -----
filas = []

for p in todos_los_productos:
    # Tomamos la primera variante (casi siempre hay una sola)
    variante = p["variants"][0] if p["variants"] else {}
    
    fila = {
        "pais":             PAIS,
        "moneda":           MONEDA,
        "id":               p.get("id"),
        "titulo":           p.get("title"),
        "bodega":           p.get("vendor"),
        "tipo":             p.get("product_type"),          # puede estar vacío
        "tags":             ", ".join(p.get("tags", [])),   # lista → texto
        "precio":           variante.get("price"),
        "precio_tachado":   variante.get("compare_at_price"),  # None si no hay promo
        "stock":            variante.get("available"),
        "publicado":        p.get("published_at"),
        "descripcion":      (p.get("body_html") or "")[:300],   # primeros 300 caracteres
    }
    filas.append(fila)

# ----- 3. GUARDAR COMO CSV -----
df = pd.DataFrame(filas)
df.to_csv(NOMBRE_CSV, index=False, encoding="utf-8-sig")

print("\nPrimeros 5 productos:")
print(df[["titulo", "bodega", "tipo", "precio", "stock"]].head())
print(f"\n✅ CSV guardado con {len(df)} filas y {len(df.columns)} columnas")