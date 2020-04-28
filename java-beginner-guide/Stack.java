class Stack {
    char[] contents;
    int head = 0;
    
    Stack(int size) {
        contents = new char[size];
    }

    void push(char c) {
        contents[head] = c;
        head++;
    }

    char pop() {
        char popped = contents[head-1];
        contents[head-1] = ' ';
        head--;
        return popped;
    }
    
    void show() {
        for (var c : contents) {
            System.out.print(c + " ");
        }
        System.out.println();
    }
}

// Run java StackDemo
