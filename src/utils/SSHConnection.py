import paramiko
class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    # 下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    # 上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    # 执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print(data.decode('utf-8'))
            data.strip()  # 打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err)
            err.strip()  # 输出错误结果
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

def main():
    conn = SSHConnection('9.197.49.49',26,'root','l0destone')
    conn.exec_command("svcinfo lsnode 1 | grep -w name| awk '{print $2}'")
    conn.exec_command('svcinfo lsnode 2 | grep -w name| awk "{print $2}"')


if __name__ == '__main__':
    main()




