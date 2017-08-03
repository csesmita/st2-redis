import telnetlib

from st2actions.runners.pythonrunner import Action
from st2common.exceptions.action import InvalidActionParameterException

"""
This action connects to the Redis Server on the port provided.
This script is a simple GET/SET implementation interface
The user command is translated into a redis command and issued
"""
class ConnectToRedis(Action):
    def __init__(self, config):
        super(ConnectToRedis, self).__init__(config=config)
        self.redisServer = self.config['redisServer']
        self.redisPort= self.config['redisPort']

    def run(self, var, value=None):
        if len(self.redisServer) == 0:
            raise InvalidActionParameterException("No Redis Server specified")
        if len(var) == 0:
            raise InvalidActionParameterException("No Variable specified")

        t = telnetlib.Telnet(self.redisServer, self.redisPort, timeout = 5)
        """
        GET var 
        SET var value        
        """        
        cmdTxt = 'GET'
        if value is not None:
            cmdTxt = 'SET'

        cmdTxt += ' '
        cmdTxt += var
        cmdTxt += ' '

        if value is not None:
            cmdTxt += value
        
        cmdTxt += '\n'

        answer = ''
        while True:
            t.write(cmdTxt.encode('ascii'))
            try:
                answer = t.read_very_eager()
                print answer
                break
            except EOFError:
                break
        t.close()
        return answer
