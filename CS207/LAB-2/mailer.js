var mailer = require("nodemailer")


var transporter = mailer.createTransport({
    service: "gmail",
    auth:{
        user: "shubhapandeye10@gmail.com",
        pass: "<password>"
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
