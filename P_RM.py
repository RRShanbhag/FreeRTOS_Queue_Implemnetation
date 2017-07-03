"""
Partitionned EDF using PartitionedScheduler.
"""
from simso.core.Scheduler import SchedulerInfo
from simso.utils import PartitionedScheduler
from simso.schedulers import scheduler
import math

@scheduler("simso.schedulers.P_RM")
class P_RM(PartitionedScheduler):
    def init(self):
        PartitionedScheduler.init(
            self, SchedulerInfo("simso.schedulers.RM_mono"))

    def packer(self):
        # First Fit
        cpus = [[cpu, 0.0, 0.0] for cpu in self.processors]  # CPU, Utilization, number of  scheduled tasks on the CPU

        for task in self.task_list:

            j = 0

            # Find the processor with the utilization less than urm(x+1).
            for i, c in enumerate(cpus):
                no_of_tasks = c[2]  # x -> No of Tasks Scheduled
                x = no_of_tasks + 1  # to calculate URM(x+1)
                urm = x * (math.pow(2, 1 / x) - 1)  # URM(x+1)
                u = c[1] + float(task.wcet) / task.period  # Utilization
                if u < urm:
                    j = i
                    break  # processor found
            # Affect it to the task.
            self.affect_task_to_processor(task, cpus[j][0])

            # Update utilization.
            cpus[j][1] += float(task.wcet) / task.period

            # update task count
            cpus[j][2] += 1
        return True
