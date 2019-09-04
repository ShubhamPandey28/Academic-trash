var mailer = require("nodemailer")


/*
var transporter = nodemailer.createTransport(transport[, defaults])

# transporter:-> is going to be an object that is able to send mail
# transport:-> is the transport configuration object, connection url or a transport plugin instance
# defaults:-> is an object that defines default values for mail options

# TLS:-> is a cryptographic protocol that provides end-to-end communications security over networks and is widely used for internet communications and online transactions. 
*/

var transporter = mailer.createTransport({
    service: "gmail",
    auth:{
        user: "shubhapandeye10@gmail.com",
        pass: "shubham2010"
    }
})

module.exports.sendMail = (receiverEmail,subject,message)=>{
    var mailOptions={
        from: "shubhampandeye10@gmail.com",
        to: receiverEmail,
        subject: subject,
        text: message
    }
    
    transporter.sendMail(mailOptions,(err,data)=>{
        if(err){
            console.log("Uanble to send the message. Error Occured: "+err.code);
            return;
        }
        console.log("Sent Successfully")
    })
}