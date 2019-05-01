// Array Helper Method

// case 1.
// ES5
// var colors = ['red','blue','green']
// for (var i = 0; i < colors.length; i++) {
//     console.log(colors[i]);
// }

// ES6 + - forEach
const colors = ['red','blue','green'] 
//forEach: 앞의 배열을 하나씩 반복하면서 첫번째 파라메터로 넘겨줌(배열 뒤에 사용)
colors.forEach(function(color){ //callback function
    console.log(color) //리턴값이 없음(결과값만 보여줌)
})


// case 2.
// ES5
// var numbers = [1,2,3]
// var doubleNumbers = []
// for (var i = 0; i < numbers.length; i++){
//     doubleNumbers.push(numbers[i]*2) //데이터를 두배로 만들어서 새로운 배열을 생성
// }
// console.log(doubleNumbers)

// ES6+ - map
const numbers = [1,2,3]
const doubleNumbers = numbers.map(function(number){ //map을 배열을 하나씩 반복하면서 가지고옴
    return number*2 //return값이 doublenumbers의 새로운 배열을 생성
})
console.log(doubleNumbers)


// case 3.
// ES6+ - filter
const products = [
    {name: 'cucumbe', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'},
]
//filter는 배열안에 들어갈 값을 return하는게 아니라 조건을 리턴하여 조건에 맞는 object를 새로운 배열에 넣음
//해당 조건이 true일 경우, item을 가져와 배열에 넣음
const fruitProducts = products.filter(function(product){ 
    return product.type === 'fruit' //fruit라는 조건에 맞는 사과와 바나나가 하나의 배열에 들어감
})
console.log(fruitProducts)


// case 4.
// ES6+ - find
const users = [
    {name:'yo'},
    {name:'admino'},
    {name:'ssafy'},
]
//단 한개의 값만 반환
//위에서 부터 순회하면서 return에 맞는 값 하나만 찾아 반환
const foundUser = users.find(function(user){ 
    return user.name === 'admino'
})
console.log(foundUser)


// case 5.
// ES6+ - every & some
const computers = [
    {name: 'macbook', ram:16},
    {name: 'gram', rem:8},
    {name:'series9', ram:32},
]
//모두가 return조건에 맞으면 true (and느낌)
const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16
})
//하나가 return조건에 맞으면 true (or느낌)
const someComputersAvailable = computers.some(function(computer){
    return computer.ram > 16
})
console.log(everyComputersAvailable)
console.log(someComputersAvailable)