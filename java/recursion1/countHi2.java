public int countHi2(String str) {
  if (str.length() < 2)
	return 0;
  if (str.charAt(0) == 'x' && str.length() >= 3 && str.substring(1, 3).equals("hi"))
	return countHi2(str.substring(3));
  if (str.substring(0, 2).equals("hi"))
	return 1 + countHi2(str.substring(1));
  return countHi2(str.substring(1));
}
