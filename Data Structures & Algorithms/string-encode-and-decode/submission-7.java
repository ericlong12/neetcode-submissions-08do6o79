class Solution {

    public String encode(List<String> strs) {
        // we use this method to help us build a string easily
        StringBuilder encodedString = new StringBuilder();
        for (String string : strs){
            encodedString.append(string.length()).append('#').append(string);
        }
        return encodedString.toString();
        

    }

    public List<String> decode(String string) {
        // we make a string list
        List<String> list = new ArrayList<>();
        int i = 0;

        // go through the whole given list
        while (i < string.length()) {
            int j = i;
            // go through each char in the string
            while (string.charAt(j) != '#') j++;

            // valueOf method convers a string into an int
            // substring is begining inclusive and ending exclusive

            // i is the length of the string. j is right after i, it 
            // is the # so which seperates each string.
            int length = Integer.valueOf(string.substring(i,j));

            // we set i equal to the next int (aka string length)
            // we add j + 1  so we can get 1 past the # which seperates the string
            // after we add the length of the string we just decoded
            // so that we arrive at the start of the next string
            i = j + 1 + length;
            list.add(string.substring(j+1, i));

        }
        return list;


    }
}


// to solve this problem we should have a keyword 
// and the amount of characters in each string

// an example can be to use # to seperate values and an int to 
// not the string length.

// ex.  "5#hello3#tac"

// use StringBuilder encodedString = new StringBuilder();