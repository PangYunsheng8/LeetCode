let selectSort = nums => {
    for (let i = 0; i < nums.length - 1; i++){
        let minIndex = i;
        for (let j = i; j < nums.length; j++){
            if (nums[j] < nums[minIndex])
                minIndex = j;
        }
        [nums[i], nums[minIndex]] = [nums[minIndex], nums[i]]
    }
}

let nums = [3,2,5,1,4,3,0,8,2]
selectSort(nums)
console.log(nums)