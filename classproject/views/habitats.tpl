<!DOCTYPE html>
<html>
<head>
    <title>Habitats</title>
</head>
<body>
    <h1>Habitats</h1>
    <p><a href="/habitats/add">Add Habitat</a></p>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Actions</th>
        </tr>
        % for row in rows:
            <tr>
                <td>{{row[0]}}</td>
                <td>{{row[1]}}</td>
                <td>
                    <a href="/habitats/edit/{{row[0]}}">Edit</a>
                    <a href="/habitats/delete/{{row[0]}}">Delete</a>
                </td>
            </tr>
        % end
    </table>
</body>
</html>
