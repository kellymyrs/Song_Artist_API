<html>
<head>
    <meta charset="UTF-8">
    <title>The update of the artist succeeded</title>
    <style>
        th,td {
        padding: 10px;
        }
    </style>
<head/>
<body>
    <h1>The update of the artist with the below characteristics succeeded<h1/>
        <hr>
            <table>
            %for row in rows:
                <tr>
                <th>Name</th>
                <th>Surname</th>
                <th>Birth Year</th>
                </tr>

                <tr>
                <th>{{row[0]}}</th>
                <th>{{row[1]}}</th>
                <th>{{row[2]}}</th>
                </tr>
                %end
            %end
            <table/>
        <hr/>
</body>
<html>