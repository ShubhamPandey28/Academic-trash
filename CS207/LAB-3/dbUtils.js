var mysql = require('mysql')

var con = mysql.createConnection({
    'host': 'localhost',
    'user': 'root',
    'password': 'Shubham@007'
});

createTable = (dbName,tableName,callback)=>{
    var con2 = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'Shubham@007',
        database: dbName
    });
    con2.query("CREATE TABLE "+tableName+"(id varchar(255));",(err)=>{
        if(err){
            console.log("Unable to create the Table.\nEnded with error code: ",err.code);
            callback(err);
        }
        else{
            console.log("Table named '"+tableName+"' created.")
            callback();
        }
    })
}

module.exports.createTable = createTable;


module.exports.createDB = (dbName,show=false,callback)=>{
    con.connect((err)=>{
        if(err){
            console.log("Unable to connect to the database --"+err.code);
            callback(err);        
        }
        else{
            console.log("Connected to the database.");
            con.query("CREATE DATABASE "+dbName+";",(err)=>{
                if(err){
                    console.log("Unable to create the Database: "+err.code);
                    callback(err);
                }
                else{
                    console.log("Database created");
                    if(show){
                        con.query("SHOW DATABASES;",(err,rows,fields)=>{
                            if(err){
                                console.log("Error while showing the databases: ",err.code);
                                callback(err)
                            }
                            else{
                                console.log(rows)                    
                            }
                        })
                    }
                    callback();
                }
                
            })
        }   
    })
    
}

module.exports.dropDB = (dbName)=>{
    con.query("DROP DATABASE "+dbName+";",(err)=>{
        if(err){
            console.log("Unable to drop the database.\nProcess ended with exit code: ",err.code);
        }
        else{
            console.log("dropped",dbName);
        }
    })
}

