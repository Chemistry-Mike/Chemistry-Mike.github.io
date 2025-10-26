import pymol
from pymol import cmd, cgo

def proline_pentagons(selection="all", cgo_name="proline_rings_cgo", color=(1.0, 1.0, 0.0), tube_radius=0.2, filled=True):
    # --- Global PyMOL Settings for Aesthetics ---
    # Two-sided lighting is set to 0, which is why we only need to draw the polygon once now.
    cmd.set("two_sided_lighting", 0)
    
    cmd.set("ray_trace_mode", 3)
    cmd.set("ray_trace_color", "black")
    
    # Set the general stick radius
    cmd.set("stick_radius", 0.15, selection)
    
    # 1. Hide the Cartoon representation for the initial selection
    cmd.hide("cartoon", selection)
    
    # --- Pre-processing: Add Hydrogens, Show Spheres/Sticks, and Adjust their Size ---
    
    # 2. Correct function to add hydrogens
    cmd.h_add(selection)
    
    # 3. Show sticks for the entire selection after adding hydrogens
    cmd.show("sticks", selection)
    
    # 4. Show spheres for all atoms in the selection
    cmd.show("spheres", selection)
    
    # 5. Set the sphere scale for all hydrogen atoms to 0.2
    cmd.set("sphere_scale", 0.2, "hydrogens")
    
    # 6. Set the sphere scale for all non-hydrogen atoms to 0.3
    cmd.set("sphere_scale", 0.3, "not hydrogens")
    
    # Colors
    yellow = (1.0, 1.0, 0.0)    # Yellow for the filled CGO pentagon
    purple = (0.5, 0.0, 0.5)    # Purple for tubes and surfaces
    tube_color = purple
    tube_name = "proline_tubes_cgo"
    
    # New PyMOL object name for ring atoms
    ring_selection_name = "prings"
    
    # --- Action 1: Color all Proline residues purple ---
    cmd.set_color("proline_purple", purple)
    cmd.color("proline_purple", f"({selection}) and resn PRO")

    prolines = cmd.get_model(f"({selection}) and resn PRO", 1)

    if not prolines.atom:
        return

    unique_prolines = set()
    for atom in prolines.atom:
        identifier = (atom.segi, atom.chain, atom.resi)
        unique_prolines.add(identifier)

    if not unique_prolines:
        return

    full_cgo = []
    tube_cgo = []
    ring_selection_strings = [] 
    
    if not filled:
        full_cgo.extend([cgo.LINEWIDTH, tube_radius * 10, cgo.COLOR, color[0], color[1], color[2]])

    ring_atoms = ['N', 'CA', 'CB', 'CG', 'CD']

    for segi, chain, resi in unique_prolines:
        base_sel = f"(segi '{segi}' and chain '{chain}' and resi {resi} and resn PRO)"

        coords = {}
        missing_atom = False
        atom_names = []

        for name in ring_atoms:
            sel_str = f"{base_sel} and name {name}"
            try:
                xyz = cmd.get_atom_coords(sel_str, state=1)
                if xyz is None:
                    missing_atom = True
                    break
                coords[name] = xyz
                atom_names.append(name)
            except:
                missing_atom = True
                break

        if missing_atom:
            continue

        num_atoms = len(atom_names)
        if num_atoms != 5:
            continue
            
        ring_selection_strings.append(f"{base_sel} and name N+CA+CB+CG+CD") 

        # --- 1. Build the Single-Sided Filled Pentagon CGO (Yellow) ---
        if filled:
            # Uses the yellow color
            full_cgo.extend([cgo.COLOR, yellow[0], yellow[1], yellow[2]])

            P0 = coords[atom_names[0]]
            P1 = coords[atom_names[1]]
            P2 = coords[atom_names[2]]
            P3 = coords[atom_names[3]]
            P4 = coords[atom_names[4]]

            # A. Draw the single side (CCW order) - Flipped side is no longer needed
            full_cgo.extend([
                cgo.BEGIN, cgo.TRIANGLE_FAN,
                cgo.VERTEX, P0[0], P0[1], P0[2],
                cgo.VERTEX, P1[0], P1[1], P1[2],
                cgo.VERTEX, P2[0], P2[1], P2[2],
                cgo.VERTEX, P3[0], P3[1], P3[2],
                cgo.VERTEX, P4[0], P4[1], P4[2],
                cgo.END
            ])
            # Removed the second cgo.TRIANGLE_FAN block here
        else:
            # --- 1b. If not filled, the main CGO is an outline ---
            full_cgo.extend([cgo.BEGIN, cgo.LINES])
            for i in range(num_atoms):
                start_name = atom_names[i]
                end_name = atom_names[(i + 1) % num_atoms]
                start_coord = coords[start_name]
                end_coord = coords[end_name]
                full_cgo.extend([
                    cgo.VERTEX, start_coord[0], start_coord[1], start_coord[2],
                    cgo.VERTEX, end_coord[0], end_coord[1], end_coord[2],
                ])
            full_cgo.extend([cgo.END])


        # --- 2. Build the Tube CGO (Purple Border) ---
        for i in range(num_atoms):
            start_name = atom_names[i]
            end_name = atom_names[(i + 1) % num_atoms]
            start_coord = coords[start_name]
            end_coord = coords[end_name]
            
            tube_cgo.extend([
                cgo.CYLINDER, 
                start_coord[0], start_coord[1], start_coord[2],
                end_coord[0], end_coord[1], end_coord[2],
                tube_radius,
                tube_color[0], tube_color[1], tube_color[2], # Purple
                tube_color[0], tube_color[1], tube_color[2]  # Purple
            ])


    # --- Load the CGOs into PyMOL ---
    if full_cgo:
        cmd.delete(cgo_name)
        cmd.load_cgo(full_cgo, cgo_name)
        cmd.enable(cgo_name)

    if tube_cgo:
        cmd.delete(tube_name)
        cmd.load_cgo(tube_cgo, tube_name)
        cmd.enable(tube_name)
        
    # --- Create and Configure the 'prings' atom object (Purple Surface) ---
    if ring_selection_strings:
        combined_selection = " or ".join(ring_selection_strings)
        
        cmd.delete(ring_selection_name) 
        cmd.create(ring_selection_name, combined_selection)
        
        # Configure 'prings' object visibility and color
        cmd.hide("spheres", ring_selection_name)
        cmd.hide("sticks", ring_selection_name)
        cmd.hide("cartoon", ring_selection_name) 
        
        cmd.show("surface", ring_selection_name)
        
        # Set color for the prings surface specifically (Purple)
        cmd.set_color("prings_color", purple)
        cmd.color("prings_color", ring_selection_name)
        
        # Set transparency to 0.5
        cmd.set("transparency", 0.5, ring_selection_name)

cmd.extend("proline_pentagons", proline_pentagons)
