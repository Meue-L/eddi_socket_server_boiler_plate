from receiver.repository.receiver_repository import ReceiverRepository


class ReceiverRepositoryImpl(ReceiverRepository):
    __instance = None
    __clientSocket = None

    __ipcAcceptorChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def injectClientSocket(self, clientSocket):
        self.__clientSocket = clientSocket

    def injectAcceptChannel(self, ipcAcceptorChannel):
        self.__ipcAcceptorChannel = ipcAcceptorChannel
