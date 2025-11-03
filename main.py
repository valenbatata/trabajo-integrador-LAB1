import flet as ft
from src.modelos.cliente import Cliente
from src.modelos.cuenta import Cuenta
# lógica para generar números de cuenta
import random

# --- Almacenamiento en memoria ---
banco_clientes: list[Cliente] = []
banco_cuentas: list[Cuenta] = []

def main(page: ft.Page):
    """Función principal que define la UI y la lógica de la aplicación Flet."""

    # --- Configuración de la Página ---
    page.title = "Sistema Bancario - DevOps 1er Año"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # --- Componentes de la Interfaz (UI) ---

    # Título de la sección
    txt_titulo_crear = ft.Text("Crear Nuevo Cliente y Cuenta", style=ft.TextThemeStyle.HEADLINE_MEDIUM)

    # Campos de entrada para el Cliente
    txt_nombre = ft.TextField(label="Nombre", width=300)
    txt_apellido = ft.TextField(label="Apellido", width=300)
    txt_dni = ft.TextField(label="DNI (sin puntos)", width=300)

    # Botón para ejecutar la acción 
    btn_crear = ft.Button(text="Crear Cliente", icon=ft.Icons.PERSON_ADD)

    # Área para mostrar los resultados  
    txt_titulo_resultados = ft.Text("Clientes y Cuentas Creadas", style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    col_resultados = ft.Column(
        controls=[ft.Text("Aún no hay clientes.")],
        spacing=10
    )

    # --- Lógica de Eventos ---

    def limpiar_campos():

        txt_nombre.value = ""
        txt_apellido.value = ""
        txt_dni.value = ""
        page.update()

    def mostrar_error(mensaje: str):
        """Muestra un mensaje de error temporal en la parte inferior"""
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje),
            bgcolor=ft.Colors.RED_700
        )
        page.snack_bar.open = True
        page.update()

    def btn_crear_cliente_click(e):
        try:
            # 1. Obtenemos SOLO los 3 datos que pide el TP y tu clase Cliente
            nombre = txt_nombre.value
            apellido = txt_apellido.value
            dni = txt_dni.value

            if not nombre or not apellido or not dni:
                raise ValueError("Nombre, Apellido y DNI son obligatorios.")

            # 2. Creamos el cliente SOLO con esos 3 argumentos
            nuevo_cliente = Cliente(
                nombre=nombre, 
                apellido=apellido, 
                dni=dni
            )
        
            # 3. (El resto del código sigue igual...)
            num_cuenta = f"CTA-{random.randint(10000, 99999)}" 
            nueva_cuenta = Cuenta(
                numero_cuenta=num_cuenta,
                cliente_asociado=nuevo_cliente,
                saldo_inicial=0.0
            )

            # Guardamos en memoria las nuevas entidades
            banco_clientes.append(nuevo_cliente)
            banco_cuentas.append(nueva_cuenta)

            # Visualizamos
            if len(banco_clientes) == 1:
                col_resultados.controls.clear() # Limpia el mensaje "No hay clientes"
            
            # Agregamos el nuevo cliente a la lista visible
            col_resultados.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.ACCOUNT_BALANCE_WALLET),
                    title=ft.Text(f"Cuenta: {nueva_cuenta.get_numero_cuenta()}"),
                    subtitle=ft.Text(f"Cliente: {nuevo_cliente.get_apellido()}, {nuevo_cliente.get_nombre()} | Saldo: ${nueva_cuenta.get_saldo():.2f}")
                )
            )

            limpiar_campos()
            print(f"DEBUG: Cliente creado: {nuevo_cliente}")
            print(f"DEBUG: Cuenta creada: {nueva_cuenta}")

        except ValueError as ve:
            # Capturamos errores de validación 
            print(f"Error de validación: {ve}")
            mostrar_error(f"Error de validación: {ve}")
        except Exception as ex:
            # Capturamos cualquier otro error inesperado
            print(f"Error inesperado: {ex}")
            mostrar_error(f"Error inesperado: {ex}")
    
        page.update()

    # --- Conexión de Eventos ---
    # Conectamos la función 'btn_crear_cliente_click' al evento 'on_click' del botón
    btn_crear.on_click = btn_crear_cliente_click

    # --- Carga de la Página ---
    # Agregamos todos los componentes a la vista principal
    page.add(
        txt_titulo_crear,
        txt_nombre,
        txt_apellido,
        txt_dni,
        btn_crear,
        ft.Divider(), # Una línea divisoria
        txt_titulo_resultados,
        col_resultados
    )

# --- Punto de entrada ---
if __name__ == "__main__":
     # Para ejecutar como app de escritorio
    ft.app(target=main, view=ft.AppView.WEB_BROWSER) # Para ejecutar en el navegador