const WebSocket = require('ws');
const fs = require('fs');
var express = require('express');

//create web server 
var http = express();

// use static files
http.use(express.static('public'))

http.get('/', function(req,res){
  res.send('<div><p>Client is available at: <a href="client.html"><b>/client.html</b></a><p>Server is available at: <b>ws://127.0.0.1:9001</b></p></div>');
});


//Fire up webserver
http.listen(9000, function () {
  console.log('INFO: Webserver fired up on port 9000');
})


// Fire up WebSocket server
const wsServer = new WebSocket.Server({
  port: 9001
}, function(){
  console.log('INFO: WebSockets server fired up on port 9001\n\n');
});



/*
*
* Function definitions
*
*/

function incomingMessageHandler(payload){
  //handle payload here
  console.log(payload);
}



/****************
/* Read data.json
****************/

var count = 0,
buf = '';
var ptr = 0;
var t;
var chunkArr = [];
var totalCount = 0;
function pushData(connection){

  console.log("\n\nINFO: BEGIN_STREAM_JSON");

  var stream = fs.createReadStream(__dirname+'/public/data/data.json',{ highWaterMark: 2 * 1024, flags: 'r', encoding: 'utf-8' });

  stream.on("data",(chunk)=>{
    buf+= chunk.toString();

    pump(connection);

  });

  stream.on("end", function(){
    // end read
    console.log("INFO: READ_COMPLETE_JSON");
    count = 0;
  });


}


function pump(con){
  var pos;
  while( (pos=buf.indexOf('\n')) >= 0){
    if (pos == 0) { // if there's more than one newline in a row, the buffer will now start with a newline
            buf = buf.slice(1); // discard it
            continue; // so that the next iteration will start with data
        }
    processLine(buf.slice(0,pos), con);
    buf = buf.slice(pos+1);
  }
}

function processLine(line, con) { // here's where we do something with a line

    if (line[line.length-1] == '\r') line=line.substr(0,line.length-1); // discard CR (0x0D)

    if (line.length > 0) { // ignore empty lines
        var obj = JSON.parse(line); // parse the JSON
        //console.log(obj); // do something with the data here!
        //return line;

        chunkArr.push(line);
        totalCount = chunkArr.length;

        if(!t){
          t = setInterval(()=>{
            if(ptr == totalCount){
              clearInterval(t);
              return;
            }
            console.log("READING_CHUNK: "+(++count));

            if(con.readyState == 1){

                con.send(chunkArr[ptr]);
            }

            ptr+=1;


          }, 300);
        }
    }
    //return '';
}

function newConnection(connection){
  //handle connection
  console.log('INFO: WS_CONNECTION_OK');
  connection.on('message', incomingMessageHandler);
  pushData(connection);
}


// definitions end


// on connection
wsServer.on('connection', newConnection);

wsServer.on('close', function(){
  console.log('WS_CONNECTION_CLOSE');

})
