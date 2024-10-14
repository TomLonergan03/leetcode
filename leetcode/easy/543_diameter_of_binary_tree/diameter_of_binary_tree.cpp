#include <algorithm>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

struct Result {
  int best_diameter;
  int height;
};

class Solution {
public:
  int diameterOfBinaryTree(TreeNode *root) { return dfs(root).best_diameter; }

  // best, height
  Result dfs(TreeNode *root) {
    if (!root) {
      return {0, 0};
    }
    Result result = {0, 0};

    int left = 0;
    int right = 0;
    if (root->left) {
      result = dfs(root->left);
      left = result.height;
    }
    if (root->right) {
      const auto [diameter, height] = dfs(root->right);
      result.best_diameter = std::max(result.best_diameter, diameter);
      result.height = std::max(result.height, height);
      right = height;
    }
    result.best_diameter = std::max(result.best_diameter, left + right);
    result.height++;
    return result;
  }
};
