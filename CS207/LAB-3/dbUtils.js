var mysql = require('mysql')

var con = mysql.createConnection({
    'host': 'localhost',
    'user': 'root',
    'password': 'Shubham@007'
});

module.exports.createDB = (dbName)=>{
    con.connect((err)=>{
        if(err){
            console.log("Unable to connect to the database --"+err.code);        
        }
        else{
            console.log("Connected to the database.");
            con.query("CREATE DATABASE "+dbName+";",(err)=>{
                if(err){
                    console.log("Unable to create the Database: "+err.code);
                }
                else{
                    console.log("DB created");
                    con.query("SHOW DATABASES;",(err,rows,fields)=>{
                        if(err){
                            console.log("Error while showing the databases: ",err.code);
                        }
                        else{
                            console.log(rows)
                            console.log("now dropping database named: ",dbName);
                            con.query("DROP DATABASE "+dbName+";",(err)=>{
                                if(err){
                                    console.log("Unable to drop ",dbName,"\nEnded with Error Code: "+err.code)
                                }
                                else{
                                    con.query("SHOW DATABASES;",(err,rows,fields)=>{
                                        if(err){
                                            console.log("Unable to show the databases error: ",err.code);
                                        }
                                        else{
                                            console.log(rows);
                                            console.log(dbName,"dropped.");
                                        }
                                    })
                                }
                            })
                        }
                    })
                }
                
            })
        }   
    })
    
}
