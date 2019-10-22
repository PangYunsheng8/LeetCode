var Rx = require('rxjs/Rx');

var subject = new Rx.Subject();
subject.next('previous');

const subscription1 = subject.subscribe(x => {
  console.log('From subscription 1:', x);
});

subject.next('after subscription1');

const subscription2 = subject.subscribe(x => {
  console.log('From subscription 2:', x);
});

subject.next('after subscription2');