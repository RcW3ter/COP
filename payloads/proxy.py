import socks

s = socks.socksocket() 
s.set_proxy(socks.SOCKS5, "localhost")

s.connect('www.google.com')