import sys
print(sys.path)
sys.path = sys.path[-3:]
print(sys.path)

import skmisc  # noqa: E402
import skmisc.loess  # noqa: E402, F401
