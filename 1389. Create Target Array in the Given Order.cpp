class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        int n = nums.size();
        vector<int> res;
        // res.push_back(nums[i]);
        for(int i=0;i<n;i++){
            res.insert(res.begin()+index[i],nums[i]);
        }
        return res;
    }
};
