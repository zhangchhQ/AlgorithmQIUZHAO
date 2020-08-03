class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ret_list = []   # 存放每一行皇后的对应列数
        self.col_set = set()
        self.pie_set = set()
        self.na_set = set()
        self.dfs(0, n, [])
        return self.generate_result(n)
    # 遍历每一行，如果该坐标符合不在攻击范围，加入result，如果遍历所有行的结果都可以，递归终止
    def dfs(self, row, n, cur_states):
        # terminator
        if row >= n:
            self.ret_list.append(cur_states)
            return
        # current process
        for col in range(n):
            # 类 dfs判断visited
            if col in self.col_set or col+row in self.na_set or col-row in self.pie_set:
                continue
                # go die
            # 类visited.add
            self.col_set.add(col)
            self.na_set.add(col+row)
            self.pie_set.add(col-row)
            # drill down
            self.dfs(row+1, n, cur_states+[col])
            # reverse
            # 下探回来后要清楚上一层的皇后值，以便找新的一组皇后
            self.col_set.remove(col)
            self.na_set.remove(col+row)
            self.pie_set.remove(col-row)
    def generate_result(self, n):
        board = []
        for res in self.ret_list:
            for i in res:
                print(i)
                board.append("." * i + "Q" + "." * (n-1-i))
        return [board[i: i + n] for i in range(0, len(board), n)]