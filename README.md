# eaxtension
method encapsulator for Python


## Import eaxtension
- copy `eaxtension.py` file in your directory
- write this code in your file
```python
from eaxtension import <class_name>
```


## Class list
- LogE: print logging message on your console.
- jsonE: read and dump json file.
- timeE: return formatted time in your code.


> ### LogE

  ### How to use
  ```python
  LogE.<attr>(<log name: str>, <log content>)
  ```
  type of log content will change automatically to string.

  ### attributes
  - LogE.d: print common log message on your console.
  - LogE.g: print green colored log message on your console.
  - LogE.e: print red colored error message on your console.
  - LogE.E: print red colored background error message on your console.
  - LogE.t: print type of <log content> on your console.
  - LogE.T: print type of <log content> with contents of <log content> on your console.

  
> ### jsonE
  
  ### modes
  - read only mode
  ```python
  json_content = jsonE.load(<file_name: str>, **<attr>)
  ```
  - dump mode
  ```python
  jsonE.dumps(<file_name: str>, <dump_content: dict>, **<attr>)
  ```
  
  - merge mode
  ```python
  jsonE.merge(<file_name: str>, <merge_content: dict>)
  ```
  
  - attributes
    - silent = <bool>
    > if silent is True, jsonE doesn't print progress Log.
  
> ### timeE
  
  ### modes
  - formatted time mode
  ```python
  time_data = timeE.geta()
  ```
  - custom format mode
  ```python
  time_data = timeE.getc(*<attr: str>)
  ```
   - attributes
     - dow: return abbreviation of 'day of week'
     - DOW: return 'day of week'
     - dowN: return number of 'day of week'
     - day: return 'day'
     - mon: return abbreviation of 'month'
     - MON: return 'month'
     - monN: return number of 'month'
     - year: return abbreviation of 'year'
     - YEAR: return 'year'
     - 24hr: return 'time' to 24hr format
     - 12hr: return 'time' to 12hr format
     - ampm: return 'AM/PM'
     - min: return 'minute'
     - sec: return 'second'
     - week of year: return 'week of year'
     - time all: return all of time data
     - date all: return all of date data
     - time and date: return all of time data and date data
