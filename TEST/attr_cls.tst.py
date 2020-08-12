o = Orb()
o.open
o.open.conn
o.open.auth
o.open.auth.challenge
o.open.auth.answer
o.open.auth.succ
o.open.auth.fail
o.keepalive
o.keepalive.ping
o.keepalive.pong
o.signal
o.signal.room
o.signal.room.join
o.signal.room.leave
o.signal.channel
o.signal.channel.join
o.signal.channel.leave
o.data
o.close 


o = Orb()
o.open.conn = 'A'
o.open.auth.challenge = 'B'
o.open.auth.answer = 'C'
o.open.auth.succ  = 'D'
o.open.auth.fail = 'E'
o.keepalive.ping = 'F'
o.keepalive.pong = 'G'
o.signal.room.join = 'H'
o.signal.room.leave = 'I'
o.signal.channel.join = 'J'
o.signal.channel.leave = 'K'
o.data = 'L'
o.close = 'M'

deleted = o.signal.room
del o.signal.room


o = Orb()
o.open.conn = 'A'
o.open.auth.challenge = 'B'
o.open.auth.answer = 'C'
o.open.auth.succ  = 'D'
o.open.auth.fail = 'E'
o.keepalive.ping = 'F'
o.keepalive.pong = 'G'
o.signal.room.join = 'H'
o.signal.room.leave = 'I'
o.signal.channel.join = 'J'
o.signal.channel.leave = 'K'
o.data = 'L'
o.close = 'M'
