import socket, sys
from PyQt5.QtWidgets import QMessageBox

def connect():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('hc.baigaohao.top',3000))
        s.sendall("loading".encode("GB2312"))
        s.recv(1024)
    except OSError:
        s.close()
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('hc2.baigaohao.top',3000))
            s.sendall("loading".encode("GB2312"))
            s.recv(1024)
        except OSError:
            s.close()
            return False
        except:
            s.close()
            return connect()
    except:
        s.close()
        return connect()

    return s

def command(self,msg):
    lit = msg.split("：")

    if lit[0] == "tip":
        QMessageBox.warning(self,"警告",lit[1],QMessageBox.Ok)
        sys.exit()

    elif lit[0] == "message":
        QMessageBox.warning(self,"警告",lit[1]+"："+lit[2],QMessageBox.Ok)
        return 0

    elif lit[0] == "login_no":
        QMessageBox.warning(self,"警告",lit[1],QMessageBox.Ok)
        return 0

    return 1