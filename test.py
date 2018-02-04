import easy_gene


def test_select_floats():
    population = [
        {'param1': 1.0, 'param2': 2.0, 'param3': 3.0},
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0},
        {'param1': 1.0, 'param2': 2.0, 'param3': 3.0}
    ]
    scores = [0, 1, 0]
    population = easy_gene.evolve(
        population=population,
        scores=scores,
        num_parents=1,
        mutation_rates=None
    )
    assert population == [
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0},
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0},
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0}
    ]


def test_select_bools():
    population = [
        {'param1': True, 'param2': False, 'param3': False},
        {'param1': False, 'param2': True, 'param3': False},
        {'param1': False, 'param2': False, 'param3': True}
    ]
    scores = [0, 0, 1]
    population = easy_gene.evolve(
        population=population,
        scores=scores,
        num_parents=1,
        mutation_rates=None
    )
    assert population == [
        {'param1': False, 'param2': False, 'param3': True},
        {'param1': False, 'param2': False, 'param3': True},
        {'param1': False, 'param2': False, 'param3': True}
    ]

def test_mutate():
    population = [
        {'param1': 1.0, 'param2': 2.0, 'param3': 3.0},
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0},
        {'param1': 1.0, 'param2': 2.0, 'param3': 3.0}
    ]
    scores = [0, 1, 0]
    population = easy_gene.evolve(
        population=population,
        scores=scores,
        num_parents=1,
        mutation_rates={'param1': 1.0, 'param2': 1.0, 'param3': 1.0}
    )
    assert population != [
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0},
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0},
        {'param1': 6.0, 'param2': 7.0, 'param3': 8.0}
    ]
