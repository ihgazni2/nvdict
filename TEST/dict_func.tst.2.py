d = {
    'open':{
        'conn':'A',
        'auth': {
            'challenge':'B',
            'answer':'C',
            'succ':'D',
            'fail':'E'
        }
    },
    'keepalive':{
        'ping':"F",
        'pong':"G",
    },
    'signal':{
        'room':{
            'join':'H',
            'leave':'I',
        },
        'channel':{
            'join':'J',
            'leave':'K',
        },
    },
    'data':'L',
    'close':'M'
}



m = _get_mat(d)
ele_sdfs = _get_ele_sdfs(m[0][0])

plmat = get_plmat(d) 
plsdfs = get_sdfs_pl(d)
leaf_plsdfs = get_sdfs_leaf_pl(d)
nonleaf_plsdfs = get_sdfs_nonleaf_pl(d)
plwfs = get_wfs_pl(d)


sdfs_vlist =  get_sdfs_vlist(d)
wfs_vlist  =  get_wfs_vlist(d)


kstruct = get_kstruct(d)
flat_vl = get_flatvl_via_kstruct(d,kstruct)


from xlist.nest import ListTree
vstruct = get_vstruct(d)
ListTree(vstruct)


leaf_entries = flatten_to_leaf_entries(d)
parr(leaf_entries)

leaf_dict = flatten_to_leaf_dict(d)
pdict(leaf_dict)

sdfs_leaf_vlist = get_sdfs_leaf_vlist(d)



kstruct,flat_vl = unzip(d)

zip(kstruct,flat_vl)


