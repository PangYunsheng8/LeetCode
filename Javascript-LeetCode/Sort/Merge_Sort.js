let mergeSort = (nums, start, end) =>{

    if (start == end){
        return
    }

    let mid = Math.floor((start + end) / 2)

    mergeSort(nums, start, mid)
    mergeSort(nums, mid+1, end)

    let arr = merge(nums.slice(start,mid), nums.slice(mid+1,end))
    console.log(arr)
}

let merge = (a, b) => {
    let arr = []
    let [l, r] = [0, 0]

    while (l < a.length && r < b.length){
        if (a[l] <= b[r]){
            arr.push(a[l])
            l++
        }else{
            arr.push(b[r])
            r++
        }
    }
    return arr
}

let nums = [3,2,5,1,4,3,0,8,2]
mergeSort(nums, 0, nums.length - 1)
console.log(nums)