"""

Data structures ---> different ways of organizing data on a computer that can be used effectively

What is an algorithm?:
    -- in life: set of steps to accomplish a task
    -- in CS:   set of rules for a computer programm to accomplish a task

What makes a good algorithm?:
    -- correctness
    -- efficiency

Why are Data Structures and Algorithms important?:
    -- they organize the data
    -- they optimize data proccessing
    -- they allow devs to develop memory and time efficient apps 

Types of DS:
    -- primitive     ---> they are built into the programming language [int, float, char, string, bool]
    -- non primitive ---> user defined ds, they are a combination of two or more primitive data structures
        -- linear
            -- data items are arranged in memory in a linear, sequential manner 
            -- they can be either static (ex. array) or dynamic (ex. stack, queue, ll)
            -- sizes and associted memory locations are fixed
        -- non linear
            -- data items are connected to several other items
            -- they are not organized sequentially (ex. tree, graph)

Types of algos:
    -- simple recursive algorithms
        -- the recursion acts as a loop 
    -- divide and conquer algorithms
        -- 1st part: divide the problem into smaller subproblems of the same type and save those problems recursively
        -- 2nd part: combine the solutions to the subproblems into a solution to the original problem (ex. quicksort)
    -- dynamic programming algorithms
        -- they work based on memorization ---> they remember the past results and use them to find new results
        -- used for optimization problems
    -- greedy algorithms
        -- they work based on hope ---> they hope that by choosing a local optimal solution at each step, they will end up a global optimal solution
        -- they take the best they can, without worrying about future consequences
    -- brute force algorithms
        -- they try all possibilities until a satisfactory solution is found (ex. Dijkstra's algorithm)
    -- randomized  algorithms
        -- they use a random number AT LEAST ONCE during the computation to make a decision (ex. quicksort)

"""