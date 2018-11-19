<html>
<head>
    <meta charset="UTF-8">
    <title>Insert Song</title>
</head>
<body>
    <h1>Insert Song</h1>
    <hr>
    <table>
        <form action="/songs/insert_song" method="post">
            <tr>
                <td>Title</td> <td><input type="text" name="title" required /></td>
            </tr>

            <tr>
                <td>Production Year</td> <td><input type="text" name="prod_year" required /></td>
            </tr>

            <tr>
                <td>CD</td>
                <td>
                    <select name="c">
                            %for item in final[0]:
                               <option value={{str(item[0])}}>{{str(item[0])}}</option>
                            %end
                     </select>
                </td>
            </tr>

            <tr>
                <td>Singer</td>
                <td>
                    <select name="sin">
                            %for item in final[1]:
                               <option value={{str(item[0])}}>{{str(item[0])}}</option>
                            %end
                     </select>
                </td>
            </tr>

            <tr>
                <td>Composer</td>
                <td>
                    <select name="co">
                            %for item in final[2]:
                               <option value={{str(item[0])}}>{{str(item[0])}}</option>
                            %end
                     </select>
                </td>
            </tr>

            <tr>
                <td>SongWriter</td>
                <td>
                    <select name="s_writer">
                            %for item in final[3]:
                               <option value={{str(item[0])}}>{{str(item[0])}}</option>
                            %end
                     </select>
                </td>
            </tr>


            <tr>
                <td><td><input type="submit" value="Update Information" /></td></td>
            </tr>

        </form>
    </table>
<hr/>
</body>
</html>