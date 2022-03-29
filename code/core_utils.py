
def escapeString(val, maxLength=254):
	"""
		Quotes several characters and removes "\\\\n" and "\\\\0" to prevent XSS injection.
		:param val: The value to be escaped.
		:type val: str
		:param maxLength: Cut-off after maxLength characters. A value of 0 means "unlimited".
		:type maxLength: int
		:returns: The quoted string.
		:rtype: str
	"""
	val = str(val).strip() \
		.replace("<", "&lt;") \
		.replace(">", "&gt;") \
		.replace("\"", "&quot;") \
		.replace("'", "&#39;") \
		.replace("(", "&#040;") \
		.replace(")", "&#041;") \
		.replace("=", "&#061;") \
		.replace("\n", "") \
		.replace("\0", "")

	if maxLength:
		return val[0:maxLength]

	return val