import hashlib, sys, re

alphanum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_".encode()

def cstrip(lines):
	d = "".encode()
	for l in lines:
		l = re.sub("#.*".encode(), "".encode(), l)
		l = re.sub("//.*".encode(), "".encode(), l)
		d += l + " ".encode()
	d = re.sub("\/\*.*?\*/".encode(), "".encode(), d) # remove /* */ comments
	d = d.replace("\t".encode(), " ".encode()) # tab to space
	d = re.sub("  *".encode(), " ".encode(), d) # remove double spaces
	d = re.sub("".encode(), "".encode(), d) # remove /* */ comments

	d = d.strip()

	# this eats up cases like 'n {'
	i = 1
	while i < len(d)-2:
		if d[i:i + 1] == " ".encode():
			if not (d[i - 1:i] in alphanum and d[i+1:i + 2] in alphanum):
				d = d[:i] + d[i + 1:]
		i += 1
	return d

f = "".encode()
for filename in sys.argv[1:]:
	f += cstrip([l.strip() for l in open(filename, "rb")])

hash = hashlib.md5(f).hexdigest().lower()[16:]
# TODO: refactor hash that is equal to the 0.5 hash, remove when we 
# TODO: remove when we don't need it any more
if hash == "8755162e69711f98":
	hash = "b67d1f1a1eea234e"
print('#define GAME_NETVERSION_HASH "%s"' % hash)
