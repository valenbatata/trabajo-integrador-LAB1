class Cliente:
        """Clase que representa a un cliente del banco."""
        def __init__(self, nombre: str, apellido: str, dni: str):
        
                # --- Validación Nombre (Letras y espacios) ---
                nombre_limpio = str(nombre).strip()
                if not nombre_limpio: 
                        raise ValueError("El nombre no puede estar vacío.")
                if not all(c.isalpha() or c.isspace() for c in nombre_limpio):
                         raise ValueError("El nombre debe contener solo letras y espacios.")
        
                # Atributos privados 
                self.__nombre = nombre_limpio

                # --- Validación Apellido (Letras y espacios) ---
                apellido_limpio = str(apellido).strip()
                if not apellido_limpio:
                        raise ValueError("El apellido no puede estar vacío.")
                if not all(c.isalpha() or c.isspace() for c in apellido_limpio):
                        raise ValueError("El apellido debe contener solo letras y espacios.")
                
                 
                self.__apellido = apellido_limpio
        
                # --- Validación DNI ---
                dni_limpio = str(dni).strip().replace(".", "").replace("-", "").replace(" ", "")
                if not dni_limpio.isdigit() or not (7 <= len(dni_limpio) <= 8):
                        raise ValueError("El DNI debe ser un número de 7 u 8 dígitos (sin puntos).")
        
                
                self.__dni = dni_limpio

        # --- GETTERS ---
        
        def get_nombre(self) -> str:
                return self.__nombre

        def get_apellido(self) -> str:
                return self.__apellido
    
        def get_dni(self) -> str:
                return self.__dni
    
        # --- MÉTODOS ---
        
        def mostrar_datos(self) -> str:
                
                return f"Cliente: {self.__apellido.upper()}, {self.__nombre}\nDNI: {self.__dni}"

        def __repr__(self) -> str:
               
                return f"Cliente(nombre={self.__nombre!r}, apellido={self.__apellido!r}, dni={self.__dni!r})"
