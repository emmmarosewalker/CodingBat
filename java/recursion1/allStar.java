public String allStar(String str) {
  if (str.length() == 0)
	return str;
  if (str.length() > 1)
	return str.charAt(0) + "*" + allStar(str.substring(1));
  return str.charAt(0) + allStar(str.substring(1));
}
