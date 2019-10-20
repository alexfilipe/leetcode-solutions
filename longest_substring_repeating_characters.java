import java.util.HashSet;

class longest_palindromic_substring {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();

        int maxLength = 0;

        for (int i = 0; i < n; i++) {

            HashSet<Character> foundLetters = new HashSet();
            int substringLength = 0;
            int currentPosition = i;
            char currentChar = s.charAt(currentPosition);;
            //System.out.println("Starting at position " + currentPosition);

            while(!foundLetters.contains(currentChar) && currentPosition < n) {
               //System.out.println("currentChar = " + currentChar);

                if (!foundLetters.contains(currentChar)) {
                    foundLetters.add(currentChar);
                    substringLength++;
                    //System.out.println("Doesn't contain " + currentChar + ", new length = " + substringLength);
                }

                currentPosition++;
                if(currentPosition < n) {
                    currentChar = s.charAt(currentPosition);
                }
            }

            if(maxLength < substringLength) {
                maxLength = substringLength;
            }

            //System.out.println("maxLength = " + maxLength);
        }

        return maxLength;
    }
}
