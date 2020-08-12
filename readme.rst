.. contents:: Table of Contents
   :depth: 5


*nvdict*
------------

- nest dict tools

Installation
============

    ::
    
        $ pip3 install nvdict

Usage
=====

Orb
~~~

creat default
#############
    
    ::
        
        from nvdict.dcls import Orb
        o = Orb()
        >>> o = Orb()
        >>> o.open.conn = 'A'
        >>> o.auth.challenge = 'B'
        >>> o.auth.answer = 'C'
        >>> o.auth.succ = 'D'
        >>> o.auth.fail = 'E'
        >>>
        >>> o
        {'open': {'conn': 'A'}, 'auth': {'challenge': 'B', 'answer': 'C', 'succ': 'D', 'fail': 'E'}}
        >>>
        >>> o._dumps()
        {'open': {'conn': 'A'}, 'auth': {'challenge': 'B', 'answer': 'C', 'succ': 'D', 'fail': 'E'}}
        >>> type(o._dumps())
        <class 'dict'>
        >>> type(o)
        <class 'nvdict.dcls.Orb'>
        
        >>> o.auth.succ._dir_path()
        'auth/succ'
        >>>
        >>> o.auth.succ._dot_path()
        'auth.succ'
        >>>
        

loads from dict
###############

    ::
        
         from nvdict.dcls import Orb
         d = {
             'open': {'conn': 'A', 'auth': {'challenge': 'B', 'answer': 'C', 'succ': 'D', 'fail': 'E'}}, 
             'keepalive': {'ping': 'F', 'pong': 'G'}, 
             'signal': {'room': {'join': 'H', 'leave': 'I'}, 
             'channel': {'join': 'J', 'leave': 'K'}}, 
             'data': 'L', 
             'close': 'M'
         }
         o = Orb()
         o._loads(d)
         >>> o.
         o.close      o.data       o.keepalive  o.open       o.signal
         >>> o.keepalive
         {'ping': 'F', 'pong': 'G'}
         >>>
         >>> o.keepalive._children_dict()
         ['F', 'G']
         >>>
         >>> o.keepalive.ping
         'F'
         >>> o.keepalive.ping._parent_dict()
         {'ping': 'F', 'pong': 'G'}
         >>>
         


Function
~~~~~~~~
    
    ::
        
        import nvdict.dict_func as dfunc
        d = {
             'open': {'conn': 'A', 'auth': {'challenge': 'B', 'answer': 'C', 'succ': 'D', 'fail': 'E'}},
             'keepalive': {'ping': 'F', 'pong': 'G'},
             'signal': {'room': {'join': 'H', 'leave': 'I'},
             'channel': {'join': 'J', 'leave': 'K'}},
             'data': 'L',
             'close': 'M'
        }
        
        kstruct,vl = dfunc.unzip(d)
        >>> kstruct
         {'open': {'conn': {}, 'auth': {'challenge': {}, 'answer': {}, 'succ': {}, 'fail': {}}}, 'keepalive': {'ping': {}, 'pong': {}}, 'signal': {'room': {'join': {}, 'leave': {}}, 'channel': {'join': {}, 'leave': {}}}, 'data': {}, 'close': {}}
        >>>
        >>> vl
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
        >>>

        >>> dfunc.zip(kstruct,vl) == d
        True
        >>>


        >>> parr(dfunc.flatten_to_leaf_entries(d))
        [('open', 'conn'), 'A']
        [('open', 'auth', 'challenge'), 'B']
        [('open', 'auth', 'answer'), 'C']
        [('open', 'auth', 'succ'), 'D']
        [('open', 'auth', 'fail'), 'E']
        [('keepalive', 'ping'), 'F']
        [('keepalive', 'pong'), 'G']
        [('signal', 'room', 'join'), 'H']
        [('signal', 'room', 'leave'), 'I']
        [('signal', 'channel', 'join'), 'J']
        [('signal', 'channel', 'leave'), 'K']
        [('data',), 'L']
        [('close',), 'M']
        >>>


        >>> parr(dfunc.get_sdfs_pl(d))
        []
        ['open']
        ['open', 'conn']
        ['open', 'auth']
        ['open', 'auth', 'challenge']
        ['open', 'auth', 'answer']
        ['open', 'auth', 'succ']
        ['open', 'auth', 'fail']
        ['keepalive']
        ['keepalive', 'ping']
        ['keepalive', 'pong']
        ['signal']
        ['signal', 'room']
        ['signal', 'room', 'join']
        ['signal', 'room', 'leave']
        ['signal', 'channel']
        ['signal', 'channel', 'join']
        ['signal', 'channel', 'leave']
        ['data']
        ['close']
        >>>

        plsdfs = dfunc.get_sdfs_pl(d) 
        dfunc.plsdfs_to_kstruct(plsdfs)
        {'open': {'conn': {}, 'auth': {'challenge': {}, 'answer': {}, 'succ': {}, 'fail': {}}}, 'keepalive': {'ping': {}, 'pong': {}}, 'signal': {'room': {'join': {}, 'leave': {}}, 'channel': {'join': {}, 'leave': {}}}, 'data': {}, 'close': {}}



        >>> parr(dfunc.get_wfs_pl(d))
        []
        ['open']
        ['keepalive']
        ['signal']
        ['data']
        ['close']
        ['open', 'conn']
        ['open', 'auth']
        ['keepalive', 'ping']
        ['keepalive', 'pong']
        ['signal', 'room']
        ['signal', 'channel']
        ['open', 'auth', 'challenge']
        ['open', 'auth', 'answer']
        ['open', 'auth', 'succ']
        ['open', 'auth', 'fail']
        ['signal', 'room', 'join']
        ['signal', 'room', 'leave']
        ['signal', 'channel', 'join']
        ['signal', 'channel', 'leave']
        >>>

        
        vl = dfunc.get_sdfs_vlist(d)
        vl[0] = d
        vl[1] = d['open']        


APIS        
~~~~
- def get_via_pl(d,pl):
- def set_via_pl(d,pl,v):
- def set_dflt_via_pl(d,pl,*args):
- def del_via_pl(d,pl):
- def is_leaf_pl_via_dict(d,pl):
- def get_type_str(o):
- def get_kschema(d):
- def get_kstruct(d):
- def get_ppl(pl):
- def get_plmat(d):
- def get_wfs_pl(d):
- def get_sdfs_pl(d):
- def get_sdfs_leaf_pl(d):
- def get_sdfs_nonleaf_pl(d):
- def plsdfs_to_kstruct(sdfs):
- def is_leaf_pl_via_plsdfs(sdfs_pl,pl):
- def get_pl_children_via_plsdfs(plsdfs,pl):
- def get_vfstch(d):
- def get_vlstch(d):
- def get_which_vchild(d,which):
- def get_some_vchildren(d,*whiches):
- def get_vchildren(d):
- def get_vchild_count(d):
- def is_leafv(d):
- def get_wfs_vmat(d):
- def get_wfs_vlist(d):
- def get_sdfs_vlist(d):
- def get_sdfs_leaf_vlist(d):
- def get_vstruct(d):
- def get_count(d):
- def flatten_to_leaf_entries(d):
- def flatten_to_leaf_dict(d):
- def deflatten_from_leaf_entries(leaf_entries):
- def get_flatvl_via_kstruct(d,kstruct):
- def unzip(d):
- def zip(kstruct,flat_vl):
- def _get_mat(d):
- def _is_leaf_ele(ele):
- def _get_wfs_elist(d):
- def _get_eparent(ele):
- def _get_efstch(ele):
- def _get_ersib(ele):
- def _get_ersib_of_fst_ance_having_rsib(ele):
- def _get_ele_sdfs_next(ele):
- def _get_ele_sdfs(ele):


RESTRICT
~~~~~~~~
- only support nested dict, no array
- for full support ,refer to this: 
- https://github.com/ihgazni2/ndtreepy
- https://github.com/navegador5/nvtree
        

License
=======

- MIT
