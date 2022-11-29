<?php
// Converts it into a PHP object
$data = json_decode(file_get_contents('php://input'), true);
echo $data;

$options = array(
'http' => array(
'header' => "",
'method' => 'POST',
'content' => http_build_query($data)
)
);
$context = stream_context_create($options);
$result = file_get_contents('http://10.10.99.152:5000', true, $context);
if ($result === FALSE) {
    echo "Bad request: ". $data;
}

var_dump($result);
?>