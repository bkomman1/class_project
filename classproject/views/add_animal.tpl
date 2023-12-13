<!DOCTYPE html>
<html>
<head>
    <title>Add Animal</title>
</head>
<body>
    <h1>Add Animal</h1>
    <form action="/animals/add" method="post">
        <label>Name: <input type="text" name="animal_name" required></label><br>
        <label>Species: <input type="text" name="species" required></label><br>
        <input type="submit" value="Add Animal">
    </form>
    <p><a href="/animals">Back to Animals</a></p>
</body>
</html>
