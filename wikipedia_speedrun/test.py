from unittest import result
from mediawiki import MediaWiki
wiki = MediaWiki()

w = wiki.opensearch('python', results=1)
print(w[-1][-1])