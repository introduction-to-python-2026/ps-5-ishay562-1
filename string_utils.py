def split_before_uppercases(formula):
    formula_split = []
    start = 0 
    for i in range(1, len(formula)):
      if formula[i].isupper():
        formula_split.append(formula[start:i])
        start = i
    formula_split.append(formula[start:])
    return formula_split


def split_at_digit(formula):
    formula_split = []
    start = 0
    for i in range(1, len(formula)):
      if formula[i].isdigit():
        formula_split.append(formula[start:i])
        start = i
    formula_split.append(formula[start:])
    return formula_split
    
def count_atoms_in_molecule(molecular_formula):
  dict_1 = {}
  split_formula = split_before_uppercases(molecular_formula)
  for i in split_formula:
    split_at_digit_formula = split_at_digit(i)
    if len(split_at_digit_formula) == 1:
      dict_1[i] = 1
      break
    dict_1[split_at_digit_formula[0]] = int(split_at_digit_formula[1])
  return dict_1

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
