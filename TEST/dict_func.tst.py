d = {
    'open':{
        'conn':'open.conn',
        'auth': {
            'challenge':'open.auth.challenge',
            'answer':'open.auth.answer',
            'succ':'open.auth.succ',
            'fail':'open.auth.fail'
        }
    },
    'keepalive':{
        'ping':"keepalive.ping",
        'pong':"keepalive.pong",
    },
    'signal':{
        'room':{
            'join':'signal.room.join',
            'leave':'signal.room.leave',
        },
        'channel':{
            'join':'signal.channel.join',
            'leave':'signal.channel.leave',
        },
    },
    'data':'data',
    'close':'close'
}


from xdict.jprint import pobj
>>> pobj(get_via_pl(d,['open']))
{
 'conn': 'open.conn',
 'auth':
         {
          'challenge': 'open.auth.challenge',
          'answer': 'open.auth.answer',
          'succ': 'open.auth.succ',
          'fail': 'open.auth.fail'
         }
}

>>> pobj(get_via_pl(d,['open','auth']))
{
 'challenge': 'open.auth.challenge',
 'answer': 'open.auth.answer',
 'succ': 'open.auth.succ',
 'fail': 'open.auth.fail'
}


>>> get_via_pl(d,['open','auth','challenge'])
'open.auth.challenge'
>>>


dd = {}
set_dflt_via_pl(dd,['open','conn'])
set_dflt_via_pl(dd,['open','auth','challenge'])
set_dflt_via_pl(dd,['open','auth','answer'])
set_dflt_via_pl(dd,['open','auth','succ'])
set_dflt_via_pl(dd,['open','auth','fail'])
set_dflt_via_pl(dd,['keepalive','ping'])
set_dflt_via_pl(dd,['keepalive','pong'])
set_dflt_via_pl(dd,['signal','room','join'])
set_dflt_via_pl(dd,['signal','room','leave'])
set_dflt_via_pl(dd,['signal','channel','join'])
set_dflt_via_pl(dd,['signal','channel','leave'])
set_dflt_via_pl(dd,['data'])
set_dflt_via_pl(dd,['close'])


set_via_pl(dd,['open','conn'],'open.conn')
set_via_pl(dd,['open','auth','challenge'],'open.auth.challenge')
set_via_pl(dd,['open','auth','answer'],'open.auth.answer')
set_via_pl(dd,['open','auth','succ'],'open.auth.succ')
set_via_pl(dd,['open','auth','fail'],'open.auth.fail')
set_via_pl(dd,['keepalive','ping'],'keepalive.ping')
set_via_pl(dd,['keepalive','pong'],'keepalive.pong')
set_via_pl(dd,['signal','room','join'],'signal.room.join')
set_via_pl(dd,['signal','room','leave'],'signal.room.leave')
set_via_pl(dd,['signal','channel','join'],'signal.channel.join')
set_via_pl(dd,['signal','channel','leave'],'signal.channel.leave')
set_via_pl(dd,['data'],'data')
set_via_pl(dd,['close'],'close')


assert(dd==d)


dd = {}
set_dflt_via_pl(dd,['open','conn'],'open.conn')
set_dflt_via_pl(dd,['open','auth','challenge'],'open.auth.challenge')
set_dflt_via_pl(dd,['open','auth','answer'],'open.auth.answer')
set_dflt_via_pl(dd,['open','auth','succ'],'open.auth.succ')
set_dflt_via_pl(dd,['open','auth','fail'],'open.auth.fail')
set_dflt_via_pl(dd,['keepalive','ping'],'keepalive.ping')
set_dflt_via_pl(dd,['keepalive','pong'],'keepalive.pong')
set_dflt_via_pl(dd,['signal','room','join'],'signal.room.join')
set_dflt_via_pl(dd,['signal','room','leave'],'signal.room.leave')
set_dflt_via_pl(dd,['signal','channel','join'],'signal.channel.join')
set_dflt_via_pl(dd,['signal','channel','leave'],'signal.channel.leave')
set_dflt_via_pl(dd,['data'],'data')
set_dflt_via_pl(dd,['close'],'close')


assert(dd==d)


del_via_pl(d,['data'])
del_via_pl(d,['open','auth'])
{'challenge': 'open.auth.challenge', 'answer': 'open.auth.answer', 'succ': 'open.auth.succ', 'fail': 'open.auth.fail'}
>>> pobj(d)
{
 'open':
         {
          'conn': 'open.conn'
         },
 'keepalive':
              {
               'ping': 'keepalive.ping',
               'pong': 'keepalive.pong'
              },
 'signal':
           {
            'room':
                    {
                     'join': 'signal.room.join',
                     'leave': 'signal.room.leave'
                    },
            'channel':
                       {
                        'join': 'signal.channel.join',
                        'leave': 'signal.channel.leave'
                       }
           },
 'close': 'close'
}



