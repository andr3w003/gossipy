from gossipy.core import AntiEntropyProtocol, CreateModelMode, StaticP2PNetwork
from gossipy.data import load_classification_dataset, DataDispatcher
from gossipy.data.handler import ClassificationDataHandler
from gossipy.model.handler import PegasosHandler
from gossipy.model.nn import AdaLine
from gossipy.node import GossipNode
from gossipy.simul import GossipSimulator, SimulationReport

X, y = load_classification_dataset("spambase", as_tensor=True)
y = 2*y - 1 #convert 0/1 labels to -1/1

data_handler = ClassificationDataHandler(X, y, test_size=.1)
data_dispatcher = DataDispatcher(data_handler, n=100, eval_on_user=False, auto_assign=True)

topology = StaticP2PNetwork(num_nodes=data_dispatcher.size(), topology=None)

model_handler = PegasosHandler(net=AdaLine(data_handler.size(1)),
                               learning_rate=.01,
                               create_model_mode=CreateModelMode.MERGE_UPDATE)

nodes = GossipNode.generate(data_dispatcher=data_dispatcher,
                            p2p_net=topology,
                            model_proto=model_handler,
                            round_len=100,
                            sync=False)


simulator = GossipSimulator(
    nodes=nodes,
    data_dispatcher=data_dispatcher,
    delta=100,
    protocol=AntiEntropyProtocol.PUSH,
    sampling_eval=.1
)

report = SimulationReport()
simulator.add_receiver(report)
simulator.init_nodes(seed=42)
simulator.start(n_rounds=200)



print(report.get_evaluation(False)[-1])


simulator_crypt = GossipSimulator(
    nodes=nodes,
    data_dispatcher=data_dispatcher,
    delta=100,
    protocol=AntiEntropyProtocol.PUSH,
    sampling_eval=.1,
    cryptography=True
)

report_crypt = SimulationReport()
simulator_crypt.add_receiver(report_crypt)
simulator_crypt.init_nodes(seed=42)
simulator_crypt.start(n_rounds=200)

print(report_crypt.get_evaluation(False)[-1])

