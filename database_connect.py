from config import DRIVER, SERVER, DATABASE, UID, PWD
import psycopg2
from create_tables import player_meta


def create_table():
    conn = psycopg2.connect(host=SERVER,
                            database=DATABASE,
                             port=5432,
                             user=UID,
                             password=PWD)


    cur = conn.cursor()
    cur.execute(player_meta)
    conn.commit()
    cur.close()

def player_add(packet):
    conn = psycopg2.connect(host=SERVER,
                            database=DATABASE,
                             port=5432,
                             user=UID,
                             password=PWD)


    cur = conn.cursor()
    cur.execute("""INSERT INTO player_meta VALUES {} on conflict do nothing""".format(tuple(packet)))
    conn.commit()
    cur.close()


if __name__ == '__main__':
    create_table()
