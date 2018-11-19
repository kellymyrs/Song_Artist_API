<html>
<head>
    <meta charset="UTF-8">
    <title> Now the artist is in the table kalitexnis of our DATABASE songs </title>
    <style>
        th,td {
        padding: 10px;
        }
    </style>
<head/>
<body>
    <h1>Now the artist is in the table kalitexnis of our DATABASE songs<h1/>
        <hr>
            <table>
                <tr>
                <th>National ID</th>
                <th>Name</th>
                <th>Surname</th>
                <th>Birth Year</th>
                </tr>
                <tr>
                %for row in rows:
                    <tr>
                    %for col in row:
                        <td>{{col}}</td>
                    %end
                </tr>
                %end
            <table/>
        <hr/>
</form>
</body>
<html>
