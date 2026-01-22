import time

class ViolationTracker:
    def __init__(self):
        self.active = {}

    def update(self, worker_id, missing_ppe):
        now = time.time()
        if missing_ppe:
            if worker_id not in self.active:
                self.active[worker_id] = now
            duration = now - self.active[worker_id]
            return duration
        else:
            if worker_id in self.active:
                del self.active[worker_id]
            return 0
