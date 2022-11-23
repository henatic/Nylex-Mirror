const request = require('request');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const jsonParser = bodyParser.json();

app.post('/', jsonParser, (req, res) => {
    console.log('Connection started!');
    request.post('http://127.0.0.1:5000', {json: req.body.message},
    function (error, response, body) {
        let userResponse;
        if(!error && response.statusCode == 200) {
            userResponse = body;
            console.log(body)
        }
        else {
            userResponse = error;
            console.log(error);
        }
    });
    res.send(JSON.stringify(userResponse));
})

const port = Number(process.env.PORT) || 5000;
app.listen(port, () => console.log(`Listening to port ${port}...`));