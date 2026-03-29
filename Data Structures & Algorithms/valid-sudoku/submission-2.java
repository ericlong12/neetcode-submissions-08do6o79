class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> columns = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for (int row = 0; row < 9; row++) {  // Corrected loop variable
            for (int column = 0; column < 9; column++) {  // Initialized column variable
                char currentCell = board[row][column];  // Corrected variable names
                if (currentCell == '.') {  // Corrected comparison operator
                    continue;
                }
                if (rows.getOrDefault(row, new HashSet<>()).contains(currentCell)
                        || columns.getOrDefault(column, new HashSet<>()).contains(currentCell)
                        || squares.getOrDefault((row / 3) * 3 + column / 3, new HashSet<>()).contains(currentCell)) {
                    return false;
                }

                columns.computeIfAbsent(column, k -> new HashSet<>()).add(currentCell);  // Corrected variable names and parentheses
                rows.computeIfAbsent(row, k -> new HashSet<>()).add(currentCell);
                squares.computeIfAbsent((row / 3) * 3 + column / 3, k -> new HashSet<>()).add(currentCell);  // Corrected formula
            }
        }
        return true;
    }
}
