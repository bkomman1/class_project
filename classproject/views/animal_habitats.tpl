<!DOCTYPE html>
<html>
<head>
    <title>Animal Habitats</title>
</head>
<body>
    <h1>Animal Habitats</h1>
    <p><strong>Animal ID:</strong> {{animal_id}}</p>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
        </tr>
        % for habitat in habitats:
            <tr>
                <td>{{habitat[0]}}</td>
                <td>{{habitat[1]}}</td>
            </tr>
        % end
    </table>

    <p><a href="/animals">Back to Animals</a></p>
</body>
</html>
