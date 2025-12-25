def dec_to_any_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result or "0"


def any_base_to_dec(string):
  prefix=string[:2].lower()
  if prefix in ('0b','0o','0x') or string.isdigit():
    return int(string,0)
  else:
    return "Use prefix like '0b', '0o' or '0x'"
    
