# Almacena la clase User en un módulo, y almacena las clases Privileges y Admin en un módulo separado.
# En un archivo separado, crea una instancia de Admin y llama a show_privileges()
# para mostrar que.

from admin_9_12 import Admin

administrador1 = Admin('Guido', 'Van Rossum', 60, '25, La Runa st.', '111 222 333', 'guido@python.ned')
administrador1.privileges.show_privileges()