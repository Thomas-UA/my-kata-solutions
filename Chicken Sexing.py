def correctness(bobs_decisions, expert_decisions):
    correct_sexing = 0.0
    for i in range(0, len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            correct_sexing += 1
        elif (bobs_decisions[i] != expert_decisions[i]) and \
        ((bobs_decisions[i] == '?' or expert_decisions[i] == '?')):
            correct_sexing += 0.5
        else:
            correct_sexing += 0
    return correct_sexing