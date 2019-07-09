# Minimum-Edit-Distance
用python 寫的 Minimum-Edit-Distance

說明:
  利用遞迴完成minimum edit distance
 
程式說明:

  1. MED_re(s1, s2, s1i, s2i)
  
  2. 會從 s1[s1i] 和 s2[s2i] 將兩個序列的最小編輯次數一個一個比對出來
  
  3. 編輯有3個種類的action : delete insert substitude
  
  4. 或是不編輯action 為 leave 留下原來就有的字元
  
  5. 假設在 s1[s1i] 和 s2[s2i] 的狀況下，有可能會採取 delete insert substitude leave的動作
  
          a. delete_cost = MED_re(s1, s2, s1i+1, s2i) + DELETE_COST ， 將原序列的字減掉   並且繼續執行MED
          
          b. insert_cost = MED_re(s1, s2, s1i, s2i+1) + INSERT_COST ， 將新的序列的字增加 並且繼續執行MED
          
          c. substitude_cost = MED_re(s1, s2, s1i+1, s2i+1) + SUBSTITUDE_COST  ， 將把字元換掉 並且繼續執行MED
          
          d. leave_cost = MED_re(s1, s2, s1i+1, s2i+1) + LEAVE_COST  ， 將把字元留著 並且繼續執行MED
          
          e. 當其中一個消耗最少的時候，他就是MED
          
  6. 當原字串已經達到結尾了，新字串還沒比對完，表示新字串剩下的部分要全部插入
  
  7. 當新字串達到結尾了，原字串還沒比對完，表示原字串剩下的部分要全部刪掉
  
  8. 最後將cost加總起來
  
  9. 在選去不同action 路徑時 ， 將不同的action 記錄到 action_mat ，最後可以找出，其中一條最少編輯的路徑的 action string
  
  10. 透過 take action 可以透過 action string 將 原序列，轉變為 新序列
  
  11. 時間複雜度: O(L*M), L = len(s1) M = len(s2)
  
  12. 空間複雜度: O(L*M), L = len(s1) M = len(s2)
