let quickSort = (nums, start, end) => {
    let [left, right] = [start, end - 1]
    if (left >= right) return

    let axis = nums[end];
    while (left < right){
        while (nums[left] <= axis && left < end) left++
        while (nums[right] > axis && right > 0) right--

        if (left < right) [nums[left], nums[right]] = [nums[right], nums[left]]
    }
    [nums[left], nums[end]] = [nums[end], nums[left]]
    quickSort(nums, start, left-1);
    quickSort(nums, left, end);
}

let nums = [9,8,7,6,5]
quickSort(nums, 0, nums.length-1)
console.log(nums)