def goodVsEvil(good, evil):
  good = good.split(' ')
  evil = evil.split(' ')
  good = goodWorth(good)
  evil = evilWorth(evil)
  if good > evil:
    print("Battle Result: Good triumphs over Evil")
  elif good < evil:
    print("Battle Result: Evil eradicates all trace of Good")
  elif good == evil:
    print("Battle Result: No victor on this battle field")

def goodWorth(arr):
  arr[0] = {
    'Quantity': int(arr[0]),
    'Worth': 1
    }
  arr[1] = {
    'Quantity': int(arr[1]),
    'Worth': 2
    }
  arr[2] = {
    'Quantity': int(arr[2]),
    'Worth': 3
    }
  arr[3] = {
    'Quantity': int(arr[3]),
    'Worth': 3
  }
  arr[4] = {
    'Quantity': int(arr[4]),
    'Worth': 4
    }
  arr[5] = {
    'Quantity': int(arr[5]),
    'Worth': 10}
  return gvesum(arr)

def evilWorth(arr):
  arr[0] = {
    'Quantity': int(arr[0]),
    'Worth': 1
    }
  arr[1] = {
    'Quantity': int(arr[1]),
    'Worth': 2
    }
  arr[2] = {
    'Quantity': int(arr[2]),
    'Worth': 2
    }
  arr[3] = {
    'Quantity': int(arr[3]),
    'Worth': 2
  }
  arr[4] = {
    'Quantity': int(arr[4]),
    'Worth': 3
    }
  arr[5] = {
    'Quantity': int(arr[5]),
    'Worth': 5}
  arr[6] = {
    'Quantity': int(arr[6]),
    'Worth': 10}
  return gvesum(arr)

def gvesum(arr):
  total = 0
  for obj in arr:
    total += obj['Quantity'] * obj['Worth']
  return total

goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
