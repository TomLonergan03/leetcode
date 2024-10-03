#include <string>
#include <vector>

class TrieNode {
public:
  TrieNode(char key) : key(key), children(), end_of_word(false) {};
  char key;
  bool end_of_word;
  std::vector<TrieNode *> children;
};

class Trie {
public:
  Trie() { root = new TrieNode(0); }
  ~Trie() { destroy(root); }

  void insert(std::string word) {
    auto node = root;
    for (const auto c : word) {
      printf("%c\n", c);
      TrieNode *loc = nullptr;
      for (auto child : node->children) {
        if (child->key == c) {
          loc = child;
          break;
        }
      }
      if (loc == nullptr) {
        TrieNode *new_node = new TrieNode(c);
        node->children.push_back(new_node);
        node = new_node;
      } else {
        node = loc;
      }
    }
    node->end_of_word = true;
  }

  bool search(std::string word) {
    auto node = root;
    for (const auto c : word) {
      TrieNode *loc = nullptr;
      for (auto child : node->children) {
        if (child->key == c) {
          loc = child;
          break;
        }
      }
      if (loc == nullptr) {
        return false;
      }
      node = loc;
    }
    return node->end_of_word;
  }

  bool startsWith(std::string prefix) {
    auto node = root;
    for (const auto c : prefix) {
      TrieNode *loc = nullptr;
      for (auto child : node->children) {
        if (child->key == c) {
          loc = child;
          break;
        }
      }
      if (loc == nullptr) {
        return false;
      }
      node = loc;
    }
    return true;
  }

private:
  void destroy(TrieNode *root) {
    for (auto child : root->children) {
      if (child) {
        destroy(child);
      }
    }
    delete root;
  }

  TrieNode *root;
};
