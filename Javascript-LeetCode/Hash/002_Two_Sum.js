var twoSum = function(nums, target) {
    let mydic = {}
    for (let i = 0; i < nums.length; i++){
        let value = target - nums[i]
        if (value in mydic){
            return [mydic[value], i]
        } else{
            mydic[nums[i]] = i
        }
    }
};

let nums = [3,2,4];
let target = 6;

let index = twoSum(nums, target)
console.log(index)