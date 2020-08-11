# PyVirusShare
A Python 3 library to interact with VirusShare API v2. 

## Installation
```
pip3 install virusshare
```

## Usage
### Library Usage Demo
```python
from virusshare import VirusShare

v = VirusShare('<api_key>')
result = v.get_info('a1ac533baaf7de1dae53cf5b465aeca28a7f20bdfc79e5a0a39437dd728c231f')
print(result['data'])
"""
{
    "filetype": "PE32 executable (DLL) (console) Intel 80386 Mono/.Net assembly, for MS Windows",
    "md5": "985d5ff3a3ede247c561c0ea4cedd342",
    "exif": {
        "CharacterSet": "Unicode",
        "CodeSize": 291328,
        "Comments": "Mono.Security.dll",
        "CompanyName": "MONO development team",
        "EntryPoint": "0x2000",
        "FileDescription": "Mono.Security.dll",
        "FileFlags": "(none)",
        "FileFlagsMask": "0x003f",
        "FileOS": "Win32",
        "FileSize": "286 kB",
...
..
.
"""

```

### Command Line Usage
```
$ PyVirusShare download -k <api_key> -hs <hash_string> -o <output_dir>
```

## Documentation