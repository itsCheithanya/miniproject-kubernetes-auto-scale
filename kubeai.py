```
    
    import time

class KubernetesHPA:
    def __init__(self, cmin, cmax, target_cpu_utilization, scaling_interval, scaling_tolerance, downscale_stabilization):
        self.cmin = cmin
        self.cmax = cmax
        self.target_cpu_utilization = target_cpu_utilization
        self.scaling_interval = scaling_interval
        self.scaling_tolerance = scaling_tolerance
        self.downscale_stabilization = downscale_stabilization
        self.last_downscale_time = time.time()

        self.current_cpu_utilization = 0.0
        self.current_pod_count = 1

    def should_scale(self):
        if time.time() - self.last_downscale_time < self.downscale_stabilization:
            return False
        return abs(self.current_cpu_utilization - self.target_cpu_utilization) > self.scaling_tolerance

    def scale(self):
        if self.current_cpu_utilization < self.target_cpu_utilization:
            self.current_pod_count = min(self.current_pod_count * 2, self.cmax)
        else:
            self.current_pod_count = max(self.current_pod_count // 2, self.cmin)
        self.current_pod_count = max(self.cmin, min(self.cmax, self.current_pod_count))

    def update_cpu_utilization(self, cpu_utilization):
        self.current_cpu_utilization = cpu_utilization

    def run_scaling_iteration(self):
        if self.should_scale():
            self.scale()
        self.last_downscale_time = time.time()
```
