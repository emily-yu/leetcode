var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send('Hello World!');
});
app.post("/post", (req, res) => {
    console.log("Connected to React");
    res.redirect("/");
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, function () {
    console.log(`Server started on port ${PORT}`)
});