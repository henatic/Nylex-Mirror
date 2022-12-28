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

        for(let device of devices) {
            request.post('http://'+ device.ip +':5000/', {json: req.body},
            function (error, response, body) {
                if(!error && response.statusCode == 200) {
                    userResponse = body;
                }
                else {
                    userResponse = error;
                }
            });
            try{
                res.send(JSON.stringify(userResponse));
            }
            catch(err) {
                console.log("Could not send to " + device.ip + " with the following error:\n" + err);
            }
        }
        
    })
    request.post('http://0.0.0.0:5000/', {json: req.body},
        function (error, response, body) {
            if(!error && response.statusCode == 200) {
                userResponse = body;
            }
            else {
                userResponse = error;
            }
        });
        try{
            res.send(JSON.stringify(userResponse));
        }
        catch(err) {
            console.log("Could not send to localhost with the following error:\n" + err);
        }
});

const port = Number(process.env.PORT) || 5050;
app.listen(port, () => console.log(`Listening to port ${port}...`));