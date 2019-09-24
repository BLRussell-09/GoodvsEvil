def goodVsEvil(good, evil):
  good = good.split(' ')
  print(good[1])

def goodWorth(arr):
  arr[0] = {
    'Quantity': int(arr[0]),
    'Hobbit': 1
    }
  arr[1] = {
    'Quantity': arr[1],
    'Men': 2
    }
  arr[2] = {
    'Quatity': int(arr[2]),
    'Elves': 3
    }
  arr[4] = {
    'Quantity': int(arr[3]),
    'Dwarves': 3
  }
  arr[4] = {
    'Quatity': int(arr[4]),
    'Eagles': 4
    }
  arr[4] = {'Wizards': 10}


goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')
