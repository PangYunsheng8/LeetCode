// var arr = [];
// for (var i = 0; i < 10; i++){
//     arr[i] = function(){
//         console.log(i)
//     }
// }
// arr[5]()  //10

// var arr = [];
// for (let i = 0; i < 10; i++){
//     arr[i] = function(){
//         console.log(i)
//     }
// }
// arr[5]()  //5

// var arr = []
// for (var i = 0; i < 10; i++){
//     arr[i] = function showNum(i){
//         return function(){
//             console.log(i)
//         }
//     }(i)
// }
// arr[5]()  //5

// //手写一个promise
// var myPromsie = new Promise((resolve, reject) =>{
//     if (/*异步操作成功*/true){
//         resolve(value)
//     } else {
//         reject(value)
//     }
// })
// myPromsie.then(data => {
//     //success
// }, error => {
//     //failure
// })

// //以下代码依次输出的内容是？
// setTimeout(function () {
//     console.log(1)
// }, 0);
// new Promise(function executor(resolve) {
//   console.log(2);
//   for (var i = 0; i < 10000; i++) {
//     i == 9999 && resolve();
//   }
//   console.log(3);
// }).then(function () {
//   console.log(4);
// });
// console.log(5);


async function testAsync() {
    let timer1 = await setTimeout(()=>{
        console.log('output1')
    }, 1000)
    console.log('output4')
    let timer2 = await setTimeout(()=>{
        console.log('output2')
    }, 2000)
    console.log('output5')
}
testAsync()
console.log('output3')