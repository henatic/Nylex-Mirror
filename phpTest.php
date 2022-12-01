<?php
    // use Joomla\CMS\Factory;

    // Converts it into a PHP object

    if(strtoupper($_SERVER["REQUEST_METHOD"]) != 'POST') {
        echo 'Method not supported.';
        exit;
    }
    if($_SERVER["CONTENT_TYPE"] != 'application/json') {
        echo 'Unsupported content-type.';
        exit;
    }

    $data = trim(file_get_contents('php://input'));
    echo $data;
    $decoded = json_decode($data, true);
    echo http_build_query($decoded);
    
    $options = array(
        'http' => array(
          'method'  => 'POST',
          'Accept' => '*/*',
          'header'  => "Content-type: application/json\r\n",
          'content' => $data
        )
      );
    echo 'My option is ' . $options['http']['content'];
    $context = stream_context_create($options);
    echo 'My context is ' . var_dump($context);
    $result = file_get_contents('http://10.10.99.152:5000/', false, $context);
    if ($result === FALSE) {
        echo "Bad request: ". $data;
    }

    var_dump($result);
?>

<?php
    if(strtoupper($_SERVER["REQUEST_METHOD"]) != 'POST') {
        echo 'Method not supported.';
        exit;
    }
    if($_SERVER["CONTENT_TYPE"] != 'application/json') {
        echo 'Unsupported content-type.';
        exit;
    }

    $data = trim(file_get_contents('php://input'));
    echo '<p id="json">' . $data . '</p>';
?>
<script language="javascript" type="text/javascript">
  function makeRequest() {
	let myJson = JSON.parse(JSON.stringify(document.getElementById('json').innerHTML));

	const xhr = new XMLHttpRequest();
    const url = "http://10.10.99.152:5000/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
       	myJson = JSON.parse(xhr.responseText);
        	document.getElementById('json').innerHTML = myJson;
      }
    }
  }
  window.addEventListener("load", makeRequest(), false);
</script>