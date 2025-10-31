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
    
    def get_ciudad(self):
        return self.__ciudad
    

    