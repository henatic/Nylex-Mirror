const request = require('request');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const find = require('local-devices');
const jsonParser = bodyParser.json();

app.post('/', jsonParser, (req, res) => {
    console.log(req.body);
    let userResponse = req.body;

    find().then(devices =>{

        for(device of devices) {
            console.log(device.ip);
        }
        request.post('http://localhost:5050/', {json: req.body},
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

});

const port = Number(process.env.PORT) || 5000;
app.listen(port, () => console.log(`Listening to port ${port}...`));