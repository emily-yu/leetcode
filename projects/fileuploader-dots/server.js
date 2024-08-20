const express = require('express');
const multer = require("multer");

const app = express()
const fs = require('fs');

// const port = 3000
// ADD THIS
var cors = require('cors');
app.use(cors());
app.get('/', (req, res) => {
  res.send('Hello World!')
})
app.post('/imagerecieve', (req, res) => {
    console.log(req.body);
    const image = req.body.
    res.send('Hello World!')
})

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, './images')
    },
    filename: function (req, file, cb) {
      const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9)
      cb(null, file.originalname); // ./
    }
  })
  
const upload = multer({ storage: storage })

app.post('/stats', upload.single('uploaded_file'), function (req, res) {
  // req.file is the name of your file in the form above, here 'uploaded_file'
  // req.body will hold the text fields, if there were any 
  console.log(req.file, req.body)
  res.send('asdf')
});

const path = require('path');

app.get('/uploadedfiles', function (req, res) {
    results = []
    //joining path of directory 
const directoryPath = path.join(__dirname, './images');
//passsing directoryPath and callback function
    fs.readdir(directoryPath, function (err, files) {
        //handling error
        if (err) {
            return console.log('Unable to scan directory: ' + err);
        } 
        //listing all files using forEach
        files.forEach(function (file) {
            // Do whatever you want to do with the file
            console.log(file); 
            results.push(file)
            console.log(results)
        });
        res.send(JSON.stringify(results))

    });
    // res.send(JSON.stringify(results))
});

app.listen(3001, () => {
  console.log(`Example app listening on port ${3001}`)
})