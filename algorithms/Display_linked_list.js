class Node {
  constructor(data) {
      this.data = data;
      this.next = null;
  }
}

class SLL {
  constructor() {
      this.head = null;
  }

  addFront(data) {
      const newNode = new Node(data);
      newNode.next = this.head;
      this.head = newNode;
  }

  display() {
      let current = this.head;
      let result = "";

      while (current) {
          result += current.data;
          if (current.next) {
              result += ', ';
          }
          current = current.next;
      }

      return result;
  }
}

const SLL1 = new SLL();
SLL1.addFront(76);
SLL1.addFront(2);
console.log(SLL1.display()); // Output: "2, 76"

SLL1.addFront(11.41);
console.log(SLL1.display()); // Output: "11.41, 2, 76"
