var obj1 = { a: 1, b: [2, 3]}

function shallowCopy(obj) {
  var dst = {}
  dst = obj
  return dst
}

obj2 = shallowCopy(obj1)
console.log(obj1)
console.log(obj2)
obj2.a = 5
console.log(obj1)
console.log(obj2)
obj2.b[0] = 4
console.log(obj1)
console.log(obj2)
obj2.b = [7, 8]
console.log(obj1)
console.log(obj2)