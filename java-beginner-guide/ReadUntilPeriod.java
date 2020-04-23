class ReadUntilPeriod {

    public static void main(String[] args)
        throws java.io.IOException {
        
        int numSpaces = 0;
        char ch;
        System.out.println("Enter some characters and a period at the end: ");
        do {
            ch = (char) System.in.read();
            if (ch == ' ') {
                numSpaces++;
            }
        } while (ch != '.');

        System.out.println("Num Spaces: " + numSpaces);
    }
}
