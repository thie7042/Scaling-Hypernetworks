# Scaling-Hypernetworks
This repository provides a sample design database that breaks down structures into base structural geometries. These simple meshes can be manipulated within the design space to create more complex structural systems using a series of translation vectors.
As supplementary material for the paper "Transformer Hypernetworks for Complex Structural Representation", this documentation provides further insight into the  mesh geometries used to train the proposed hypernetworks and the vectors used to train encoder models. To see view the target output designs that are constructed from this ground-truth dataset, run visualise_database.py within the example folder.


**Example Base Geometries**: The fundamental building block elements that structural designs can be broken down into.
![image](https://github.com/user-attachments/assets/70cfaf3a-84c1-41cb-b647-cc397c7c5566)

**Base Geometry manipulation**: Translating structural elements within the design space using vector transformations.

![image](https://github.com/user-attachments/assets/fa883b0e-e312-446e-8d4c-f6c29a33caf4)

The sample data provided within this repository has been curated within a low memory footprint, as supplementary material to further communicate the novel concepts introduced within the paper "Transformer Hypernetworks for Complex Structural Representation". As a result, the example sample provided within this repository focuses on the steel frame task from the aforementioned paper. 


## Requirements

Please ensure that your version of python is ≥ 3.9.
To install the required dependencies, run:

```bash
pip install -r requirements.txt

```

