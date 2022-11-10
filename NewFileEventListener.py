from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileMovedEvent

class NewFileListener():
    """
        a Basic File listener that uses the watchdog library
    """
    def __init__(self, folder_path, onNewFileFunc):
        """_summary_

        Args:
            folderPath (string): a path to the folder to listen to
            onNewFileFunc ((newFilePath) -> None ): the function that is called for each creation of the new file
        """

        self.__observer = Observer()
        self.__observer.schedule(NewFileEventHandler(onNewFileFunc), folder_path, recursive=False)
    
    def start_listenning(self):
        self.__observer.start()

    def stop_listenning(self):
        self.__observer.stop()
        self.__observer.join()


class NewFileEventHandler(FileSystemEventHandler):
    def __init__(self, onNewFileFunc):
        self.onNewFileFunc = onNewFileFunc
    
    def on_closed(self, event):
        self.onNewFileFunc(event.src_path)
        return super().on_closed(event)