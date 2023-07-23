function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    num1 = fibArr[0]
    num2 = fibArr[1]
    for(let i = 2; i < n; i++){
        let sum = num1 + num2
        fibArr.push(sum)
        num1 = num2
        num2 = sum
    }
    // your code here
    return fibArr;
}
   
var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
