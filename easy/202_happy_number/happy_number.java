import java.util.HashSet;

class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<Integer>();
        while (true) {
            n = squareDigits(n);
            if (n == 1) {
                return true;
            }
            if (set.contains(n)) {
                return false;
            }
            set.add(n);
        }
    }

    private int squareDigits(int n) {
        int result = 0;
        while (n > 0) {
            result += Math.pow(n % 10, 2);
            n /= 10;
        }
        return result;
    }
}