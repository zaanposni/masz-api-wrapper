from rich.console import Console

class MASZLogLevel:
    VERBOSE = 0
    INFO = 1
    CRITICAL = 2

class WithDummy:
    def __enter__(self, *args):
        pass
    def __exit__(self, *args):
        pass

class MASZConsole(Console):
    def __init__(self, log_level: MASZLogLevel = MASZLogLevel.INFO):            
        super().__init__()
        self.log_level = log_level
        
    def verbose(self, string: str):
        if self.log_level == 0:
            self.log(f"[bright_black][V][/bright_black] {string}")

    def info(self, string: str):
        if self.log_level <= 1:
            self.log(f"[bright_black][[white]I[bright_black]][/bright_black] {string}")

    def critical(self, string: str):
            self.log(f"[bright_black][[bright_red]C[bright_black]][/bright_black] {string}")

    def info_status(self, string: str):
        if self.log_level <= 1:
            return self.status(string)
        return WithDummy()

    def verbose_status(self, string: str):
        if self.log_level == 0:
            return self.status(string)
        return WithDummy()

console = MASZConsole()
