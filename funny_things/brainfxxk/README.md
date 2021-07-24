# BrainFxxk
## Description
The "BrainFxxk" is kind of programming language created in 1993 by Urban Müller [wiki](https://en.wikipedia.org/wiki/Brainfuck). It uses 8 characters as commands. This language is extremely minimize but not easy to understand. 

# How it works
## Commands
1. `<` and `>`: they are used to move left/right the data pointer
    ```
    # pointer points to 2nd data
    | 0 | 0 | 0 | 0 | 0 |
          ^
    # after < command, it will pointer to the first data
    | 0 | 0 | 0 | 0 | 0 |
      ^
    # then > command, it will bring the pointer back to the second data
    | 0 | 0 | 0 | 0 | 0 |
          ^  
    ```
2. `+` and `-`: they are used to increment or decrement the actual pointed data
    ```
    # actual data is 3
    | 0 | 3 | 0 |
          ^
    # after + command, it the second data becomes 4
    | 0 | 4 | 0 |
          ^
    # then - command, it the second data is back to 3
    | 0 | 3 | 0 |
          ^ 
    ```
3. `[` and `]`: conditional operations.
    ```
    [ : if the current data is 0, jump to the operation after `]`, otherwise continue the next operations
    ] : back to `[`
    ```
4. `,` and `.`: input and output commands
    ```
    . : output the data as ASCII character
    , : read input and save in the current pointer
    ```

### Example
```
# from https://en.wikipedia.org/wiki/Brainfuck
++       Cell c0 = 2
> +++++  Cell c1 = 5

[        Start your loops with your cell pointer on the loop counter (c1 in our case)
< +      Add 1 to c0
> -      Subtract 1 from c1
]        End your loops with the cell pointer on the loop counter

At this point our program has added 5 to 2 leaving 7 in c0 and 0 in c1
but we cannot output this value to the terminal since it is not ASCII encoded.

To display the ASCII character "7" we must add 48 to the value 7.
We use a loop to compute 48 = 6 * 8.

++++ ++++  c1 = 8 and this will be our loop counter again
[
< +++ +++  Add 6 to c0
> -        Subtract 1 from c1
]
< .        Print out c0 which has the value 55 which translates to "7"!
```