simpleGenderPredictor
------------

Download historical baby names from the United States Social Security Administration website and use the frequency to predict the gender given a name (case insensitive). Works with Python 2 and 3.

```python
from simpleGenderPredictor import simpleGenderPredictor
p = simpleGenderPredictor.simpleGenderPredictor()

p.predict_name('john')
('M', 0.9957609676907682)

p.predict_name('no_name')
('Unknown', None)

p.predict_name('Jane')
('F', 0.9969194911455744)
```