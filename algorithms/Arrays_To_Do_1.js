// Push Front
function pushFront(arr, val) {
    for (let i = arr.length; i > 0; i--) {
      arr[i] = arr[i - 1];
    }
    arr[0] = val;
    return arr;
  }
  
  // Pop Front
  function popFront(arr) {
    if (arr.length === 0) return undefined;
  
    const removedValue = arr[0];
  
    for (let i = 0; i < arr.length - 1; i++) {
      arr[i] = arr[i + 1];
    }
    arr.length--;
  
    console.log(removedValue);
    return arr;
  }
  
  // Insert At
  function insertAt(arr, index, val) {
    for (let i = arr.length; i > index; i--) {
      arr[i] = arr[i - 1];
    }
    arr[index] = val;
    return arr;
  }
  
  // Remove At
  function removeAt(arr, index) {
    if (index < 0 || index >= arr.length) return undefined;
  
    const removedValue = arr[index];
  
    for (let i = index; i < arr.length - 1; i++) {
      arr[i] = arr[i + 1];
    }
    arr.length--;
  
    console.log(removedValue);
    return arr;
  }
  
  // Swap Pairs
  function swapPairs(arr) {
    for (let i = 0; i < arr.length - 1; i += 2) {
      const temp = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = temp;
    }
    return arr;
  }
  
  // Remove Duplicates from a sorted array
  function removeDupes(arr) {
    if (arr.length === 0) return [];
  
    const result = [arr[0]];
  
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] !== arr[i - 1]) {
        result.push(arr[i]);
      }
    }
  
    return result;
  }
  
  // Testing the functions
  console.log(pushFront([5, 7, 2, 3], 8));
  console.log(popFront([0, 5, 10, 15]));
  console.log(insertAt([100, 200, 5], 2, 311));
  console.log(removeAt([1000, 3, 204, 77], 1));
  console.log(swapPairs([1, 2, 3, 4]));
  console.log(removeDupes([-2, -2, 3.14, 5, 5, 10]));
  