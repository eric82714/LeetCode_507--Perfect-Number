bool checkPerfectNumber(int num){
    if(num == 1) return false;
        
    int tmp = num-1, divisor = 2;
        
    while(divisor * divisor < num) {
        if(num % divisor == 0)
            tmp = tmp - divisor - (num / divisor);             
        divisor ++;
    }
            
    return tmp == 0;

}
