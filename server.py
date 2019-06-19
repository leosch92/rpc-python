import rpyc
import time
class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass
    def on_disconnect(self, conn):
        #  código que é executado quando uma conexão é finalizada, caso seja necessário
        pass
    def exposed_get_sum(self, collection):
        start = time.time()
        sum = 0
        for number in collection:
            sum += number
        end = time.time()
        print("Procedimento no servidor: {}".format(end-start))
        return sum
        
#Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
