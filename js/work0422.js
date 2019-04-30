function concat(str1,str2){
    return `${str1}-${str2}`
}
console.log('concat:'+concat(2,1))

function checkLongStr(string){
    if (string>10){
        return 'True'
    }
    else{
        return 'False'
    }
}
console.log('Check_long_str:'+checkLongStr('yo'))

if (checkLongStr(concat('Happy','Hacking'))) {
    console.log('Long String')
}
else {
    console.log('short string')
}