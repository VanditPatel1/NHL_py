from config import DRIVER, SERVER, DATABASE, UID, PWD
import psycopg2
from create_tables import player_meta, shot_table
import pandas as pd


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
            self.conn.rollback()
            raise

        else:
            self.conn.commit()
            cur.close()

    def add_row(self, packet, table):

        keys = packet.keys()
        columns = ','.join(keys)
        values = ','.join(['%({})s'.format(k) for k in keys])
        insert = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(table, columns, values)
        try:
            cur = self.conn.cursor()
            res = cur.mogrify(insert, packet)
            cur.execute(res)

        except Exception as ex:
            print (ex)
            self.conn.rollback()
            raise

        else:
            self.conn.commit()
            cur.close()

    def get_player_id(self, id=None, full=None, first=None, last=None):

        if last:
            SQL = """SELECT id FROM player_meta WHERE {0} = {1};""".format('last_name', last)

        if full is not None:
            first, last = full.split(' ')
            SQL = """SELECT id FROM player_meta WHERE {0} = (%s) and {1} = (%s);""".format('first_name', 'last_name')
            print (SQL)
        try:
            cur = self.conn.cursor()
            res = cur.execute(SQL, (first, last))

        except Exception as ex:
            print (ex)
            self.conn.rollback()
            raise

        else:
            res = cur.fetchall()
            cur.close()

            return res

    def get_shots(self, id):

        SQL = """SELECT x_coord, y_coord, goal, period, shot_type, assist_1, assist_2, game_winning, empty_net FROM shots WHERE player_id = {}""".format(id)

        try:
            cur = self.conn.cursor()
            res = cur.execute(SQL)

        except Exception as ex:
            print (ex)
            self.conn.rollback()
            raise

        else:
            res = cur.fetchall()
            cur.close()

            df = pd.DataFrame(res, columns=['x', 'y', 'goal', 'period', 'shot', 'a1', 'a2', 'gw', 'empt'])
            return df





if __name__ == '__main__':
    db = db_connect()
    #db.create_table(player_meta)
    db.create_table(shot_table)
