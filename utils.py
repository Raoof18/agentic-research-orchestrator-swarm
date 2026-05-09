import time


def performance_logger(func):
    async def wrapper(self, *args, **kwargs):

        start = time.perf_counter()

        task_name = self.TASK_MAPPING.get(self.role, "Task")

        print(f"[LOG] Agent {self.name} our {self.role} has started task: {task_name}.")

        result = await func(self, *args, **kwargs)

        end = time.perf_counter()

        duration = end - start

        print(f"[LOG] Agent {self.name} finished in {duration}s.")

        return result
    
    return wrapper