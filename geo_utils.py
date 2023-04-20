##
# Simple substitution, no arithmetic
# Need to leave the initial 'N' and 'W' alone!
def simple_sub(n_coords: str, w_coords: str, key_val_pairs: list):
  for key in key_val_pairs.keys():
    n_coords = n_coords.replace(key, key_val_pairs[key])
    w_coords = w_coords.replace(key, key_val_pairs[key])

  return (n_coords, w_coords)