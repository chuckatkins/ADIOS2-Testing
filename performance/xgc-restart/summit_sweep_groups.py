from codar.savanna.machines import SummitNode

from summit_node_layouts import summit_node_layouts
from sweep_groups_helper import create_sweep_groups

# Parameters
writer_np               = [384, 1536, 6144]
reader_np_ratio         = [1]
writers_per_node_summit = [6]
size_per_pe             = []
engines                 = ['bp4']
run_repetitions         = 0
batch_job_timeout_secs  = 3600
per_experiment_timeout  = 600

#node_layouts = summit_node_layouts('writer', 'reader')
#n = SummitNode()
#for i in range(writers_per_node_summit[0]):
#   n.cpu[i] = "{}:{}".format("writer", i)
#    n.cpu[i + writers_per_node_summit[0]] = "{}:{}".format("reader", i)
node_layouts = []
node_layouts.append([ {'writer': writers_per_node_summit[0]}, {'reader': writers_per_node_summit[0]}])


sweep_groups = create_sweep_groups ('summit',
                                    writer_np,
                                    reader_np_ratio,
                                    size_per_pe,
                                    engines,
                                    node_layouts,
                                    run_repetitions,
                                    batch_job_timeout_secs,
                                    per_experiment_timeout)

