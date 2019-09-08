var mysql = require('mysql')

var con = mysql.createConnection({
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': 'shubham@007',
});

var dbName = "mydb";

con.connect((err)=>{
    if(err){
        console.log("Unable to connect to the database --"+err.code);        
    }
    else{
        console.log("Connected to the database.");
        con.query("CREATE DATABASE "+dbName,(err)=>{
            if(err){
                console.log("Unable to create the Database: "+err.code);
            }
            else{
                console.log("DB created And now going to drop it.");
            }
        })
        con.query("DROP DATABASE "+dbName,(err)=>{
            if(err){
                console.log("unable to drop the database. --"+err.code);
            }
            else{
                console.log("dropped the database");
            }
        })
    }
})
