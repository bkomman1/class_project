<!DOCTYPE html>
<html>
<head>
    <title>Animals</title>
</head>
<body>
    <h1>Animals</h1>
    <p><a href="/animals/add">Add Animal</a></p>

    <form action="/animals" method="get">
        <label>Search: <input type="text" name="search" value="{{search_term}}"></label>
        <input type="submit" value="Search">
    </form>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Species</th>
            <th>Actions</th>
        </tr>
        % for row in rows:
            <tr>
                <td>{{row[0]}}</td>
                <td>{{row[1]}}</td>
                <td>{{row[2]}}</td>
                <td>
                    <a href="/animals/edit/{{row[0]}}">Edit</a>
                    <a href="/animals/delete/{{row[0]}}">Delete</a>
                    <a href="/animal_habitats/{{row[0]}}">View Habitats</a>
                </td>
            </tr>
        % end
    </table>
</body>
</html>
