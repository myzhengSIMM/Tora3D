![image](https://github.com/myzhengSIMM/Tora3D/assets/150652802/a90b9e10-cd11-4e69-b9ea-d14e73aa2be7)# Tora3D
Code for "Tora3D: An Autoregressive Torsion Angle Prediction Model for Molecular 3D Conformation Generation". Please read our paper [https://doi.org/10.1186/s13321-023-00754-4](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-023-00726-8) for more detials.

# Abstract of article
Three-dimensional (3D) conformations of a small molecule profoundly affect its binding to the target of interest, the resulting biological effects, and its disposition in living organisms, but it is challenging to accurately characterize the conformational ensemble experimentally. Here, we proposed an autoregressive torsion angle prediction model Tora3D for molecular 3D conformer generation. Rather than directly predicting the conformations in an end-to-end way, Tora3D predicts a set of torsion angles of rotatable bonds by an interpretable autoregressive method and reconstructs the 3D conformations from them, which keeps structural validity during reconstruction. Another advancement of our method over other conformational generation methods is the ability to use energy to guide the conformation generation. In addition, we propose a new message-passing mechanism that applies the Transformer to the graph to solve the difficulty of remote message passing. Tora3D shows superior performance to prior computational models in the trade-off between accuracy and efficiency, and ensures conformational validity, accuracy, and diversity in an interpretable way.![image](https://github.com/myzhengSIMM/Tora3D/assets/150652802/250fa9c4-e6d4-4e5d-8ff0-fa3c50ccc15d)

![1e84967c59dbc7434351549fbaa2c9d](https://github.com/myzhengSIMM/Tora3D/assets/150652802/7d959913-4d59-4099-82ec-2c0ac6ef61d7)

## Download 
After you clone this Repositories in your machine, you should download some files/folders(because the limit of github for big file)
  
1, "data_1/rdkit_folder"   

  Download rdkit_folder.tar.gz file from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/JNGTDF, put it in data_1 floder, then unzip it use tar commond. The file structure after unzip is as follows:
  
     Tora3D
     -data_1
     --rdkit_folder
     ---druds
     ---qm9
2,
  "model_save"      
  
  "prepare_ori_con"       (If you encounter an error message indicating that the file is corrupted)
  
  "data1/drugs"
  
  These three files are obtained from Kuaipan:
        https://pan.quark.cn/s/c32e62fe57b0
        Extraction code: nKrC
  
## setup
You should install pyg in your conda enveriment to run this Repositories.

## preprocess
Preprocess the GEOM dataset in the preprocess.ipynb file, where the data_path is the path to the GEOM dataset.（data source：https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/JNGTDF The data file we downloaded is rdkit_folder.tar.gz.）The files generated after preprocessing are placed in ./data_1/drugs/.

## usage
You should run the main_drugs-Copy3_ot-1088.ipynb to get trained model or use our pretraind model to get result.

The small molecule conformations predicted by the model are saved in ./confs_save, where each molecule is a separate folder. The p_*.sdf files are the conformer sets predicted by our model, and the t_*.sdf files are the true conformer sets.

## visualization
You can check the predicted conformations in the show3Dstructure.ipynb file.
