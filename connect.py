import psycopg2
import paramiko
from sshtunnel import SSHTunnelForwarder

mypkey = paramiko.RSAKey.from_private_key_file('pyapp')
pkey='pyapp'
key=paramiko.RSAKey.from_private_key_file(pkey)
tunnel =  SSHTunnelForwarder(
        ( '172.16.1.13', 22),
        ssh_username='userimec',
        ssh_password='Pin.1234',
        ssh_pkey=pkey,
        remote_bind_address=('localhost', 5432))

tunnel.start()
conn = psycopg2.connect(dbname='pyapp1', user='userimec' , password='Pin.1234', host='127.0.0.1', port=tunnel.local_bind_port)