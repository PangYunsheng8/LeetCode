let bubbleSort = nums => {
    for (let i = 0; i < nums.length - 1; i++){
        for (let j = 0; j < nums.length - 1 - i; j++){
            if(nums[j] > nums[j+1])
                [nums[j], nums[j+1]] =  [nums[j+1], nums[j]]
        }
    }
}

let nums = [3,2,5,1,4,3,0,8,2]
bubbleSort(nums)
console.log(nums)