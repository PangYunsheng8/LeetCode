// async function test1() {
//     await setTimeout(()=>{
//         console.log('1')
//     }, 1000)
//     let b = await 2
//     console.log(b)
// }
// test1()

// async function test2() {
//     let a = await new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             console.log('1')
//             resolve()
//         }, 1000)
//     })
//     let b = await new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             console.log('2')
//             resolve()
//         }, 2000)
//     })
//     let c = 3
//     console.log(c)
// }
// test2()

async function test1() {
    await setTimeout(()=>{
        console.log('1')
    }, 1000)
    console.log('3')
}

async function test2() {
    await new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('2')
            resolve()
        }, 2000)
    })
    console.log('3')
}

async function test3() {
    await setTimeout(()=>{
        console.log('1')
    }, 1000)
    await new Promise((resolve, reject)=>{
        setTimeout(()=>{
            console.log('2')
            resolve()
        }, 2000)
    })
    console.log('3')
}

// test1()
// test2()
test3()