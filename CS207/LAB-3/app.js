var mysql = require("mysql")
var fs = require('fs')
var http = require('http')
var path = require('path')
var {parse} = require('querystring')
var url = require('url')

app = http.createServer((req,res)=>{
    if(req.method == 'POST'){
        var body = "";

        req.on('data',(dataChunk)=>{
            body += dataChunk.toString();
        });

        req.on('end',()=>{
            var parsedBody = parse(body);
            console.log(parsedBody.dbName+" "+parsedBody.tableName);
            res.writeHead(200,{'content':"text/html"});
            res.end('Database Made.','utf-8');
        })
    }
    else{
        console.log("request for: ",req.url);
        var filePath = "./pubic"+req.url;
        if(req.url == "/"){
            filePath = "./public/index.html";
        }
        var ext = String(path.extname(filePath)).toLocaleLowerCase();
        var typejson = {
            ".js": "text/javascript",
            ".html": "text/html",
            ".css": "text/css",
            ".json": "application/json"
        }

        var contentType = typejson[ext] || "application/octet-stream";
        fs.readFile(filePath,(error,content)=>{
            if(error){
                if(error.code == 'ENOENT'){
                    fs.readFile("./public/404.html",(err,content)=>{
                        res.writeHead(404,{'content':'text/html'});
                        res.end(content,"utf-8");
                    });
                }
                else{
                    res.writeHead(500);
                    res.end("Error: "+error.code);
                }
            }
            else{
                res.writeHead(200,{'content':contentType});
                res.end(content,'utf-8');
            }
        })
    }
});

var port = 2020

app.listen(port,(error)=>{
    if(error){
        console.log("Unable to listen to the port: "+port+"\nError occured: "+error.code);
    }
    else{
        console.log("listening to the port: "+port);
    }
})
