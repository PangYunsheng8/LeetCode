var Rx = require('rxjs/Rx');

let observable = Rx.Observable.create(function(observer){
    try{
        observer.next('Faker')
        observer.next('Uzi')
        observer.complete()
        throw 'An error!'
    } catch(e) {
        observer.error(e)
    }
})

let observer = {
    next: function(value){ console.log('this is ' + value)},
    error: function(error){ console.log('Error: ' + error)},
    complete: function() { console.log('complete') }
}
console.log('start')
// observable.subscribe(function(value){
//     console.log(value)
// })
observable.subscribe(observer)
console.log('end')