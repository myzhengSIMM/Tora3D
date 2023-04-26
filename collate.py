import torch
from generate_feat import generate_feat
from utils import Data_enhancement
import random

# collate
def collate(data_list, max_num_atom, wl_max_iter, data_enhancement=True):
    """
<<<<<<< HEAD

    """

=======
    # max_num_atom： 决定要将AM_bond_feat  pad到多少的平方  这个数字不是由batch_size内部决定的而是由全部数据来决定的，本项目中使用9
    # wl_max_iter：wl算法迭代次数  默认选3

    """
    
    # 先弄只有最低能的构象把
>>>>>>> ead8aac572b4bfbf5e25b5638f0da5f049708d5f
    smiles_list = [data.name for data in data_list]
    labels_list = [data.dihedral_degree[0].cpu().numpy().tolist() for data in data_list]
    relativeenergy_list = [data.relativeenergy_list[0]        for i,data in enumerate(data_list)]
    masks_list =  [data.dihedral_pairs_atoms4.t() for data in data_list]
    
    atom_feat, AM_bond_feat, node_color_list, d_list, num_atom_list = zip(*[generate_feat(smile, max_num_atom, wl_max_iter) for smile in smiles_list])
<<<<<<< HEAD

=======
    # atom_feat:   元组，元组中一共由batch_size个元素，每个元素都是[max_num_atom,39]的tensor
    # AM_bond_feat：元组，元组中一共由batch_size个元素，每个元素都是[max_num_atom，max_num_atom，10]的tensor
    # node_color_list：元组，元组中一共由batch_size个元素，每个元素都是长度为 max_num_atom 的list
    # d_list: 元组，元组中一共由batch_size个元素，每个元素都是长度为 max_num_atom 的list
    # num_atom_list: 元组，元组中一共有batch_size个元素，每个元素代表小分子长度
>>>>>>> ead8aac572b4bfbf5e25b5638f0da5f049708d5f
    
    atom_feat = torch.stack(atom_feat)
    AM_bond_feat = torch.stack(AM_bond_feat)
    node_color_feat = torch.tensor(node_color_list)
    d = torch.tensor(d_list)
    relativeenergys = torch.tensor(relativeenergy_list)
    return atom_feat, AM_bond_feat, node_color_feat, d, labels_list, masks_list, num_atom_list,relativeenergys

# collate_new
def collate_new(data_list, max_num_atom, wl_max_iter, data_enhancement=True):
    """
<<<<<<< HEAD
=======
    # max_num_atom： 决定要将AM_bond_feat  pad到多少的平方  这个数字不是由batch_size内部决定的而是由全部数据来决定的，本项目中使用9
    # wl_max_iter：wl算法迭代次数  默认选3
>>>>>>> ead8aac572b4bfbf5e25b5638f0da5f049708d5f

    """
    
    
    conformer_index = [random.randint(0,data.dihedral_degree.shape[0]-1) for data in data_list]
    
    smiles_list = [data.name for data in data_list]
    labels_list = [data.dihedral_degree[conformer_index[i]].cpu().numpy().tolist() for i,data in enumerate(data_list)]
    relativeenergy_list = [data.relativeenergy_list[conformer_index[i]]        for i,data in enumerate(data_list)]   # dtype : float
    masks_list =  [data.dihedral_pairs_atoms4.t() for data in data_list]
    
    atom_feat, AM_bond_feat, node_color_list, d_list, num_atom_list = zip(*[generate_feat(smile, max_num_atom, wl_max_iter) for smile in smiles_list])
<<<<<<< HEAD

=======
    # atom_feat:   元组，元组中一共由batch_size个元素，每个元素都是[max_num_atom,39]的tensor
    # AM_bond_feat：元组，元组中一共由batch_size个元素，每个元素都是[max_num_atom，max_num_atom，10]的tensor
    # node_color_list：元组，元组中一共由batch_size个元素，每个元素都是长度为 max_num_atom 的list
    # d_list: 元组，元组中一共由batch_size个元素，每个元素都是长度为 max_num_atom 的list
    # num_atom_list: 元组，元组中一共有batch_size个元素，每个元素代表小分子长度
    
>>>>>>> ead8aac572b4bfbf5e25b5638f0da5f049708d5f
    atom_feat = torch.stack(atom_feat)
    AM_bond_feat = torch.stack(AM_bond_feat)
    node_color_feat = torch.tensor(node_color_list)
    d = torch.tensor(d_list)
    relativeenergys = torch.tensor(relativeenergy_list)
    return atom_feat, AM_bond_feat, node_color_feat, d, labels_list, masks_list, num_atom_list, relativeenergys


# collate_new_user
def collate_new_user(data_list, max_num_atom, wl_max_iter, data_enhancement=True):
    """
<<<<<<< HEAD
=======
    # max_num_atom： 决定要将AM_bond_feat  pad到多少的平方  这个数字不是由batch_size内部决定的而是由全部数据来决定的，本项目中使用9
    # wl_max_iter：wl算法迭代次数  默认选3
>>>>>>> ead8aac572b4bfbf5e25b5638f0da5f049708d5f

    """
    
#     conformer_index = [random.randint(0,data.dihedral_degree.shape[0]-1) for data in data_list]
    data_list = [data for data in data_list if data is not None]
    
    smiles_list = [data.name for data in data_list]
    labels_list = [data.dihedral_degree.cpu().numpy().tolist() for i,data in enumerate(data_list)]
    relativeenergy_list = [data.relativeenergy for data in data_list]  # dtype : float
    masks_list =  [data.dihedral_pairs_atoms4.t() for data in data_list]
  
    atom_feat, AM_bond_feat, node_color_list, d_list, num_atom_list = zip(*[generate_feat(smile, max_num_atom, wl_max_iter) for smile in smiles_list])
<<<<<<< HEAD

=======
    # atom_feat:   元组，元组中一共由batch_size个元素，每个元素都是[max_num_atom,39]的tensor
    # AM_bond_feat：元组，元组中一共由batch_size个元素，每个元素都是[max_num_atom，max_num_atom，10]的tensor
    # node_color_list：元组，元组中一共由batch_size个元素，每个元素都是长度为 max_num_atom 的list
    # d_list: 元组，元组中一共由batch_size个元素，每个元素都是长度为 max_num_atom 的list
    # num_atom_list: 元组，元组中一共有batch_size个元素，每个元素代表小分子长度
>>>>>>> ead8aac572b4bfbf5e25b5638f0da5f049708d5f
    
    atom_feat = torch.stack(atom_feat)
    AM_bond_feat = torch.stack(AM_bond_feat)
    node_color_feat = torch.tensor(node_color_list)
    d = torch.tensor(d_list)
    relativeenergys = torch.tensor(relativeenergy_list)
    return atom_feat, AM_bond_feat, node_color_feat, d, labels_list, masks_list, num_atom_list, relativeenergys,smiles_list