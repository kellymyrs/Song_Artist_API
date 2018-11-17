import pymysql as db
import settings

'''lets create the connection we need for the server of the database'''

def connection():
    conn = db.connect(host=settings.mysql_host,
                      port=settings.mysql_port,
                      user=settings.mysql_user,
                      password=settings.mysql_password,
                      db=settings.mysql_schema,
                      charset=settings.mysql_charset)
    return conn


 #1st task
# if we don't have input we return the whole list
# in this queries we are using like statement because if we don't enter except ('') except name then if we put
# == it would cause from and statements 1 and 0 and 0 and that causes thw whole statement 0
#putting the +% for finding also the names etc tha start from the letter of input also for no input
# because if it give as empty string(nothing from input) we dose'nt count it
# no output
#also its like a scroller is better to find names from the start letter
def get_update__search_artist(artist_type, name, surname, start_birth, final_birth):
    con = connection()
    cur = con.cursor()
    if start_birth == '':
        start_birth = '1800'
    if final_birth == '':
        final_birth = '2050'
    if artist_type == 'tragoudistis':
        cur.execute("SELECT DISTINCT ar_taut,onoma,epitheto,etos_gen "
                    "FROM kalitexnis,singer_prod "
                    "WHERE ar_taut=tragoudistis AND (onoma LIKE %s AND epitheto LIKE %s AND etos_gen>=%s AND etos_gen<=%s); "
                    , (name + '%', surname + '%', start_birth, final_birth))
        results = cur.fetchall()
    elif artist_type == 'sinthetis':
        cur.execute("SELECT DISTINCT ar_taut,onoma,epitheto,etos_gen "
                    "FROM tragoudi,kalitexnis "
                    "WHERE ar_taut=sinthetis AND (onoma LIKE %s AND epitheto LIKE %s AND etos_gen>=%s AND etos_gen<=%s); "
                    , (name + '%', surname + '%', start_birth, final_birth))
        results = cur.fetchall()
    elif artist_type == 'stixourgos':
        cur.execute("SELECT DISTINCT ar_taut,onoma,epitheto,etos_gen "
                    "FROM tragoudi,kalitexnis "
                    "WHERE ar_taut=stixourgos AND (onoma LIKE %s AND epitheto LIKE %s AND etos_gen>=%s AND etos_gen<=%s); "
                    , (name + '%', surname + '%', start_birth, final_birth))
        results = cur.fetchall()
    cur.close()
    con.close()
    return results

def get_update_artist_information(id):
    con = connection()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT onoma,epitheto,etos_gen "
                "FROM kalitexnis "
                "WHERE ar_taut=%s; ", id)
    results = cur.fetchall()
    cur.close()
    con.close()
    return results

def update_result(na, surname, birth_year):
    con = connection()
    cur = con.cursor()
    cur.execute("UPDATE kalitexnis "
                "SET onoma=%s , epitheto=%s , etos_gen=%s "
                "WHERE onoma=%s AND epitheto=%s AND etos_gen=%s; ", (na, surname, birth_year, na, surname, birth_year))
    con.commit()
    cur.execute("SELECT DISTINCT onoma,epitheto,etos_gen "
                "FROM kalitexnis "
                "WHERE onoma=%s AND epitheto=%s AND etos_gen=%s; ", (na, surname, birth_year))
    results = cur.fetchall()
    cur.close()
    con.close()
    return results

#end of 1st task

#2nd task
# same with the first like the only think that we cant check is the number so just ignore them after the if statement
def search_songs(s_title , prod_year, comp):
    con = connection()
    cur = con.cursor()
    if len(prod_year)>0:
        cur.execute("SELECT DISTINCT titlos,etos_par,etaireia "
                    "FROM tragoudi as t,singer_prod as s,group_prod as g,cd_production as c "
                    "WHERE (t.titlos=s.title AND s.cd=c.code_cd AND titlos LIKE %s AND etos_par LIKE %s AND etaireia LIKE %s) "
                    "OR (t.titlos=g.title AND g.cd=c.code_cd AND titlos LIKE %s AND etos_par LIKE %s AND etaireia LIKE %s); "
                    , (s_title + '%', prod_year, comp + '%',s_title + '%', prod_year, comp + '%'))
        results= cur.fetchall()
    else: #empty string of prod_year
        cur.execute("SELECT DISTINCT titlos,etos_par,etaireia "
                    "FROM tragoudi as t,singer_prod as s,group_prod as g,cd_production as c "
                    "WHERE (t.titlos=s.title AND s.cd=c.code_cd AND titlos LIKE %s AND etaireia LIKE %s) "
                    "OR (t.titlos=g.title AND g.cd=c.code_cd AND titlos LIKE %s AND etaireia LIKE %s); "
                    , (s_title + '%', comp + '%', s_title + '%', comp + '%'))
        results = cur.fetchall()
    cur.close()
    con.close()
    return results
#end of 2 task


#task 3
def insert_artist(id, na, su, b_year):
    con = connection()
    cur = con.cursor()
    #checking for key
    cur.execute("SELECT ar_taut "
                "from kalitexnis "
                "where ar_taut=%s ", id)
    temp = cur.fetchall()
    if not temp:
        return temp
    else:
        cur.execute("INSERT INTO kalitexnis (ar_taut, onoma, epitheto, etos_gen) VALUES (%s, %s ,%s, %s) ", (id , na, su, b_year))
        # select it to see if we insert it it
        con.commit()
        cur.execute("SELECT DISTINCT ar_taut,onoma,epitheto,etos_gen "
                    "FROM kalitexnis "
                    "WHERE ar_taut=%s AND onoma = %s AND epitheto=%s AND etos_gen=%s ", (id, na, su, b_year))
        results = cur.fetchall()
    cur.close()
    con.close()
    return results
#end of task 3


#task4
def get_cd():
    con = connection()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT code_cd "
                "FROM cd_production; " )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results

def get_kalitexnis(): #composer can sing his own songs etc
    con = connection()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT * "
                "FROM kalitexnis; " )
    results = cur.fetchall()
    cur.close()
    con.close()
    return results

def insert_song(tit, py, cd, singer, comp, sw):
    con = connection()
    cur = con.cursor()
    cur.execute("SELECT titlos "
                "from tragoudi "
                "where titlos=%s ", tit)
    temp = cur.fetchall()
    if not temp:
        return temp
    else:
        cur.execute("INSERT INTO tragoudi "
                    "VALUES (%s,%s,%s,%s); ", (tit, comp, py, sw))
        con.commit()
        cur.execute("INSERT INTO singer_prod "
                    "VALUES (%s,%s,%s); ", (cd, singer, tit))
        con.commit()
        #select to see if we insert it
        cur.execute("SELECT titlos,etos_par,cd,tragoudistis,sinthetis,stixourgos "
                    "FROM tragoudi,singer_prod "
                    "WHERE titlos=%s AND etos_par=%s AND cd=%s AND tragoudistis=%s AND sinthetis=%s AND stixourgos=%s "
                    ,(tit, py, cd, singer, comp, sw))
        results = cur.fetchall()
    cur.close()
    con.close()
    return results
#end of task 4








