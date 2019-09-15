const express = require('express')
const app = express()
const port = 9467
const fs = require('fs');

app.get('/', (req, res) => {
fs.readFile('data.json', 'utf8', (err, data) => {
    if (err) throw res.send(err);
	res.send(data)


});
});
app.get('/test', (req, res) => res.send('Hello World! test'))



app.listen(port, () => console.log(`Example app listening on port ${port}!`))