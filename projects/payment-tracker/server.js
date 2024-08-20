const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.send('/')
})

const PORT = 8000
app.listen(PORT, function () {
    console.log(`Server started on port ${PORT}`)
});