var obj1 = { a: 1, b: [2, 3]}

function deepCopy(obj) {
  var dst = {}
  for (key in obj) {
    if (obj.hasOwnProperty(key)) {
      //判断ojb子元素是否为对象，如果是，递归复制
      if (obj[key] && typeof obj[key] === "object") {
        dst[key] = deepCopy(obj[key])
      } else {  //如果不是，简单复制
        dst[key] = obj[key]
      }
    }
  }
  return dst
}

obj2 = deepCopy(obj1)
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