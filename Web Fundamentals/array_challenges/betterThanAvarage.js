function betterThanAverage(arr) {
    var sum = 0;
    // calculate the sum of all elements
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }

    var count = 0;
    // count how many values are greater than the average
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > sum / arr.length) {
            count += 1;
        }
    }
    return count;
}

var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // Output: 4
