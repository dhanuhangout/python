"""Chat Server."""
import SocketServer
import re
import socket


class ClientError(Exception):
    """Client Exception."""
    pass


class ChatServer(SocketServer.ThreadingTCPServer):
    """The server class."""

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.ThreadingTCPServer.__init__(self, server_address,
                                                 RequestHandlerClass)
        self.users = {}


class RequestHandler(SocketServer.StreamRequestHandler):
    """A class that handles all the client's requests."""
    NICKNAME = re.compile('^[A-Za-z0-9_-]+$') # Regex for a valid nickname

    def handle(self):
        self.nickname = None
        self.private_message('Who are you?')
        nickname = self._readline()
        done = False
        try:
            self.nick_command(nickname)
            self.private_message(
                'Hello %s, welcome to the Python Chat Server.' % nickname)
            self.broadcast('%s has joined the chat.' % nickname, False)
        except ClientError, error:
            self.private_message(error.args[0])
            done = True
        except socket.error:
            done = True
        # Now they are logged in; let them chat.
        while not done:
            try:
                done = self.process_input()
                print 'done = ', done
            except ClientError, error:
                self.private_message(str(error))
            except socket.error, error:
                done = True

    def finish(self):
        """Ends the connection."""
        if self.nickname:
            message = '%s has quit.' % self.nickname
            if hasattr(self, 'parting_words'):
                message = '%s has quit. %s' % (self.nickname,
                    self.parting_words)

            self.broadcast(message, False)

            if self.server.users.get(self.nickname):
                del(self.server.users[self.nickname])
        self.request.shutdown(2)
        self.request.close()

    def process_input(self):
        """Process clinet input."""
        done = False
        input_line = self._readline()
        command, arg = self._parse_command(input_line)
        if command:
            done = command(arg)
        else:
            input_line = '<%s> %s\n' % (self.nickname, input_line)
            self.broadcast(input_line)
        return done

    def nick_command(self, nikname):
        """Handle nick name."""
        if not nikname:
            raise ClientError('No nickname provided.')
        if not self.NICKNAME.match(nikname):
            raise ClientError('Invalid nickname: %s.' % nikname)
        if nikname == self.nickname:
            raise ClientError('You are already known as %s.' % nikname)
        if self.server.users.get(nikname, None):
            raise ClientError(
                'There\'s already a user named "%s" here.' % nikname)
        old_nickname = None
        if self.nickname:
            old_nickname = self.nickname
            del(self.server.users[self.nickname])
        self.server.users[nikname] = self.wfile
        self.nickname = nikname
        if old_nickname:
            self.broadcast('%s is now known as %s' % (old_nickname,
                self.nickname))

    def quit_command(self, parting_words):
        """Quit command."""
        if parting_words:
            self.parting_words = parting_words
        return True

    def names_command(self, ignored):
        """Names command."""
        self.private_message(', '.join(self.server.users.keys()))

    def broadcast(self, message, include_this_user=True):
        """Broadcast message to all clients."""
        message = self._ensure_newline(message)
        for user, output in self.server.users.items():
            if include_this_user or user != self.nickname:
                output.write(message)

    def private_message(self, message):
        """Send private message to user."""
        self.wfile.write(self._ensure_newline(message))

    def _readline(self):
        """Read line from client."""
        return self.rfile.readline().strip()

    def _ensure_newline(self, newline):
        """Ensure the line ends with new line character."""
        if newline and newline[-1] != '\n':
    		newline += '\r\n'
        return newline

    def _parse_command(self, cmd):
        """Parse user command."""
        command_method, arg = None, None
        if cmd and cmd[0] == '/':
            if len(cmd) < 2:
                raise ClientError('Invalid command: "%s"' % cmd)
            command_and_arg = cmd[1:].split(' ', 1)
            if len(command_and_arg) == 2:
                command, arg = command_and_arg
            else:
                command, = command_and_arg
            command_method = getattr(self, command + '_command', None)
            if not command_method:
                raise ClientError('No such command: "%s"' % command)
        return command_method, arg


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Usage: %s [hostname] [port num]' % sys.argv[0]
        sys.exit(1)
    HOSTNAME = sys.argv[1]
    PORT = int(sys.argv[2])
    ChatServer((HOSTNAME, PORT), RequestHandler).serve_forever()
