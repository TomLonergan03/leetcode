struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  int maxDepth(TreeNode *root) {
    if (!root) {
      return 0;
    }
    const auto left = root->left ? maxDepth(root->left) : 0;
    const auto right = root->right ? maxDepth(root->right) : 0;
    return (left > right ? left : right) + 1;
  }
};
