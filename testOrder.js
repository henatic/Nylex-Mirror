let xhr = new XMLHttpRequest();
var url = "URL_HERE";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "text/xml");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log("Succeeded with this response: ");
        console.log(xhr.responseText);
    }
    else {
        console.log("Failed with this response: ");
        console.log(xhr.responseText);
    }
};
console.log(jsonString);
xhr.send(jsonString);