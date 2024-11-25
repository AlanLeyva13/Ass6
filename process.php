<?php
if (!isset($_GET['integers']) || !isset($_GET['threshold'])) {
    echo "Error: Missing integers or threshold.";
    exit;
}

$integers = escapeshellarg($_GET['integers']);
$threshold = escapeshellarg($_GET['threshold']);

$command = "python3 bitwise_operations.py $integers $threshold";
$output = shell_exec($command);

if ($output === null) {
    echo "Error executing Python script.";
    exit;
}


echo "<h1>Python Script Output</h1>";
echo "<pre>$output</pre>";
?>