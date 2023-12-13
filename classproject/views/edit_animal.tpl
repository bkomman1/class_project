<!DOCTYPE html>
<html>
<head>
    <title>Edit Animal</title>
</head>
<body>
    <h1>Edit Animal</h1>
    <form action="/animals/edit/{{animal[0]}}" method="post">
        <label>Name: <input type="text" name="animal_name" value="{{animal[1]}}" required></label><br>
        <label>Species: <input type="text" name="species" value="{{animal[2]}}" required></label><br>
        <input type="submit" value="Update Animal">
    </form>
    <p><a href="/animals">Back to Animals</a></p>
</body>
</html>
