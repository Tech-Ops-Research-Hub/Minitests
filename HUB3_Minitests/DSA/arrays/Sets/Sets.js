let mySet = new Set([1,2,3]);
mySet.add(9);
console.log(mySet.has(7));
console.log([...mySet]); // [1,2,3,9]
mySet.delete(2);