import os
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from scripts.resources.collection import CollectionResource
from scripts.resources.item import ItemResource


def main():
    # ==========================
    # Configuración de Flask y Flask-RESTful
    # ==========================
    app = Flask(__name__)
    api = Api(app)

    # ==========================
    # Registro de Rutas
    # ==========================
    load_dotenv()
    env = os.getenv("ENV", "dev")

    if env == "dev":
        # Productos
        api.add_resource(
            type("ProductosCollection", (CollectionResource,), {}), 
            "/productos",
            resource_class_args=("productos",)
        )
        api.add_resource(
            type("ProductosItem", (ItemResource,), {}), 
            "/productos/<int:id>",
            resource_class_args=("productos", "codigo")
        )

        # Tipos de Producto
        api.add_resource(
            type("TiposDeProductoCollection", (CollectionResource,), {}), 
            "/tipos_de_producto",
            resource_class_args=("tipos_de_producto",)
        )
        api.add_resource(
            type("TiposDeProductoItem", (ItemResource,), {}), 
            "/tipos_de_producto/<int:id>",
            resource_class_args=("tipos_de_producto",)
        )

        # Tipos de Unidad
        api.add_resource(
            type("TiposDeUnidadCollection", (CollectionResource,), {}), 
            "/tipos_de_unidad",
            resource_class_args=("tipos_de_unidad",)
        )

        api.add_resource(
            type("TiposDeUnidadItem", (ItemResource,), {}), 
            "/tipos_de_unidad/<int:id>",
            resource_class_args=("tipos_de_unidad",)
        )

        # Marcas
        api.add_resource(
            type("MarcasCollection", (CollectionResource,), {}), 
            "/marcas",
            resource_class_args=("marcas",)
        )

        api.add_resource(
            type("MarcasItem", (ItemResource,), {}), 
            "/marcas/<int:id>",
            resource_class_args=("marcas",)
        )

        # Ventas
        api.add_resource(
            type("VentasCollection", (CollectionResource,), {}), 
            "/ventas",
            resource_class_args=("ventas",)
        )
        api.add_resource(
            type("VentasItem", (ItemResource,), {}), 
            "/ventas/<int:id>",
            resource_class_args=("ventas",)
        )

        # Métodos de Pago
        api.add_resource(
            type("MetodosDePagoCollection", (CollectionResource,), {}), 
            "/metodos_de_pago",
            resource_class_args=("metodos_de_pago",)
        )
        api.add_resource(
            type("MetodosDePagoItem", (ItemResource,), {}), 
            "/metodos_de_pago/<int:id>",
            resource_class_args=("metodos_de_pago",)
        )

        # Clientes
        api.add_resource(
            type("ClientesCollection", (CollectionResource,), {}), 
            "/clientes",
            resource_class_args=("clientes",)
        )
        api.add_resource(
            type("ClientesItem", (ItemResource,), {}), 
            "/clientes/<int:id>",
            resource_class_args=("clientes",)
        )

    # ==========================
    # Ejecutar la aplicación
    # ==========================
    app.run(debug=True)

if __name__ == "__main__":
    main()
