from config import DRIVER, SERVER, DATABASE, UID, PWD
import psycopg2
from create_tables import player_meta, shot_table


class db_connect():

    def __init__(self):
        try:
            self.conn = psycopg2.connect(host=SERVER,
                                    database=DATABASE,
                                    port=5432,
                                    user=UID,
                                    password=PWD)
            print ("Connection made to db...")

        except:
            print ("Cannot connect to db...")
            raise

    def create_table(self, new_table):
        try:
            cur = self.conn.cursor()
            cur.execute(new_table)

        except:
            print ("Could not create table...")
            raise

        else:
            conn.commit()
            cur.close()

    def add_row(self, packet, table):
        try:
            cur = self.conn.cursor()
            cur.execute("""INSERT INTO {0} VALUES {1} on conflict do nothing""".format(table, tuple(packet)))

        except:
            print ("Could not add to table {}, values {}").format(table, packet)

        else:
            conn.commit()
            cur.close()


if __name__ == '__main__':
    create_table()
