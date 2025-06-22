

from database.DB_connect import DBConnect
from model.object import Object


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_nodi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select *
from artsmia.objects o"""
            cursor.execute(query, )

            for row in cursor:
                result.append(Object(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_archi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor()
            query = """SELECT eo1.object_id, eo2.object_id
FROM artsmia.exhibition_objects eo1, artsmia.exhibition_objects eo2
WHERE eo1.exhibition_id = eo2.exhibition_id
  AND eo1.object_id < eo2.object_id
"""
            cursor.execute(query, )

            for row in cursor:
                result.append((row[0], row[1]))
            cursor.close()
            cnx.close()
        return result
if __name__ == '__main__':
    DAO = DAO()
    print(len(DAO.get_nodi()))
    print(len(DAO.get_archi()))



