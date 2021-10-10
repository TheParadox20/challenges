class exponential {
    static public int power(int x, int y){
        int omega=x;
        for (int i = 0; i < y-1; i++) {
            omega *=x;
        }
        return omega;
    }
    public static void main(String[] args) {
        System.out.println(power(5,3));        
    }    
}