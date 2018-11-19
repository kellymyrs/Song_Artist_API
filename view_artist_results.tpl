<html>
<head>
    <meta charset="UTF-8">
    <title> View_Artist_Result </title>
    <style>
        th,td {
        padding: 10px;
        }
    </style>
<head/>
<body>
    <h1>View Artist Results<h1/>
        <hr>
            <table>

                <tr>
                <th>National ID</th>
                <th>Name</th>
                <th>Surname</th>
                <th>Birth Year</th>
                <th>Edit ?</th>
                </tr>

                <tr>
                %for row in rows:
                    <tr>
                    %for col in row:
                        <td>{{col}}</td>
                    %end
                <form action="/songs/update_search_artist/update_artist_information/{{row[0]}}" method="post">
                    <td><input value="Edit Me!" type="submit"></td>
                </form>
                </tr>
                %end

            <table/>
        <hr/>
</body>
<html>
