import numpy as np
import pyvista as pv
import os 
import re
import numpy as np
import random

# Create a plotter
plotter = pv.Plotter()
current_mesh_index = 0

relative_path = os.path.abspath(__file__)
relative_path = relative_path.split('Scaling-Hypernetworks')[0]

# Get example structures
design_folder = relative_path +  r'\Scaling-Hypernetworks\example\data\example_meshes\\'
vector_folder = relative_path +  r'\Scaling-Hypernetworks\example\data\example_vectors\\'
structures = [name for name in os.listdir(design_folder) if os.path.isdir(os.path.join(design_folder, name))]

random.shuffle(structures)

def show_next_mesh():
    global current_mesh_index

    plotter.clear()

    # If we haven't shown all meshes, add the next mesh
    if current_mesh_index < len(structures):

        structure = structures[current_mesh_index]

        # Load structural base geometries
        base_geometries = os.listdir(design_folder + structure)
        
        # Loop through base geometries
        for geo in base_geometries:

            # Load mesh
            mesh = pv.read(design_folder + structure + '\\' + geo)

            # If working with bracing, use mirrored property
            if 'Bracing' in geo:

                mirrored = mesh.copy()
                mirrored.points[:, 2] *= -1 

                center1 = mesh.center
                center2 = mirrored.center

                # Compute translation vector 
                translation = [center1[0] - center2[0], center1[1] - center2[1],center1[2] - center2[2]]

                # Apply translation
                mirrored.translate(translation, inplace=True)
                mesh = mesh + mirrored
            
            # Apply corresponding translation vectors
            with open(vector_folder + structure + '\\' + geo.replace('.stl','.txt') ) as file:
                vectors =  file.read()
                vectors = re.findall(r'\{([^}]+)\}', vectors)
                vectors = [list(map(float, vec.split(','))) for vec in vectors]

                v = np.array(vectors)
                axis =  np.min(v[:,0])

                for vector in vectors:

                    # Roofbeam mirrored 
                    if 'Roofbeam' in geo and vector[0] == axis :

                        mirrored = mesh.copy()
                        mirrored.points[:, 2] *= -1 

                        center1 = mesh.center
                        center2 = mirrored.center

                        translation = [center1[0] - center2[0], center1[1] - center2[1],center1[2] - center2[2]]

                        # Apply translation
                        mirrored.translate(translation, inplace=True)
                        mirrored.translate(vector, inplace=True)  
                        plotter.add_mesh(mirrored, show_edges=True)

                    else:
                        translated_mesh = mesh.copy() 
                        translated_mesh.translate(vector, inplace=True)  
                        plotter.add_mesh(translated_mesh, show_edges=True)

            # Display center beam
            if 'Eavestrut' in geo:
                center_beam = mesh.copy()

                center_beam.translate(np.array(vectors[0]) - np.array([float(geo.split('_')[1])/2,0,-2]), inplace=True)  
                plotter.add_mesh(center_beam, show_edges=True)

        title = f"Steel Frame, width = {geo.split('_')[2].replace('.stl','')}m, span = {geo.split('_')[1]}m"
        plotter.add_text(title, font_size=16, color='black')
        plotter.add_text("Press 'n' to view the next structure", position='upper_right',font_size=12, color='black')

        plotter.render() 
        
        plotter.reset_camera() 
        current_mesh_index += 1 
    else:
        plotter.close()  

plotter.add_key_event("n", show_next_mesh)

show_next_mesh()

plotter.show()
