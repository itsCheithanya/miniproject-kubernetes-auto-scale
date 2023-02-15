# miniproject-kubernetes-auto-scale
The KubernetesHPA class is defined with the required parameters: cmin, cmax, target_cpu_utilization, scaling_interval, scaling_tolerance, and downscale_stabilization.
    The current CPU utilization and pod count are stored as instance variables.
    The should_scale method determines if a scaling decision should be made based on the difference between the current CPU utilization and the target CPU utilization, and the scaling tolerance. If the last downscale operation was performed within the downscale stabilization time, no downscale operation is performed.
    The scale method updates the pod count based on the current CPU utilization and the target CPU utilization. The pod count is limited by the minimum and maximum allowed values.
    The update_cpu_utilization method is called to update the current CPU utilization.
    The run_scaling_iteration method runs a single scaling iteration. It checks if a scaling decision should be made, and if so, scales the pod count. It also updates the time of the last downscale operation.
    
    
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
