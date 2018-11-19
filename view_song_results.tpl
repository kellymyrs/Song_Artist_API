<html>
<head>
    <meta charset="UTF-8">
    <title> View_Song_Result </title>
    <style>
        th,td {
        padding: 10px;
        }
    </style>
<head/>
<body>
    <form action="/songs/search_songs" method="post">
        <h1>View Artist Results<h1/>
        <hr>
            <table>
                <tr>
                <th>Song Title</th>
                <th>Production Year</th>
                <th>Company</th>
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
