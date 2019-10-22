var Rx = require('rxjs/Rx');

var subject = new Rx.Subject();
console.log('1')
setTimeout(()=>{
  subject.next(3);
}, 500)
subject.subscribe({
  next: (v) => console.log('observerA: ' + v)
});
subject.subscribe({
  next: (v) => console.log('observerB: ' + v)
});
console.log('2')
setTimeout(()=>{
  subject.next(1);
}, 1000)
setTimeout(()=>{
  subject.next(2);
}, 2000)