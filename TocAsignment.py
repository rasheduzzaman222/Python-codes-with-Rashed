# DFA Access Control System for Smart Building
# Step 3: Implementation as per assignment requirements

# Define authentication symbols (Σ)
symbols = {"CD", "FP", "RT", "PN", "FC", "VC", "BC", "AO"}

# Define unique sequences per zone (must match DFA design)
zone_sequences = {
    "LO": ["CD", "PN", "FC", "FP"],
    "LAB": ["CD", "FP", "RT", "PN", "FC"],
    "SR": ["FP", "RT", "BC", "AO"],
    "EL": ["CD", "FC", "PN", "AO"],
    "RW": ["VC", "FP", "RT", "PN", "BC"],
    "DC": ["FP", "BC", "RT", "AO"],
    "MR": ["CD", "PN", "VC", "FP"],
    "SO": ["AO", "FP", "RT", "PN"]
}

# Build DFA transition function
# States will be numbered: q0 (start), q1,q2,...; q_reject as special
transitions = {}
accepting_states = {}

# Start state
state_counter = 1
start_state = "q0"
reject_state = "q_reject"

# Helper: create states from sequences
def add_sequence(seq, zone):
    global state_counter
    current = start_state
    for symbol in seq:
        next_state = f"q{state_counter}"
        state_counter += 1
        # Add transition
        transitions[(current, symbol)] = next_state
        current = next_state
    # Mark final state as accepting
    accepting_states[current] = zone

# Add all sequences to DFA
for zone, seq in zone_sequences.items():
    add_sequence(seq, zone)

# For all undefined transitions, go to reject_state
all_states = {start_state, reject_state} | set(s for (s, _) in transitions.keys()) | set(transitions.values())
for st in all_states:
    for sym in symbols:
        if (st, sym) not in transitions:
            transitions[(st, sym)] = reject_state

# Reject state loops to itself
for sym in symbols:
    transitions[(reject_state, sym)] = reject_state

# DFA Simulation Function
def dfa_simulate(input_sequence):
    current_state = start_state
    for symbol in input_sequence:
        if symbol not in symbols:
            return "Access Denied (Invalid symbol)"
        current_state = transitions.get((current_state, symbol), reject_state)
        if current_state == reject_state:
            return "Access Denied"
    # After consuming all inputs
    if current_state in accepting_states:
        return f"Access Granted: {accepting_states[current_state]}"
    else:
        return "Access Denied"

# --------------------------
# Example Runs
# --------------------------
tests = [
    ["CD", "PN", "FC", "FP"],  # LO correct
    ["FP", "RT", "BC", "AO"],  # SR correct
    ["CD", "PN", "VC", "FP"],  # MR correct
    ["CD", "PN", "FC"],        # Incomplete LO
    ["FP", "RT", "BC", "AO", "CD"], # Extra after SR
    ["CD", "QR", "FP", "FP"],  # Invalid symbol
    ["AO", "FP", "RT", "PN"]   # SO correct
]

for t in tests:
    print(f"Input: {t} -> {dfa_simulate(t)}")
