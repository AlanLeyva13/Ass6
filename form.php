<!DOCTYPE html>
<html>
<head>
    <title>Bitwise Operations Form</title>
</head>
<body>
    <form action="process.php" method="GET">
        <label for="integers">Input list of integers separated by commas):</label><br>
        <input type="text" id="integers" name="integers" placeholder="example: 3,5,7,9" required><br><br>
        <label for="threshold">Input the series of integers separated by commas:</label><br>
        <input type="number" id="threshold" name="threshold" placeholder="example 4" required><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>