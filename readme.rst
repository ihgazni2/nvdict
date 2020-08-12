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





~~~~~

        

License
=======

- MIT
