const express = require('express')
const app = express()
const port = 9467
const fs = require('fs');

app.get('/bme280', (req, res) => {
    fs.readFile('data_bme280.json', 'utf8', (err, data) => {
        if (err) throw res.send(err);
        res.send(data)
    });
});

app.get('/dht', (req, res) => {
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) throw res.send(err);
        res.send(data)
    });
});

app.get('/', (req, res) => {
    fs.readFile('data_bme280.json', 'utf8', (err, data) => {
        if (err) throw res.send(err);
        res.send(data)
    });
});


app.listen(port, () => console.log(`Example app listening on port ${port}!`))