# Keyboard Light Binary Counter

## Overview

This script utilizes the `pyautogui` library to simulate key presses on the keyboard, specifically targeting the Scroll Lock, Caps Lock, and Num Lock keys. It counts from 0 to 7 in binary (3-bit), represented by the state of these keys, and visually indicates the counting process through the keyboard lights.

## Requirements

- Python 3.x
- `pyautogui` library
- A keyboard with Scroll Lock, Caps Lock, and Num Lock keys lights

### Installation of Dependencies

You can install the `pyautogui` library using pip:

```bash
pip install pyautogui
```

Behavior
1. Scroll Lock is toggled at each iteration of the count.
2. Caps Lock is toggled on every odd count starting from 2.
3. Num Lock is toggled on the fifth count.
4. On reaching the eighth count, it waits for a second and calls the `toggle_locks_off()` function to reset the state of the locks.
5. Each count iteration includes a pause of 0.9 seconds, except for the last count, which has a 1-second pause before resetting.

### Execution
The script contains a loop that runs the `count()` function 10 times, allowing the counting sequence to be repeated.

#### Main Loop
```
for _ in range(10):
    count()
```
### Example Output
| Decimal | Binary | Num Lock | Caps Lock | Scroll Lock | Lights        |
|---------|--------|----------|-----------|--------------|---------------|
| 0       | 000    | Off      | Off       | Off          | 🔴🔴🔴         |
| 1       | 001    | On       | Off       | Off          | 🔴🔴🟢         |
| 2       | 010    | Off      | On        | Off          | 🔴🟢🔴         |
| 3       | 011    | On       | On        | Off          | 🔴🟢🟢         |
| 4       | 100    | Off      | Off       | On           | 🔴🔴🟢         |
| 5       | 101    | On       | Off       | On           | 🟢🔴🟢         |
| 6       | 110    | Off      | On        | On           | 🔴🟢🟢         |
| 7       | 111    | On       | On        | On           | 🟢🟢🟢         |



### Note
Ensure that no other application is using the Scroll Lock, Caps Lock, or Num Lock keys during execution, as this could interfere with the script's intended functionality.
