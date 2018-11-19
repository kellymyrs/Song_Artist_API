<html>
<head>
    <meta charset="UTF-8">
    <title> Now the song is in the table traogudi of our DATABASE songs </title>
    <style>
        th,td {
        padding: 10px;
        }
    </style>
<head/>
<body>
    <h1>Now the song is in the table tragoudi of our DATABASE songs<h1/>
        <hr>
            <table>
                <tr>
                <th>Title</th>
                <th>Production Year</th>
                <th>CD</th>
                <th>Singer</th>
                <th>Composer</th>
                <th>Song Writer</th>
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
