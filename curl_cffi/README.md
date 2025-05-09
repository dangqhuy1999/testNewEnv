## Link tutorial: https://github.com/lexiforest/curl_cffi/tree/main


## **Usage**
curl_cffi comes with a low-level curl API and a high-level requests-like API.

## **requests-like**

### v0.9:

```python
from curl_cffi import requests
r = requests.get("https://tls.browserleaks.com/json", impersonate="chrome")
```

### v0.10:

```python
import curl_cffi

# Notice the impersonate parameter
r = curl_cffi.get("https://tls.browserleaks.com/json", impersonate="chrome")

print(r.json())
# output: {..., "ja3n_hash": "aa56c057ad164ec4fdcb7a5a283be9fc", ...}
# the js3n fingerprint should be the same as target browser

# To keep using the latest browser version as `curl_cffi` updates,
# simply set impersonate="chrome" without specifying a version.
# Other similar values are: "safari" and "safari_ios"
r = curl_cffi.get("https://tls.browserleaks.com/json", impersonate="chrome")

# Randomly choose a browser version based on current market share in real world
# from: https://caniuse.com/usage-table
# NOTE: this is a pro feature.
r = curl_cffi.get("https://example.com", impersonate="realworld")

# To pin a specific version, use version numbers together.
r = curl_cffi.get("https://tls.browserleaks.com/json", impersonate="chrome124")

# To impersonate other than browsers, bring your own ja3/akamai strings
# See examples directory for details.
r = curl_cffi.get("https://tls.browserleaks.com/json", ja3=..., akamai=...)

# http/socks proxies are supported
proxies = {"https": "http://localhost:3128"}
r = curl_cffi.get("https://tls.browserleaks.com/json", impersonate="chrome", proxies=proxies)

proxies = {"https": "socks://localhost:3128"}
r = curl_cffi.get("https://tls.browserleaks.com/json", impersonate="chrome", proxies=proxies)

```


## **Sessions**

### v0.9:

```python
from curl_cffi import requests

s = requests.Session()
```

### v0.10:

```python
s = curl_cffi.Session()

# httpbin is a http test website, this endpoint makes the server set cookies
s.get("https://httpbin.org/cookies/set/foo/bar")
print(s.cookies)
# <Cookies[<Cookie foo=bar for httpbin.org />]>

# retrieve cookies again to verify
r = s.get("https://httpbin.org/cookies")
print(r.json())
# {'cookies': {'foo': 'bar'}}
```

