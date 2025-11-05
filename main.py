import flet as ft
from src.modelos.cliente import Cliente
from src.modelos.cuenta import Cuenta
from src.modelos.caja_ahorro import CajaAhorro
import random #crea los IDS de las cuentas de usuario
from fpdf import FPDF 
from datetime import datetime 

# --- arregos de memoria ---
banco_clientes: list[Cliente] = []
banco_cuentas: list[Cuenta | CajaAhorro] = [] 

"""Usamos esta variable para "recordar" la instancia de la cuenta (sea `Cuenta` o `CajaAhorro`) que el usuario está viendo y operando activamente"""
cuenta_activa_actual: Cuenta | CajaAhorro | None = None

def main(page: ft.Page):
    #--- Configuración de la Página ---
    page.title = "Sistema Bancario - DevOps 1er Año"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- FORMULARIO ---
    txt_titulo_crear = ft.Text("Crear Nuevo Cliente y Cuenta", style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    txt_nombre = ft.TextField(label="Nombre", width=350)
    txt_apellido = ft.TextField(label="Apellido", width=350)
    txt_dni = ft.TextField(label="DNI (sin puntos)", width=350)
    
    dd_tipo_cuenta = ft.Dropdown(
        label="Tipo de Cuenta",
        width=350,
        options=[
            ft.dropdown.Option(key="CajaAhorro", text="Caja de Ahorro (con 2% interés)"),
            ft.dropdown.Option(key="Cuenta", text="Cuenta Corriente (base)"),
        ],
        value="CajaAhorro" 
    )
    
    btn_crear = ft.Button(text="Crear Cliente", icon=ft.Icons.PERSON_ADD, width=350)
    
    #Estilo del formulario
    vista_formulario = ft.Column(
        controls=[
            txt_titulo_crear,
            txt_nombre,
            txt_apellido,
            txt_dni,
            dd_tipo_cuenta,
            btn_crear
        ],
        visible=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    # --- VISTA DE LA CUENTA ---
    txt_titulo_cuenta = ft.Text("¡Cuenta Creada Exitosamente!", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.Colors.GREEN_700)
    txt_numero_cuenta = ft.Text(size=16)
    txt_cliente_asociado = ft.Text(size=16)
    txt_saldo = ft.Text(size=18, weight=ft.FontWeight.BOLD)
    txt_monto = ft.TextField(label="Ingrese el monto", width=350, prefix="$", keyboard_type=ft.KeyboardType.NUMBER)
    txt_transaccion_status = ft.Text(value="", visible=False, color=ft.Colors.BLUE_700) 
    btn_depositar = ft.Button(text="Depositar", icon=ft.Icons.ADD, width=170)
    btn_retirar = ft.Button(text="Retirar", icon=ft.Icons.REMOVE, width=170)
    
    # --- BOTÓN PDF ---
    btn_imprimir_pdf = ft.Button(
        text="Imprimir PDF", 
        icon=ft.Icons.PICTURE_AS_PDF, 
        width=350,
        bgcolor=ft.Colors.GREEN_700
    )
   
    
    btn_volver = ft.Button("Crear otro cliente", icon=ft.Icons.ARROW_BACK, width=350)

    vista_cuenta = ft.Column(
        controls=[
            txt_titulo_cuenta, ft.Divider(),
            txt_numero_cuenta, txt_cliente_asociado, txt_saldo,
            ft.Divider(),
            ft.Text("Realizar Transacción", style=ft.TextThemeStyle.TITLE_MEDIUM),
            txt_monto,
            ft.Row(controls=[btn_depositar, btn_retirar], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            txt_transaccion_status, 
            ft.Divider(),
            btn_imprimir_pdf, 
            btn_volver
        ],
        visible=False,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    # --- Lógica de Eventos ---
    def mostrar_error(mensaje: str):
        page.snack_bar = ft.SnackBar(content=ft.Text("debe ingresar un monto"), bgcolor=ft.Colors.RED_700)
        page.snack_bar.open = True
        page.update()

    def actualizar_saldo_ui():
        if cuenta_activa_actual:
            txt_saldo.value = f"Saldo: ${cuenta_activa_actual.get_saldo():.2f}"
        page.update()

    def mostrar_vista_cuenta(cuenta: Cuenta | CajaAhorro): 
        global cuenta_activa_actual # permite modificar la variable de memoria
        cuenta_activa_actual = cuenta 

        txt_numero_cuenta.value = f"N° de Cuenta: {cuenta.get_numero_cuenta()}"
        cliente = cuenta.get_cliente()
        txt_cliente_asociado.value = f"Cliente: {cliente.get_apellido()}, {cliente.get_nombre()}"
        
        if isinstance(cuenta, CajaAhorro): #insistance pregunta si es tipo caja de ahorro
             txt_titulo_cuenta.value = f"¡Caja de Ahorro Creada!"
             txt_cliente_asociado.value += f" (Interés: {cuenta.get_interes()*100}%)"
        else:
            txt_titulo_cuenta.value = "¡Cuenta Corriente Creada!"

        actualizar_saldo_ui()
        
        vista_formulario.visible = False
        vista_cuenta.visible = True
        
        txt_nombre.value = ""
        txt_apellido.value = ""
        txt_dni.value = ""
        txt_monto.value = ""
        txt_transaccion_status.visible = False

    def volver_al_inicio(e):
        global cuenta_activa_actual
        cuenta_activa_actual = None 
        vista_cuenta.visible = False
        vista_formulario.visible = True
        page.update()

    def btn_depositar_click(e):
        if not cuenta_activa_actual: return #si la variable está vacia return detiene la función
        try:
            monto_float = float(txt_monto.value)
            exito = cuenta_activa_actual.ingresar_dinero(monto_float)
            if exito:
                actualizar_saldo_ui()
                txt_transaccion_status.value = f"Depósito de ${monto_float:.2f} exitoso."
                txt_transaccion_status.color = ft.Colors.GREEN_800
                txt_transaccion_status.visible = True
                txt_monto.value = "" 
        except ValueError as ve:
            txt_transaccion_status.value = f"Error: {ve}"
            txt_transaccion_status.color = ft.Colors.RED_800
            txt_transaccion_status.visible = True
        page.update()


    def btn_retirar_click(e):
        if not cuenta_activa_actual: return
        try:
            monto_float = float(txt_monto.value)
            
            if hasattr(cuenta_activa_actual, 'retirar_dinero'): # "has attribute" (o "tiene un atributo"
                exito = cuenta_activa_actual.retirar_dinero(monto_float)
            else:
                print("ADVERTENCIA: Usando _retirar. Crea 'retirar_dinero' público.")
                cuenta_activa_actual._retirar(monto_float) 
                exito = True 

            if exito:
                actualizar_saldo_ui()
                txt_transaccion_status.value = f"Retiro de ${monto_float:.2f} exitoso."
                txt_transaccion_status.color = ft.Colors.GREEN_800
                txt_transaccion_status.visible = True
                txt_monto.value = "" 
        except ValueError as ve:
            txt_transaccion_status.value = f"Error: {ve}"
            txt_transaccion_status.color = ft.Colors.RED_800
            txt_transaccion_status.visible = True
        page.update()

    # --- FUNCIÓN PARA PDF ---
    def btn_imprimir_pdf_click(e):
        if not cuenta_activa_actual:
            mostrar_error("No hay cuenta activa para imprimir.")
            return

        try:
            cuenta = cuenta_activa_actual
            cliente = cuenta.get_cliente()
            
            pdf = FPDF()
            pdf.add_page()
            
            # Título
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, 'Reporte de Cuenta Bancaria', 0, 1, 'C')
            pdf.ln(10) # Salto de línea

            # --- Datos del Cliente ---
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, 'Datos del Cliente', 0, 1)
            pdf.set_font("Arial", '', 12)
            pdf.cell(0, 8, f"Cliente: {cliente.get_apellido()}, {cliente.get_nombre()}", 0, 1)
            pdf.cell(0, 8, f"DNI: {cliente.get_dni()}", 0, 1)
            pdf.ln(5)

            # --- Datos de la Cuenta ---
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, 'Datos de la Cuenta', 0, 1)
            pdf.set_font("Arial", '', 12)
            pdf.cell(0, 8, f"Numero de Cuenta: {cuenta.get_numero_cuenta()}", 0, 1)
            if isinstance(cuenta, CajaAhorro):
                pdf.cell(0, 8, f"Tipo: Caja de Ahorro (Interes: {cuenta.get_interes()*100}%)", 0, 1)
            else:
                pdf.cell(0, 8, "Tipo: Cuenta Corriente", 0, 1)
            
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, f"Saldo Actual: ${cuenta.get_saldo():.2f}", 0, 1)
            pdf.ln(10)

            # --- Historial de Transacciones ---
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, 'Historial de Transacciones', 0, 1)
            pdf.set_font("Arial", '', 10)
            
            transacciones = cuenta.get_transacciones()
            if not transacciones:
                pdf.cell(0, 8, "No hay transacciones registradas.", 0, 1)
            else:
                # Encabezados de la tabla
                pdf.set_fill_color(230, 230, 230)
                pdf.cell(50, 8, "Fecha", 1, 0, 'C', True)
                pdf.cell(40, 8, "Tipo", 1, 0, 'C', True)
                pdf.cell(40, 8, "Monto", 1, 1, 'C', True)
                
                # Datos
                for tx in transacciones: #tx nombre de variable temporal
                    fecha_str = tx.get_fecha().strftime("%Y-%m-%d %H:%M")
                    monto_str = f"${tx.get_monto():.2f}"
                    tipo_str = tx.get_tipo().capitalize()
                    
                    pdf.cell(50, 8, fecha_str, 1)
                    pdf.cell(40, 8, tipo_str, 1)
                    pdf.cell(40, 8, monto_str, 1, 1, 'R') # Alineado a la derecha
            
            # Guardar el PDF
            nombre_archivo = f"reporte_{cliente.get_dni()}_{cuenta.get_numero_cuenta()}.pdf"
            pdf.output(nombre_archivo)
            
            print(f"DEBUG: PDF generado: {nombre_archivo}")
            txt_transaccion_status.value = f"PDF '{nombre_archivo}' guardado."
            txt_transaccion_status.color = ft.Colors.BLUE_800
            txt_transaccion_status.visible = True

        except Exception as ex:
            print(f"Error al generar PDF: {ex}")
            mostrar_error(f"Error inesperado al generar PDF: {ex}")
        
        page.update()


    # --- FUNCIÓN PARA CREAR CLIENTE ---

    def btn_crear_cliente_click(e):
        try:
            nombre = txt_nombre.value
            apellido = txt_apellido.value
            dni = txt_dni.value
            tipo_cuenta_seleccionado = dd_tipo_cuenta.value 

            if not nombre or not apellido or not dni or not tipo_cuenta_seleccionado:
                raise ValueError("Todos los campos son obligatorios.")

            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, dni=dni)
            num_cuenta = f"CTA-{random.randint(10000, 99999)}" 
            
            nueva_cuenta: Cuenta | CajaAhorro
            
            if tipo_cuenta_seleccionado == "CajaAhorro":
                nueva_cuenta = CajaAhorro(
                    numero_cuenta=num_cuenta,
                    cliente_asociado=nuevo_cliente,
                    saldo_inicial=0.0
                )
            else: 
                nueva_cuenta = Cuenta(
                    numero_cuenta=num_cuenta,
                    cliente_asociado=nuevo_cliente,
                    saldo_inicial=0.0
                )

            banco_clientes.append(nuevo_cliente)
            banco_cuentas.append(nueva_cuenta)

            mostrar_vista_cuenta(nueva_cuenta) 
            
            print(f"DEBUG: Cliente creado: {nuevo_cliente}")
            print(f"DEBUG: Cuenta creada: {nueva_cuenta}")

        except ValueError as ve:
            print(f"Error de validación: {ve}")
            mostrar_error(f"Error de validación: {ve}")
        except Exception as ex:
            print(f"Error inesperado: {ex}")
            mostrar_error(f"Error inesperado: {ex}")
        
        page.update()

    # --- Conexión de Eventos ---
    btn_crear.on_click = btn_crear_cliente_click
    btn_volver.on_click = volver_al_inicio
    btn_depositar.on_click = btn_depositar_click
    btn_retirar.on_click = btn_retirar_click
    btn_imprimir_pdf.on_click = btn_imprimir_pdf_click 

    # --- Carga de la Página ---
    page.add(
        vista_formulario,
        vista_cuenta
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)