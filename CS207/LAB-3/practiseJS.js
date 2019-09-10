var v = 10


f = (a,b)=>{
    setTimeout(()=>{
        return a+b
    },3000)
}

// functions inside a promise run on different threads. --NF note

func = (a,b)=>{
    return new Promise((resolve, reject)=>{

        a = parseInt(a)
        b = parseInt(b)
        resolve(a+b)
    })
    
} 
"value"
func(1,2).then((value)=>{
    console.log(value,"value recieved.")
})

//console.log(f(2,3))



/*

var a = 9;
var b = 4;

var promise = Promise.resolve(a)

promise.then(()=>{
    console.log()
})

*/