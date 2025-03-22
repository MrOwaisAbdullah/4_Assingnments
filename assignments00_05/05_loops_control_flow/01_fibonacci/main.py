MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  
    next_term = 1
    print("\n\033[01mHere are the first 10000 Fibonacci numbers:\033[0m")
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    print("\n")

if __name__ == '__main__':
    main()