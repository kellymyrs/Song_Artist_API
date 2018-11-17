# we will use templates for html
# this file contains all the routing for the bottle ,for sql queries we will use app.py
from bottle import route, run, template, request
import app
import settings

@route('/')
@route('/songs')
def songs_menu():
    return template('songs_menu')

# now we will use one route to select which template we want to return for our framework
# have one template for each task of the exercise
# we could do more routes but is a waste of  code
@route('/songs/<name>')
def songs(name):
    if name == 'update_search_artist':
        return template('update_search_artist.html')
    elif name == 'search_songs':
        return template('search_songs.html')
    elif name == 'insert_artist':
        return template('insert_artist.html')
    elif name == 'insert_song':
        #need the each one for the drop down
        cds = app.get_cd()
        sins = app.get_kalitexnis()
        comps = app.get_kalitexnis()
        sws = app.get_kalitexnis()
        #cant pass 4 variables we will pass a tuple of tuple of lists
        return template('insert_song.tpl', final=[cds, sins, comps, sws])


#task 1
# this route(post) is for the update_search_artist html-tpl form we have to get the data and return from sql table
@route('/songs/update_search_artist', method='POST')
def update_search_results():
    # now we want to get the information from the submit button
    nam = request.forms.getunicode('name')
    surname = request.forms.getunicode('surname')
    sbr = request.forms.getunicode('start_birth_year')
    fbr = request.forms.getunicode('final_birth_year')
    artist_type = request.forms.getunicode('artist_type')

    # use this function to create the table we want to print

    u_s_results = app.get_update__search_artist(artist_type, nam, surname, sbr, fbr)

    #in the case the user puts wrong name or surname or births
    if not u_s_results:
        return template('no_output_found.html')
    else:
        return template('view_artist_results.tpl', rows=u_s_results)

#it will take a string from python that will have the ar taut of each list of tuples(artists) and the we will query it
#so we ar routing the ar_taut and use it to the function to find the artist
#we could also use  a link in the button is the same thing
@route('/songs/update_search_artist/update_artist_information/<id>', method='POST')
def update_artist_information(id):
    #use this function to return the informations we need for the artist
    #make it string to be sure its also works without
    id = str(id)
    u_a_results = app.get_update_artist_information(id)

    return template('update_artist_information.tpl', rows=u_a_results)

@route('/songs/update_search_artist/update_artist_information/update_result', method='POST')
def update_result():
    na = request.forms.getunicode('name')
    surname = request.forms.getunicode('surname')
    birth_year = request.forms.getunicode('birth_year')

    u_results = app.update_result(na, surname, birth_year)
    return template('view_update_artist_result.tpl',rows=u_results)
#end of 1 task



#task 2
# this route(post) is for the search_songs html-tpl form we have to get the data and return from sql table
@route('/songs/search_songs', method='POST')
def search_songs():
    # now we want to get the information from the submit button
    s_title = request.forms.getunicode('s_title')
    prod_year = request.forms.getunicode('prod_year')
    comp = request.forms.getunicode('comp')

    #use this function to create the table we want to print

    s_s_results = app.search_songs(s_title, prod_year, comp)

    #in the case the user puts wrong title or year or company
    if not s_s_results:
        return template('no_output_found.html')
    else:
        return template('view_song_results.tpl', rows=s_s_results)
#end of task 2


#task 3
# this route(post) is for the insert artist html-tpl form we have to insert data to the sql table and return a message
@route('/songs/insert_artist',method='POST')
def insert_artist():
    #now we want to get the information from the submit button
    id = request.forms.getunicode('id')
    na = request.forms.getunicode('nam')
    su = request.forms.getunicode('sur')
    b_year = request.forms.getunicode('b_year')

    #use this function to insert an artist to our table

    i_a_results = app.insert_artist(id, na, su, b_year)

    if not i_a_results:
        return template('insert_failed.html')
    else:
        return template('insert_succeeded.tpl', rows=i_a_results)
#end of task3

#taks4
# this route(post) is for the insert song html-tpl form we have to insert data to the sql table and return message
@route('/songs/insert_song',method='POST')
def insert_song():
    #now we want to get the information from the submit button
    tit = request.forms.getunicode('title')
    py = request.forms.getunicode('prod_year')
    cd = request.forms.getunicode('c')
    singer = request.forms.getunicode('sin')
    comp = request.forms.getunicode('co')
    sw = request.forms.getunicode('s_writer')

    #use this function to insert a song to our table

    i_s_results = app.insert_song(tit, py, cd, singer, comp, sw)
    if not i_s_results:
        return template('insert_song_failed.html')
    else:
        return template('insert_song_succeeded.tpl', rows=i_s_results)
#end of task4

run(host='localhost', port=settings.web_port, reloader=True, debug=True)
