//Method One
let insertSort = nums => {
    for (let i = 1; i < nums.length; i++){
        let index = i;
        let j = i - 1;
        while (j>=0){
            if (nums[index]<nums[j]){
                [nums[index], nums[j]] = [nums[j], nums[index]]
                index = j;
            }
            j--;
        }
    }
}

//Method Two
let insertSort2 = nums => {
    for (let i = 1; i < nums.length; i++){
        temp = nums[i];
        let j = i - 1;
        while (j>=0 && nums[j]>temp){
            nums[j+1] = nums[j];
            j--;
        }
        nums[j+1] = temp;
    }
}

let nums = [3,2,5,1,4,3,0,8,2]
insertSort2(nums)
console.log(nums)