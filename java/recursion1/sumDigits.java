public int sumDigits(int n) {
  if (n == 0){
	return 0;
  }
  
  return sumDigits(n/10) + n % 10;
}
