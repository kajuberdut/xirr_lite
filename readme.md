# xirr_lite

xirr_lite contains a number of example implimentation of a xirr which function in python either with or without dependencies.
This example MIGHT be useful if you are seeking a zero dependency solution OR if you already have numpy as a dependency and are seeking to avoid adding others. Rather that install xirr_lite, the best result probably comes from directly copying an implimentation.


## Installation & Usage
Note: You should probably not install this package -- better alternatives exist if you want to take on an external dependency -- for example, [a very fast rust implimentation with a python wrapper](https://github.com/Anexen/pyxirr).

However, if you wish to install anyways you can do so with:

`pip install xirr_lite`

Or, to also install Numpy for faster and more robust array methods:

`pip install xirr_lite[optimize]`

### Usage
``` python
import datetime

from xirr_lite import xirr

    def mdt(iso_fmt: str) -> datetime.datetime:
        return datetime.datetime.fromisoformat(iso_fmt)

    result = xirr(
        [
            (mdt("2020-01-01"), -5000),
            (mdt("2020-04-07"), 500),
            (mdt("2020-08-05"), 500),
            (mdt("2020-09-01"), 500),
            (mdt("2020-12-01"), 1000),
            (mdt("2021-01-02"), 1000),
            (mdt("2021-04-05"), 1000),
            (mdt("2021-08-09"), 1500),
        ]
    )
    print(result)
    # 0.19069352136108342

```

## Credits
__Note that these credits do not represent an endorsement or promotion by these entities__
1. The [SciPy](https://github.com/scipy/scipy) team for the code found in xirr_lite.newton.
2. [peliot](https://github.com/peliot) for secant_method, xnpv and xirr.