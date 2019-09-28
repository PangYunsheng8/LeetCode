var twoSum = function(nums, target) {
    let hashTable = {}
    for (let i = 0; i < nums.length; i++){
        hashTable[nums[i]] = i;
    }
    let hashKey = []
    for (key in hashTable){
        hashKey.push(key)
    }

    let index = [];
    for (let i = 0; i < nums.length - 1; i++){
        let value = target - nums[i]
        if (value in hashKey && value != nums[i]){
            index.push(i);
            index.push(hashTable[value]) 
        }
    }
    return index
};

let nums = [3,2,4];
let target = 6;

let index = twoSum(nums, target)
console.log(index)