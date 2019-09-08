var http = require("http")
var fs = require("fs")
var path = require("path")
var url = require("url")
const {parse} = require("querystring")
var mailer = require("./mailer")


app = http.createServer((req,res)=>{
    // fetching the requested file 
    if(req.method == 'POST'){
        
        var body = ''
        req.on('data',(dataChunk)=>{
            body += dataChunk.toString();
        });
        req.on('end',()=>{
            var postBody=parse(body)
            console.log("sending message to "+postBody.firstname +" "+postBody.lastname)
            mailer.sendMail(postBody.email,"test Email",postBody.comments)
            res.writeHead(200,{'Content-type':"text/html"});
            res.end('Post received.\n');
        }) 

    }
    else{
        console.log("requested: ",req.url);
        var filePath = "."+req.url;
        if(filePath == "./"){
            filePath = "./static/index2.html";
        }else{
            filePath = "./static"+req.url;
        }
        //Getting the content type as the res.writeHed requires the content typte of file which is tobe dispalyed in the browser
        ext = String(path.extname(filePath)).toLocaleLowerCase();

        var typejson = {
            ".js": "text/javascript",
            ".html": "text/html",
            ".css": "text/css",
            ".json": "application/json"
        }

        var contentType = typejson[ext] || "application/octet-stream";

        fs.readFile(filePath,(error,content)=>{
            if(error){
                if(error.code == 'ENOENT'){ //ENOENT (No such file or directory): Commonly raised by fs operations to indicate that a component of the specified pathname does not exist — no entity (file or directory) could be found by the given path.
                    fs.readFile("./404.html",(err,content)=>{
                        res.writeHead(404,{'Content-type':"text/html"});
                        res.end(content,"utf-8");   
                    });
                }
                else{
                    res.writeHead(500);
                    res.end("error: "+error.code);
                }

            }else{
                res.writeHead(200,{'Content-Type':contentType});
                res.end(content,"utf-8");
            }
        });
    }
});
var port = 2000;
app.listen(port,()=>{
    console.log("listening to the port: "+port);
})