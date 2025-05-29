from fastapi import FastAPI
import uvicorn
from db import Base, engine
from routes.marca import router as marca_router
from routes.medida_de_venta import router as medida_de_venta_router
from routes.unidad_de_medida import router as unidad_de_medida_router
from routes.producto import router as producto_router
from routes.cliente import router as cliente_router
from routes.precio import router as precio_router
from routes.estado_de_lote import router as estado_de_lote_router
from routes.ubicacion import router as ubicacion_router
from routes.lote import router as lote_router
from routes.metodo_de_pago import router as metodo_de_pago_router
from routes.venta import router as venta_router

app = FastAPI(debug=True)

Base.metadata.create_all(bind=engine)

# ${host}/api/marcas
# ${host}/api/marcas/{id}
# CRUD available
app.include_router(
    marca_router,
    prefix="/api",
    tags=["marcas"],
)

# ---
# ${host}/api/medidas_de_venta
# ${host}/api/medidas_de_venta/{id}
# CR available
app.include_router(
    medida_de_venta_router,
    prefix="/api",
    tags=["medidas_de_venta"],
)

# ---
# ${host}/api/unidades_de_medida
# ${host}/api/unidades_de_medida/{id}
# CR available
app.include_router(
    unidad_de_medida_router,
    prefix="/api",
    tags=["unidades_de_medida"],
)

# ---
# ${host}/api/productos
# ${host}/api/productos/{id}
# CRUD available
app.include_router(
    producto_router,
    prefix="/api",
    tags=["productos"],
)

# ---
# ${host}/api/clientes
# ${host}/api/clientes/{id}
# CRUD available
app.include_router(
    cliente_router,
    prefix="/api",
    tags=["clientes"],
)

# ---
# ${host}/api/precios
# ${host}/api/precios/{id}
# CRUD available
app.include_router(
    precio_router,
    prefix="/api",
    tags=["precios"],
)

# ---
# ${host}/api/estados_de_lote
# ${host}/api/estados_de_lote/{id}
# CRUD available
app.include_router(
    estado_de_lote_router,
    prefix="/api",
    tags=["estados_de_lote"],
)

# ---
# ${host}/api/ubicaciones
# ${host}/api/ubicaciones/{id}
# CRUD available
app.include_router(
    ubicacion_router,
    prefix="/api",
    tags=["ubicaciones"],
)

# ---
# ${host}/api/lotes
# ${host}/api/lotes/{id}
# CRUD available
app.include_router(
    router=lote_router,
    prefix="/api",
    tags=["stock"],
)

# ---
# ${host}/api/metodos_de_pago
# ${host}/api/metodos_de_pago/{id}
# CRUD available
app.include_router(
    metodo_de_pago_router,
    prefix="/api",
    tags=["metodos_de_pago"],
)

# ---
# ${host}/api/ventas
# ${host}/api/ventas/{id}
# CRD available
app.include_router(
    venta_router,
    prefix="/api",
    tags=["ventas"],
)

# ---
# ${host}/api/usuarios
# ${host}/api/usuarios/{id}

print(f"API corriendo en {app.docs_url} {app.root_path} {app.routes}")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=4000)
