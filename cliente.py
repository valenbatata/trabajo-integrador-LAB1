class Cliente:

    def __init__ (self, nombre: str, apellido: str, email: str, password: str, dni: str, telefono: str, ciudad: str, pais: str):
   
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.password = password
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais


    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_dni(self):
        return self.dni 
       
    def get_email(self):
        return self.email 

    def get_password(self):
        return self.password
    
    def get_telefono(self):
        return self.telefono  
    
    def get_ciudad(self):
        return self.ciudad
    
    def get_pais(self):
        return self.pais
    

    def mostrar_datos(self):
        nombre = self.get_nombre()
        apellido = self.get_apellido()
        dni = self.get_dni()

        return f"Cliente: {apellido}, {nombre}\nDNI: {dni}"