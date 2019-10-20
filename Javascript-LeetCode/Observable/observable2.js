var Rx = require('rxjs/Rx');

var myObservable = Rx.Observable.create(function (observer) {
  setTimeout(() => {
    observer.next(1);
  }, 1000);

  setTimeout(() => {
    observer.next(2);
  }, 2000);

  setTimeout(() => {
    observer.next(3);
  }, 3000);
  setTimeout(() => {
    observer.next(4);
    observer.complete();
  }, 4000);
});

var observer1 = {
  next: x => console.log('Observer1 got a next value: ' + x),
  error: err => console.error('Observer1 got an error: ' + err),
  complete: () => console.log('Observer1 got a complete notification'),
};

var subscription1 = myObservable.subscribe(observer1);

var subscription2 = myObservable.subscribe({
  next: x => console.log('Observer2 got a next value: ' + x),
  error: err => console.error('Observer2 got an error: ' + err),
  complete: () => console.log('Observer2 got a complete notification'),
});

setTimeout(()=>{
  subscription1.unsubscribe();
  subscription2.unsubscribe();
},5000)
