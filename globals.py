class Style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


MAX = 0
MIN = 1
BLUE = 'BLUE'
RED = 'RED'
OUTSIDE = -1
ROW_COL_LENGTH = 3
SMALL = 1
MEDIUM = 2
LARGE = 3
NONE = -1
DRAW = 'DRAW'
COLORS = [BLUE, RED]
SIZES = [SMALL, MEDIUM, LARGE]
STACKS_NUM = 2
TOTAL_ACTIONS = 'total_actions'
TOTAL_TIME = 'total_time'
AVG_ACTION_TIME = 'avg_action_time'
WINS = 'wins'
HUNDRED_FLOAT = 100.0
SECONDS_TO_MILLISECONDS = 1000.0
MAX_TURNS_ALLOWED = 30
SEARCH_DEPTH = 2
ALL = 'ALL'

# Agents
HUMAN = 'H'
RANDOM = 'R'
REFLEX = 'RX'
MINIMAX_GENERAL = 'MM_G'
MINIMAX_CORNERS = 'MM_C'
MINIMAX_AGGRESSIVE = 'MM_A'
MINIMAX_DEV_GENERAL = 'MMD_G'
MINIMAX_DEV_CORNERS = 'MMD_C'
MINIMAX_DEV_AGGRESSIVE = 'MMD_A'
ALL_AGENTS = [HUMAN, RANDOM, REFLEX, MINIMAX_GENERAL, MINIMAX_DEV_GENERAL,
              MINIMAX_CORNERS, MINIMAX_DEV_CORNERS, MINIMAX_AGGRESSIVE, MINIMAX_DEV_AGGRESSIVE]
ALL_AGENTS_WITHOUT_HUMAN = [RANDOM, REFLEX, MINIMAX_GENERAL, MINIMAX_DEV_GENERAL,
                            MINIMAX_CORNERS, MINIMAX_DEV_CORNERS, MINIMAX_AGGRESSIVE, MINIMAX_DEV_AGGRESSIVE]

USAGE_HELP = 'Usage:\n' \
             'Running with human agent only works with adding --display and cannot run with more the one additional agent\n\n' \
             '--display\tAdd this argument to show GUI (only works with 2 agents)\n' \
             '--iterations\tNumber of rounds between each two agents (default is 1)\n' \
             '--agents <agent1> <agent2> ...\tList of agents to run each one against the others:\n' \
             '\tALL\t\t\tinsert all agents except Human\n' \
             '\tH\t\t\tHuman(human controlled agent)\n' \
             '\tR\t\t\tRandom (performs random actions)\n' \
             '\tRX\t\t\tReflex (chooses always the first legal action)\n' \
             '\tMM_G\t\tMinimax (with alpha-beta pruning) agent with General heuristic\n' \
             '\tMM_C\t\tMinimax (with alpha-beta pruning) agent with Corners heuristic\n' \
             '\tMM_A\t\tMinimax (with alpha-beta pruning) agent with Aggressive heuristic\n' \
             '\tMMD_G\t\tMinimax (with alpha-beta pruning and deviation random jumps) agent with General heuristic\n' \
             '\tMMD_C\t\tMinimax (with alpha-beta pruning and deviation random jumps) agent with Corners heuristic\n' \
             '\tMMD_A\t\tMinimax (with alpha-beta pruning and deviation random jumps) agent with Aggressive heuristic\n'
