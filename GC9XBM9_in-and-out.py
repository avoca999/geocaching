import string
import sys

import geo_utils as g

def initialise():
  global n_folds
  n_folds = 0

def finalise():
  pass

# From https://stackoverflow.com/questions/72348363/how-to-intersperse-characters-from-two-different-strings-alternatively-to-form-a
def interleave(str1, str2):
    min_len = min(len(str1), len(str2))
    return "".join([str1[i] + str2[i] for i in range(min_len)]) + str1[min_len:] + str2[min_len:]

def do_fold():
  global n_folds
  global s_creases

  '''
  s_creases shows the creases in the strip of paper, in the form 1 for an in-crease, and 0 for an out-crease.
  Experiment shows that there's always an odd number of creases.
  If the current number is n (always odd), making a fold adds n+1 creases, in pairs of (1,0), 
  interleaved with the existing creases
  i.e.
     1
   1 1 0
  1101100, etc.
  '''

  if n_folds == 0:
    # First time, get one in-crease
    s_creases = '1'
  else:
    n_creases_to_add = len(s_creases) + 1
    s_creases_to_add = '10' * int(n_creases_to_add/2)
    s_creases = interleave(s_creases_to_add, s_creases)

  n_folds += 1
  finished = (len(s_creases) > 50)

  print('%d folds, %d creases: %s.' % (n_folds, len(s_creases), s_creases))

  return finished

def main():
  global s_creases

  try:
    initialise()

    finished = False
    while not finished:
      finished = do_fold()

    # Now have a binary string
    n_int = int(s_creases,2)
    print('int is %d' % n_int)

    s_int = str(n_int)
    keys = string.ascii_uppercase
    key_val_pairs = {}
    for i in range (0, len(s_int)):
      key = keys[i]
      val = s_int[i]
      key_val_pairs[key] = val

    print('key_val_pairs is %s' % key_val_pairs)

    n_coords, w_coords = g.simple_sub('51 44.RHN', '00 22.OMJ', key_val_pairs)

    print('Co-ords are N %s W %s' % (n_coords, w_coords))

  except:
    print('ERROR: ;', sys.exc_info())
    finalise()
    # Pause
    #u.output('Press return to exit.')
    #raw_input()

  print('Execution finished successfully')

if __name__ == "__main__":
    main()
