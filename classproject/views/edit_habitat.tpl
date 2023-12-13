<!DOCTYPE html>
<html>
<head>
    <title>Edit Habitat</title>
</head>
<body>
    <h1>Edit Habitat</h1>
    <form action="/habitats/edit/{{habitat[0]}}" method="post">
        <label>Name: <input type="text" name="habitat_name" value="{{habitat[1]}}" required></label><br>
        <input type="submit" value="Update Habitat">
    </form>
    <p><a href="/habitats">Back to Habitats</a></p>
</body>
</html>
