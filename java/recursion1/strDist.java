public int strDist(String str, String sub) {
  if (str.equals(""))
    return 0;
  
  int subLen = sub.length();
  int strLen = str.length();
  
  if (subLen > strLen)
    return 0;
  
  if (str.substring(0, subLen).equals(sub)) {
    if (str.substring(strLen - subLen).equals(sub)) {
      return str.length();
    } else {
      return strDist(str.substring(0, strLen-1), sub);
    }
  }
  return strDist(str.substring(1), sub);
  
}
