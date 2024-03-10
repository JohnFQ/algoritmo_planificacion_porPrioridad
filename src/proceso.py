class proceso:
    def __init__(self, id, nombre, tiempo_llegada, tiempo_ejecucion, estado = "nuevo"):
        self.id = id
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion
        self.estado = estado

    def actualizarEstado(self, nuevo_estado):
        if nuevo_estado:
            self.estado = nuevo_estado
        else:
            print('No puede asignar un valor None al estado del proceso')


