from pymol import cmd

def color_charged():    
    cmd.h_add("all")
    cmd.color("white", "all")
    acidic_selection = "resn ASP+GLU"
    basic_selection = "resn ARG+LYS+HIS"
    
    # Specific negatively and positively charged atoms
    neg_atoms_acidic = f"({acidic_selection}) and (name OD1+OD2+OE1+OE2)"
    pos_atoms_basic = f"({basic_selection}) and (name NZ+NH1+NH2)"

    # 3. Coloring Charged Residues (Side Chain Atoms)
    
    # Color all atoms in acidic side chains salmon (covers entire side chain)
    cmd.color("salmon", f"({acidic_selection}) and sidechain")

    # Color all atoms in basic side chains palegreen (covers entire side chain)
    cmd.color("palegreen", f"({basic_selection}) and sidechain")
    
    # 4. Coloring Specific Charged Atoms (Override)

    # Color the specific negatively charged atoms red (Overrides salmon)
    cmd.color("red", neg_atoms_acidic)

    # Color the specific positively charged atoms green (Overrides palegreen)
    cmd.color("green", pos_atoms_basic)
    
    # 5. Display Settings
    
    # Show spheres and sticks
    cmd.show("spheres", "all")
    cmd.show("sticks", "all")
    
    # Set display sizes
    cmd.set("stick_radius", 0.1) 
    cmd.set("sphere_scale", 0.2, "all")
    cmd.set("sphere_scale", 0.1, "elem H") # 0.1 for hydrogens

    # Hide cartoon
    cmd.hide("cartoon", "all")

    # Show surface and set transparency to 0.5
    cmd.show("surface", "all")
    cmd.set("transparency", 0.5)

    # 6. Ray Tracing Settings
    cmd.set("ray_trace_mode", 3)
    cmd.set("ray_trace_color", "black")

# Register the function so it can be called directly as a PyMOL command
cmd.extend("color_charged", color_charged)
