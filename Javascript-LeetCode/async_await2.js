// async function test() {  //123
//     await new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             console.log('2')
//             resolve()
//         }, 2000)
//     })
//     console.log('3')
// }
// test()
// console.log('1')

//-------------------------------------------------------
// async function test() {  132
//     await setTimeout(()=>{
//         console.log('2')
//     }, 1000)
//     console.log('3')
// }
// test()
// console.log('1')

//------------------------------------------------------
async function test() {
    await setTimeout(()=>{
        console.log('1')
    }, 1000)
    console.log('5')
    await new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('2')
            resolve()
        }, 2000)
    })
    console.log('3')
}
test()
console.log('4')