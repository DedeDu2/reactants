def count_atoms_in_reaction(reaction):
    reactants, products = reaction.split('->')
    reactant_atoms = count_atoms(reactants.strip())
    product_atoms = count_atoms(products.strip())
    return {'Reactants': reactant_atoms, 'Products': product_atoms}

reaction = "H2 + O2 -> H2O"
print("Reaction:", reaction)
print("Count of atoms in reaction:", count_atoms_in_reaction(reaction))
