class Cliente:
        
        def __init__(self, nombre: str, apellido: str, email: str, password: str, dni: str, telefono: str, ciudad: str, pais: str):
                # Usamos setters para aplicar validaciones centrales
                self.set_nombre(nombre)
                self.set_apellido(apellido)
                self.set_email(email)
                self.set_password(password)
                self.set_dni(dni)
                self.set_telefono(telefono)
                self.set_ciudad(ciudad)
                self.set_pais(pais)

        # ---------------- GETTERS ----------------
        def get_nombre(self):
                return self.__nombre

        def get_apellido(self):
                return self.__apellido

        def get_dni(self):
                return self.__dni

        def get_email(self):
                return self.__email

        def get_password(self):
                return self.__password

        def get_telefono(self):
                return self.__telefono

        def get_ciudad(self):
                return self.__ciudad

        def get_pais(self):
                return self.__pais

        # ---------------- SETTERS + VALIDACIÓN ----------------
        def set_nombre(self, nombre: str):
                if not isinstance(nombre, str) or not nombre.strip() or not nombre.strip().isalpha():
                    raise ValueError("El nombre debe contener solo letras y no estar vacío.")
                self.__nombre = nombre.strip().capitalize()

        def set_apellido(self, apellido: str):
                if not isinstance(apellido, str) or not apellido.strip() or not apellido.strip().isalpha():
                    raise ValueError("El apellido debe contener solo letras y no estar vacío.")
                self.__apellido = apellido.strip().capitalize()

        def set_email(self, email: str):
                if not isinstance(email, str) or "@" not in email or "." not in email:
                    raise ValueError("El email no tiene un formato válido.")
                self.__email = email.strip().lower()

        def set_password(self, password: str):
                if not isinstance(password, str) or len(password) < 6:
                    raise ValueError("La contraseña debe tener al menos 6 caracteres.")
                self.__password = password

        def set_dni(self, dni: str):
                dni_str = str(dni).strip()
                if not dni_str.isdigit():
                    raise ValueError("El DNI debe contener solo números.")
                if len(dni_str) < 7 or len(dni_str) > 10:
                    raise ValueError("El DNI debe tener entre 7 y 10 dígitos.")
                self.__dni = dni_str

        def set_telefono(self, telefono: str):
                telefono_str = str(telefono).strip()
                if not telefono_str.isdigit() or len(telefono_str) < 7:
                    raise ValueError("El teléfono debe contener solo números válidos y tener al menos 7 dígitos.")
                self.__telefono = telefono_str

        def set_ciudad(self, ciudad: str):
                if not isinstance(ciudad, str) or not ciudad.strip() or not ciudad.strip().isalpha():
                    raise ValueError("La ciudad debe contener solo letras y no estar vacía.")
                self.__ciudad = ciudad.strip().capitalize()

        def set_pais(self, pais: str):
                if not isinstance(pais, str) or not pais.strip() or not pais.strip().isalpha():
                    raise ValueError("El país debe contener solo letras y no estar vacío.")
                self.__pais = pais.strip().capitalize()

        # ---------------- METODOS ----------------
        def mostrar_datos(self):
                nombre = self.get_nombre()
                apellido = self.get_apellido()
                dni = self.get_dni()
                return f"Cliente: {apellido}, {nombre}\nDNI: {dni}"
