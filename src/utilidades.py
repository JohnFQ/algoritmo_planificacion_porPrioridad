import logging
import os
class utilidades:
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta completa al directorio de logs
    logs_directory = os.path.join(current_directory, 'logs')

    # Crear el directorio de logs si no existe
    os.makedirs(logs_directory, exist_ok=True)

    # Construir la ruta completa al archivo de registro
    log_file_path = os.path.join(logs_directory, 'aplicacion.log')
    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    @classmethod
    def escribir_log(cls, mensaje, severidad):
        if severidad == 'INFO':
            cls.logger.info(mensaje)
        elif severidad == 'ERROR':
            cls.logger.error(mensaje)
        elif severidad == 'WARNING':
            cls.logger.warning(mensaje)
        else:
            cls.logger.warning(f'la severidad {severidad} no es reconocida. Se registra en log como INFO')
            cls.logger.info(mensaje)
