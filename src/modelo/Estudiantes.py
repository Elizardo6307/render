from modelo.Coneccion import conexion2023
from flask import jsonify, request

def buscar_estu(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM autores ID_Autor = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            estu = {'ID_Autor': datos[0], 'Nombre': datos[1],
                       'Apellido': datos[2], 'Fecha_Nacimiento': datos[3]
                       }
            return estu
        else:
            return None
    except Exception as ex:
            raise ex
    

class ModeloEstudiante():

    @classmethod  # Corrige el error tipográfico aquí
    def listar_estudiante(self):
        try:
            conn = conexion2023()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM autores ")
            datos = cursor.fetchall()
            estudiantes = []

            for fila in datos:
                estu = {'ID_Autor': fila[0],
                       'Nombre': fila[1],
                       'Apellido': fila[2],
                       'Fecha_Nacimiento': fila[3]
                }
                estudiantes.append(estu)

            conn.close()

            return jsonify({'Autores': estudiantes, 'mensaje': "autores listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
            
    
    @classmethod
    def lista_estudiante(self,codigo):
        try:
            usuario = buscar_estu(codigo)
            if usuario != None:
                return jsonify({'autores': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def registrar_estudiante(self):
        try:
            usuario = buscar_estu(request.json['Id_Autor_a'])
            if usuario != None:
                return jsonify({'mensaje': "ID_autor  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO Autores values(%s,%s,%s,%s)', (request.json['ID_autor_a'], request.json['Nombre_a'],
                                                                            request.json['Apellido_a'], request.json['Fecha_Nacimiento_a']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    
    @classmethod
    def actualizar_estudiante(self,codigo):
        try:
            usuario = buscar_estu(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE Autores SET Nombre=%s, Apellido=%s, Fecha_Nacimiento=%s WHERE ID_Autor=%s""",
                        (request.json['Nombre_a'], request.json['Apellido_a'], request.json['Fecha_Nacimiento_a'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "autor actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "autor  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_estuy(self,codigo):
        try:
            usuario = buscar_estu(codigo)
            if usuario != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM autores WHERE ID_Autor = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "autor eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "autor no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})