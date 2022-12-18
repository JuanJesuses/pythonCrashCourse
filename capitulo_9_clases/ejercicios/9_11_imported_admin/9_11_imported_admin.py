# Comienza tu trabajo desde el ejercicio 9-8. Almacena las clases User, Privileges y Admin en un módulo.
# Crea un archivo separado, haz una instancia de Admin y llama a show_privileges()
# para mostrar que.

from uspriad_module import Admin, User, Privileges

administrador1 = Admin('Guido', 'Van Rossum', 60, '25, La Runa st.', '111 222 333', 'guido@python.ned')
administrador1.privileges.show_privileges()