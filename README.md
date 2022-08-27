# AI-Project-Gobblet

Final project in the course 'Introduction to Artificial Intelligence' at The Hebrew University

-- Usage --  
    install the requirements with (create before a virtual environment if needed):  
    ``pip3 install -r requirements.txt``  
    Running command: ``python3 gobblet.py <ARGS>``  
    Running with human agent only works with adding --display and cannot run with more the one additional agent.  
    Arguments:

    --display       Add this argument to show GUI (only works with 2 agents)
    --iterations    Number of rounds between each two agents (default is 1)
    --agents        List of agents to run each one against the others:
        ALL     insert all agents except Human
        H       Human(human controlled agent)
        R       Random (performs random actions)
        RX      Reflex (chooses always the first legal action)
        MM_G    Minimax (with alpha-beta pruning) agent with General heuristic
        MM_C    Minimax (with alpha-beta pruning) agent with Corners heuristic
        MM_A    Minimax (with alpha-beta pruning) agent with Aggressive heuristic
        MMD_G   Minimax (with alpha-beta pruning and deviation random jumps) agent with General heuristic
        MMD_C   Minimax (with alpha-beta pruning and deviation random jumps) agent with Corners heuristic
        MMD_A   Minimax (with alpha-beta pruning and deviation random jumps) agent with Aggressive heuristic

Examples:  
    ``python3 gobblet.py --display --agents MM_G H``  
    ``python3 gobblet.py --agents ALL --iterations=10``  
    ``python3 gobblet.py --agents R RX MM_G MM_A --iterations=50``
 
