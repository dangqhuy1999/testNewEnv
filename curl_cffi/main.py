import curl_cffi

r = curl_cffi.get("https://baomoi.com", impersonate="chrome124")
print(r)
