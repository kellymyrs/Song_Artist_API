 <html>
<head>
    <meta charset="UTF-8">
    <title>Update Artist Information</title>
<head/>
<body>
    <hr>
    <h1>Update Artist Information<h1/>
    <hr>
    <table>
    %for row in rows:
        <form action="/songs/update_search_artist/update_artist_information/update_result" method="post">
            <tr>
                <td>Name</td> <td><input type="text" name="name" value="{{row[0]}}" /></td>
            </tr>

            <tr>
                <td>Surname</td> <td> <input type="text" name="surname" value="{{row[1]}}" /></td>
            </tr>

            <tr>
                <td>Birth Year</td> <td><input type="text" name="birth_year" value="{{row[2]}}" /></td>
            </tr>

            <tr>
                <td><td><input type="submit" value="Submit" /></td></td>
            </tr>
        </form>
     %end
    </table>
<hr/>
</body>
<html>
