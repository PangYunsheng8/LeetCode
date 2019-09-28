class ListNode{
    constructor(val, next){
        this.val = val;
        this.next = next;
    }
}

let linkedList = new ListNode() //哑结点

linkedList.next = new ListNode(1)
linkedList.next.next = new ListNode(2)

for (let t = linkedList.next; t; t=t.next){
    console.log(t.val)
}
