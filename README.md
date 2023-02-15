# miniproject-kubernetes-auto-scale
The KubernetesHPA class is defined with the required parameters: cmin, cmax, target_cpu_utilization, scaling_interval, scaling_tolerance, and downscale_stabilization.
    The current CPU utilization and pod count are stored as instance variables.
    The should_scale method determines if a scaling decision should be made based on the difference between the current CPU utilization and the target CPU utilization, and the scaling tolerance. If the last downscale operation was performed within the downscale stabilization time, no downscale operation is performed.
    The scale method updates the pod count based on the current CPU utilization and the target CPU utilization. The pod count is limited by the minimum and maximum allowed values.
    The update_cpu_utilization method is called to update the current CPU utilization.
    The run_scaling_iteration method runs a single scaling iteration. It checks if a scaling decision should be made, and if so, scales the pod count. It also updates the time of the last downscale operation.
    
    
