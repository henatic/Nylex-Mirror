const request = require('request');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const jsonParser = bodyParser.json();

app.post('/', jsonParser, (req, res) => {
    console.log(req.body);
    let userResponse = req.body;
    request.post('http://10.10.99.152:5001', {json: req.body},
    function (error, response, body) {
        if(!error && response.statusCode == 200) {
            userResponse = body;
        }
        else {
            userResponse = error;
        }
    });
    res.send(JSON.stringify(userResponse));
})

const port = Number(process.env.PORT) || 5000;
app.listen(port, () => console.log(`Listening to port ${port}...`));