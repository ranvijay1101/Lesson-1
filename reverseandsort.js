// let num = [10,5, 1, 3, 6,4,8,5]
// num.reverse()
// console.log(num)

let num = [10, 40, 25, 5, 1]
num.sort(function(a,b){
    return a - b
})
num.reverse()
console.log(num)