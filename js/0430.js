//반복-while
let i = 0
while (i<10){
    console.log(i)
    i++ //탈출조건
}

//반복-for
for (let j=0; j<10; j++) { 
    console.log(j)
}

//반복-for of
for (let number of [1,2,3,4,5]){ //const로도 선언 가능
    console.log(number)
}

// array (배열)
const number = [1,2,3,4]

console.log(numbers[0])
console.log(numbers[-1])

/* > const me ={
    ... name: 'admino',
    ... 'phone number': '010123456',
    ... appleProducts:{
    ..... ipad: true,
    ..... iphone: 'X'
    ..... }
    ... } */

// JSON - javascript object notation(JS 객체 표기법)
JSON.stringify() //object -> JSON string
JSON.parse() //JSON string -> object

/* > const jsonData = JSON.stringify(me)
undefined
> jsonData
'{"name":"admino","phone number":"010123456","appleProducts":{"ipad":true,"iphone":"X"}}'
> typeof jsonData
'string'
> const parseData = JSON.parse(jsonData
... )
undefined
> parseData
{ name: 'admino',
  'phone number': '010123456',
  appleProducts: { ipad: true, iphone: 'X' } }
> typeof parseData
'object' */


//함수
// 방법1
function add(num1, num2){
    return num1+num2 //리턴을 꼭 명시해야됨
}
console.log('add:'+add(1,2))

// 방법2
const sub = function(num1,num2){
    return num1-num2
}
console.log('sub:'+sub(5,3))

typeof add
typeof sub

// Arrow Function
// 기존 방법
/*const mul = function(num1,num2){
    return num1*num2
}*/
// Arrow
const mul = (num1,num2) => {
    return num1*num2
}

let square = (num) => {
    return num**2
}

// return 문 단 한줄이면 {} & return 생략가능
square = (num) => num **2 

// ()안의 인자가 하나뿐이면 ()도 생략 가능. 0개일때는 생략 불가능
square = num => num**2
let noArgs = () => 'No args'

// object를 return한다면? 괄호가 없으면 {}를 함수의 {}로 인식하기때문에 ()가 필요!
let returnObject = () => ({key:'value'})

// 함수의 기본 인자
const sayHello = (name='noName') => `hi ${name}`

sayHello('jhon')
sayHello()

// 익명함수(이름이 존재하지 않는 함수)
function (num) {return num**3} //세제곱
(num) => {return num*0.5} //제곱근

// 익명 함수 즉시 호출(변수에다 바로 함수 호출하기)
(function (num) {return num**3})(3) //3의 세제곱