import telnetlib

from st2actions.runners.pythonrunner import Action
from st2common.exceptions.action import InvalidActionParameterException

"""
This action connects to the Redis Server on the port provided.
This script is a simple GET/SET implementation interface
The user command is translated into a redis command and issued
"""
class ConnectToRedis(Action):
    def run(self, redisServer, redisPort, var, value=None):
        if len(redisServer) == 0:
            raise InvalidActionParameterException("No Redis Server specified")
        if len(var) == 0:
            raise InvalidActionParameterException("No Variable specified")

        t = telnetlib.Telnet()
        t.open($redisServer, $redisPort)
        """
        GET var 
        SET var value        
        """        
        cmd = 'GET'
        if value is not None:
            cmd = 'SET'

        cmd += ' '
        cmd += var
        cmd += ' '

        if value is not None:
            cmd += value

        while True:
            answer = t.write(cmd)
            try:
                answer = t.read_all()
                break
            except EOFError:
                break
        return answer
