simpleGenderPredictor
------------

Download historical baby names from SSA.gov website and use the frequency to predict the gender given a name. Works with Python 2 and 3.

```python
from simpleGenderPredictor import simpleGenderPredictor
p = simpleGenderPredictor.simpleGenderPredictor()
p.predict_name('john')

('M', 0.9957609676907682)
```