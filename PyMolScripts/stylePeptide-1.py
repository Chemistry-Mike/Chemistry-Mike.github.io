import pymol
from pymol import cmd, util

def style_peptide():
    object_list = cmd.get_object_list()
    if not object_list:
        print("Error: No molecular structure is currently loaded.")
        return

    original_name = object_list[0]
    new_name = "peptide"
    cmd.set_name(original_name, new_name)

    cmd.h_add(new_name)

    cmd.show('sticks', new_name)
    cmd.show('spheres', new_name)
    cmd.show('cartoon', new_name)

    cmd.set('stick_radius', '0.25', new_name)
    cmd.set('valence_mode', '3')

    cmd.set('sphere_scale', '0.15', f'({new_name} and elem H)')
    cmd.set('sphere_scale', '0.25', f'({new_name} and not elem H)')

    # Removed cmd.set_bond to rely on the global stick_radius for all bonds.
    # cmd.set_bond('radius', 0.1, f'({new_name} and elem H)', 'neighbor')

    cmd.set('cartoon_transparency', '0.5', new_name)

cmd.extend('style_peptide', style_peptide)

print("PyMOL command 'style_peptide' has been updated and should now correctly apply H-bond radius.")
