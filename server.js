const express = require('express')
const app = express()

app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(express.json());

const port = 3001

function saveToFile(data){
  const fs = require('fs');

  const content = 'Some content!';

  var jsonContent = JSON.stringify(data);
  console.log("jsoncontent\n",jsonContent);

  try {
    fs.writeFileSync('data.json', jsonContent);
    // file written successfully
  } catch (err) {
    console.error(err);
  }

}

function loadFromFile(filePath){
  const fs = require('fs');

  var data ="";
  var jsonObj = {};
  try {
    data = fs.readFileSync(filePath, 'utf8');
    console.log(data);
    jsonObj = JSON.parse(data);
  } catch (err) {
    console.error(err);
  }

  // return data;
  return jsonObj;
}

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/load', (req, res) => {
  var filePath = "./data.json";
  var data = loadFromFile(filePath);
  // res.send('load workflowy data is ' + data)
  res.json(data);
})

app.post('/save', (req, res) => {
  saveToFile(req.body);
  // res.send('save workflowy data')
  console.log("req body:", req.body);
  res.send(req.body);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})