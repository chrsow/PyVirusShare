# PyVirusShare

A python library to interact with Virusshare API v2. 

## Installation

```
pip install virusshare
```

## Usage
### Library Usage Demo
```python
from virusshare import VirusShare

v = VirusShare('<api_key>')
result = v.get_info('778d0b014c58e8130804c56e9579a97eb77eee79')
print(result['data'])
"""
{
    "filetype": "Zip archive data, at least v2.0 to extract",
    "sha1": "778d0b014c58e8130804c56e9579a97eb77eee79",
    "ssdeep": "393216:Fap6O7g0jcBlDxonTFwEf0Hez/3+xpT4WWFobJ2p1ok:RKg0jcBlDxohzMHQupWFobY",
...
"""

```

### Command Line Usage
TODO

## Documentation