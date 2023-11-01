// Remove Blanks
function removeBlanks(str) {
    let result = '';
    for (let i = 0; i < str.length; i++) {
      if (str[i] !== ' ') {
        result += str[i];
      }
    }
    return result;
  }
  
  // Get Digits
  function getDigits(str) {
    let result = '';
    for (let i = 0; i < str.length; i++) {
      if (!isNaN(str[i])) {
        result += str[i];
      }
    }
    return Number(result);
  }
  
  // Acronyms
  function acronym(str) {
    let words = str.split(' ');
    let result = '';
    for (let i = 0; i < words.length; i++) {
      if (words[i] !== '') {
        result += words[i][0].toUpperCase();
      }
    }
    return result;
  }
  
  // Count Non-Spaces
  function countNonSpaces(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
      if (str[i] !== ' ') {
        count++;
      }
    }
    return count;
  }
  
  // Remove Shorter Strings
  function removeShorterStrings(arr, minLength) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].length >= minLength) {
        result.push(arr[i]);
      }
    }
    return result;
  }
  
  // Testing the functions
  console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));
  console.log(getDigits("abc8c0d1ngd0j0!8"));
  console.log(acronym(" there's no free lunch - gotta pay yer way. "));
  console.log(countNonSpaces("Honey pie, you are driving me crazy"));
  console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4));
  