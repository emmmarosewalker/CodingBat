public int countAbc(String str) {
  if (str.length() < 3)
	return 0;
  if (str.substring(0, 2).equals("ab"))
	if (str.charAt(2) == 'c' || str.charAt(2) == 'a')
	  return 1 + countAbc(str.substring(2));
  return countAbc(str.substring(1));
}
