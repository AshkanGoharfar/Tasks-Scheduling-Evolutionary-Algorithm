import random
import math
from Individual import Individual
import numpy as np
from operator import itemgetter
from sklearn.metrics.pairwise import cosine_similarity
import operator
import matplotlib.pyplot as plt
import itertools
import secrets


def fitness(individual):
    return len(conditions(individual))


def individual_fitness(individual):
    individual_cond_2, cond_2_dict, c = individual_condition_2(individual)
    return len(
        individual_condition_1(individual) + individual_cond_2 + individual_condition_3(individual))


def fitness_gen(gen):
    return len(gen_condition_1(gen)) + len(gen_condition_3(gen))


def individual_condition_1(individual):
    false_condition_1 = []
    each_individual = individual
    for i in range(7):
        for j in range(2):
            bad_condition = list(set(each_individual[i][j]).intersection(each_individual[i][j + 1]))
            if bad_condition is not None:
                for node in bad_condition:
                    false_condition_1.append([node, 1])
    return false_condition_1


def condition_1(individual):
    false_condition_1 = []
    each_individual = individual.an_individual
    for i in range(7):
        for j in range(2):
            bad_condition = list(set(each_individual[i][j]).intersection(each_individual[i][j + 1]))
            if bad_condition is not None:
                for node in bad_condition:
                    false_condition_1.append([node, 1])
    return false_condition_1


def gen_condition_1(gen):
    false_condition_1 = []
    for j in range(2):
        bad_condition = list(set(gen[j]).intersection(gen[j + 1]))
        if bad_condition is not None:
            for node in bad_condition:
                false_condition_1.append([node, j, 1])
    return false_condition_1


def gen_condition_3(gen):
    false_condition_3 = []
    for j in range(3):
        if j == 0 and len(gen[j]) > 3 or len(gen[j]) < 2:
            false_condition_3.append([j, 3])
        elif j == 1 and len(gen[j]) > 4 or len(gen[j]) < 2:
            false_condition_3.append([j, 3])
        elif j == 2 and len(gen[j]) > 3 or len(gen[j]) < 0:
            false_condition_3.append([j, 3])
    return false_condition_3


def condition_2(individual):
    false_condition_2 = []
    each_individual = individual.an_individual
    employee_shifts = {}
    for i in range(7):
        for j in range(3):
            for k in range(len(each_individual[i][j])):
                if each_individual[i][j][k] not in employee_shifts:
                    employee_shifts[each_individual[i][j][k]] = 1
                else:
                    employee_shifts[each_individual[i][j][k]] += 1
                    if employee_shifts[each_individual[i][j][k]] > 5 and [each_individual[i][j][k],
                                                                          2] not in false_condition_2:
                        false_condition_2.append([each_individual[i][j][k], 2])
    return false_condition_2


def individual_condition_2(individual):
    false_condition_2 = []
    each_individual = individual
    employee_shifts = {}
    employee_loc = {}
    if len(each_individual) < 7:
        while len(each_individual) < 7:
            initialed_gen_9 = []
            for y in range(3):
                initialed_gen_10 = []
                for k in range(8):
                    initialed_gen_10.append(np.random.randint(1, 8 + 1))
                initialed_gen_9.append(list(dict.fromkeys(initialed_gen_10)))
            each_individual.append(initialed_gen_9)
    for i in range(7):
        for j in range(3):
            for k in range(len(each_individual[i][j])):
                if each_individual[i][j][k] not in employee_shifts:
                    employee_shifts[each_individual[i][j][k]] = 1
                    employee_loc[each_individual[i][j][k]] = [[i, j, k]]
                else:
                    employee_shifts[each_individual[i][j][k]] += 1
                    if employee_shifts[each_individual[i][j][k]] > 5:
                        employee_loc[each_individual[i][j][k]].append([i, j, k])
                        if [each_individual[i][j][k], 2] not in false_condition_2:
                            false_condition_2.append([each_individual[i][j][k], 2])
    return false_condition_2, employee_loc, employee_shifts


def individual_condition_3(individual):
    false_condition_3 = []
    each_individual = individual
    for i in range(7):
        for j in range(3):
            if j == 0 and len(each_individual[i][j]) > 3 or len(each_individual[i][j]) < 2:
                false_condition_3.append([[i, j], 3])
            elif j == 1 and len(each_individual[i][j]) > 4 or len(each_individual[i][j]) < 2:
                false_condition_3.append([[i, j], 3])
            elif j == 2 and len(each_individual[i][j]) > 3 or len(each_individual[i][j]) < 0:
                false_condition_3.append([[i, j], 3])
    return false_condition_3


def condition_3(individual):
    false_condition_3 = []
    each_individual = individual.an_individual
    for i in range(7):
        for j in range(3):
            if j == 0 and len(each_individual[i][j]) > 3 or len(each_individual[i][j]) < 2:
                false_condition_3.append([[i, j], 3])
            elif j == 1 and len(each_individual[i][j]) > 4 or len(each_individual[i][j]) < 2:
                false_condition_3.append([[i, j], 3])
            elif j == 2 and len(each_individual[i][j]) > 3 or len(each_individual[i][j]) < 0:
                false_condition_3.append([[i, j], 3])
    return false_condition_3


def conditions(individual):
    # print('Conditions :')
    # print(condition_1(individual))
    # print(condition_2(individual))
    # print(condition_3(individual))
    # print(condition_1(individual) + condition_2(individual) + condition_3(individual))
    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    return condition_1(individual) + condition_2(individual) + condition_3(individual)


# def generate_crossover(individuals, mutation_rate, num_of_nurses):
#     new_pop = []
#     for i in range(len(individuals)):
#         first_individual = individuals[(i + 1) % len(individuals)].an_individual
#         second_individual = individuals[i].an_individual
#         first_parent_gens = []
#         second_parent_gens = []
#         if len(first_individual) < 7 or len(second_individual) < 7:
#             while len(first_individual) < 7:
#                 initialed_gen_6 = []
#                 for u in range(3):
#                     initialed_gen_3 = []
#                     num_of_terms = np.random.randint(1, num_of_nurses + 1)
#                     for k in range(num_of_terms):
#                         initialed_gen_3.append(np.random.randint(1, num_of_nurses + 1))
#                     initialed_gen_6.append(list(dict.fromkeys(initialed_gen_3)))
#                 first_individual.append(initialed_gen_6)
#             while len(second_individual) < 7:
#                 initialed_gen_5 = []
#                 for g in range(3):
#                     initialed_gen_4 = []
#                     num_of_terms_1 = np.random.randint(1, num_of_nurses + 1)
#                     for k in range(num_of_terms_1):
#                         initialed_gen_4.append(np.random.randint(1, num_of_nurses + 1))
#                     initialed_gen_5.append(list(dict.fromkeys(initialed_gen_4)))
#                 second_individual.append(initialed_gen_5)
#         for j in range(7):
#             first_parent_gens.append([first_individual[j], fitness_gen(first_individual[j])])
#             second_parent_gens.append([second_individual[j], fitness_gen(second_individual[j])])
#         # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         # print('jhgcfuxtrjytzxjtxjtkzxtutrxu')
#         first_parent_gens = sorted(first_parent_gens, key=lambda x: x[1])
#         second_parent_gens = sorted(second_parent_gens, key=lambda x: x[1])
#         # print(first_parent_gens)
#         # print(second_parent_gens)
#         count = np.random.randint(4, 8)
#         # print(count)
#         new_child = []
#         for j in range(count):
#             new_gen = []
#             for k in range(3):
#                 if j % 2 == 0:
#                     if k == 0 or k == 2:
#                         new_gen.append(first_parent_gens[j][0][k])
#                     else:
#                         new_gen.append(second_parent_gens[j][0][k])
#                 else:
#                     if k == 0 or k == 2:
#                         new_gen.append(second_parent_gens[j][0][k])
#                     else:
#                         new_gen.append(first_parent_gens[j][0][k])
#             new_child.append(new_gen)
#         # print('count and new good child : ')
#         # print(count)
#         # print(new_child)
#         num_of_worst_nodes = 7 - count
#         flag_ok = 0
#         new_child_copy = new_child
#         ######################## ta inja dorste az in ja be baad bayad doros beshe #######################
#         worst_children = first_parent_gens + second_parent_gens
#         # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#         # print('before :')
#         # print(worst_children)
#         worst_children = sorted(worst_children, key=lambda x: x[1], reverse=True)
#         # print('after :')
#         # print(worst_children)
#         # print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
#         # new_child = crossover_fitness(worst_children)
#
#         pop_counter = 0
#         never_in_while = 0
#         while flag_ok == 0 and pop_counter < 14:
#             never_in_while = 1
#             j = 0
#             while j < num_of_worst_nodes and flag_ok == 0 and len(worst_children) > num_of_worst_nodes - 1:
#                 new_gen = []
#                 for k in range(3):
#                     if worst_children[j][0][k] not in new_gen:
#                         new_gen.append(worst_children[j][0][k])
#                     else:
#                         initialed_gen_8 = []
#                         num_of_terms_2 = np.random.randint(1, num_of_nurses + 1)
#                         for k in range(num_of_terms_2):
#                             initialed_gen_8.append(np.random.randint(1, num_of_nurses + 1))
#                         new_gen.append(list(dict.fromkeys(initialed_gen_8)))
#                 new_child_copy.append(new_gen)
#                 j += 1
#             if len(new_child_copy) < 7:
#                 new_child_copy = second_individual
#             if individual_fitness(new_child_copy) < individual_fitness(first_individual) or individual_fitness(
#                     new_child_copy) < individual_fitness(second_individual):
#                 new_child = new_child_copy
#                 flag_ok = 1
#                 # print('flag okkkkk ')
#             else:
#                 for s in range(len(new_child_copy) - num_of_worst_nodes, len(new_child_copy)):
#                     del new_child_copy[-1]
#                 pop_counter += 1
#                 del worst_children[0]
#         if flag_ok == 0 or len(new_child) < 7:
#             initialed_individual = []
#             for j in range(7):
#                 initialed_shift = []
#                 for l in range(3):
#                     initialed_gen = []
#                     num_of_terms_3 = np.random.randint(1, num_of_nurses + 1)
#                     for k in range(num_of_terms_3):
#                         initialed_gen.append(np.random.randint(1, num_of_nurses + 1))
#                     if list(dict.fromkeys(initialed_gen)) not in initialed_shift:
#                         initialed_shift.append(list(dict.fromkeys(initialed_gen)))
#                     else:
#                         initialed_gen_1 = []
#                         num_of_terms_4 = np.random.randint(1, num_of_nurses + 1)
#                         for k in range(num_of_terms_4):
#                             initialed_gen_1.append(np.random.randint(1, num_of_nurses + 1))
#                         initialed_shift.append(list(dict.fromkeys(initialed_gen_1)))
#                 initialed_individual.append(initialed_shift)
#             new_child = initialed_individual
#             print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
#             print(new_child)
#         new_child = mutation(new_child, mutation_rate, num_of_nurses)
#         new_individual = Individual(new_child)
#         new_individual.fitness = fitness(new_individual)
#         new_individual.false_conditions = conditions(new_individual)
#         new_pop.append(new_individual)
#     return new_pop

def generate_crossover(individuals, mutation_rate, num_of_nurses):
    new_pop = []
    initialed_indiv = []
    for i in range(len(individuals)):
        first_individual = individuals[(i + 1) % len(individuals)].an_individual
        second_individual = individuals[i].an_individual
        # first_parent_gens = []
        # second_parent_gens = []
        # for j in range(7):
        #     first_parent_gens.append([first_individual[j], fitness_gen(first_individual[j])])
        #     second_parent_gens.append([second_individual[j], fitness_gen(second_individual[j])])
        print('JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ')
        first_par_select = np.random.randint(1, 7)
        new_child = []
        all_nurses = [1, 2, 3, 4, 5, 6, 7, 8]
        # print(len(first_individual))
        len_sec_indiv = len(second_individual)
        for j in range(1, len_sec_indiv):
            second_individual[0].extend(second_individual[1])
            del second_individual[1]
        first_individual.extend(second_individual)
        len_first_indiv = len(first_individual)
        for j in range(1, len_first_indiv):
            first_individual[0].extend(first_individual[1])
            del first_individual[1]
        flag_better_fitness = 0
        num_of_proc = 0
        flag_increased_situate = 0
        initialed_indiv = first_individual[0]
        print('Na ga')
        print(len(first_individual[0]))
        while flag_better_fitness == 0 and num_of_proc < 5 and flag_increased_situate == 0:
            print('ndlasndlandland')
            # print(len(first_individual[0]))
            all_gens = []
            # while len(all_gens) < 21:
            print(initialed_indiv)
            # random.choices(list, k=2)
            all_gens = random.choice(initialed_indiv, k=21)
            print(all_gens)
            #
            # print(len(all_gens))
            # for k in range(21):
            #     all_gens.pop(random.randrange(len(all_gens)))
            print('KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk')
            new_child = all_gens
            new_child_copy = all_gens
            increase_chance = 0.2
            decrease_chance = 0.8
            chance = random.uniform(0, 1)
            print(chance)
            if increase_chance > chance:
                flag_increased_situate = 1
                flag_increased = 0
                checked_items = []
                while flag_increased == 0 and len(checked_items) < 21:
                    head = np.random.randint(0, 21)
                    if head not in checked_items:
                        checked_items.append(head)
                    else:
                        flag_head = 0
                        while flag_head == 0:
                            head = np.random.randint(0, 21)
                            if head not in checked_items:
                                flag_head = 1
                                checked_items.append(head)
                    unavailable_nurses = list(set(all_nurses) - set(new_child_copy[head]))
                    if len(unavailable_nurses) > 0:
                        new_child_copy[head].append(random.choice(unavailable_nurses))
                        new_child = new_child_copy
                        flag_find_empty = 1
                        flag_increased = 1

        #     else:
        #         flag_better_fitness = 0
        #         checked_items = []
        #         while flag_better_fitness == 0 and len(checked_items) < 21:
        #             head = np.random.randint(0, 21)
        #             if head not in checked_items:
        #                 checked_items.append(head)
        #             else:
        #                 flag_head = 0
        #                 while flag_head == 0:
        #                     head = np.random.randint(0, 21)
        #                     if head not in checked_items:
        #                         flag_head = 1
        #                         checked_items.append(head)
        #             if len(new_child_copy[head]) > 2:
        #                 new_child_copy[head].pop(random.randrange(len(new_child_copy[head])))
        #                 if individual_fitness(convert_2D_to_3D(new_child_copy)) < individual_fitness(
        #                         individuals[(i + 1) % len(individuals)].an_individual) or individual_fitness(
        #                         convert_2D_to_3D(new_child_copy)) < individual_fitness(individuals[i].an_individual):
        #                     new_child = new_child_copy
        #                     flag_better_fitness = 1
        #     num_of_proc += 1
        # print('before : ')
        # print(new_child)


def convert_2D_to_3D(child):
    n_child = []
    for i in range(7):
        n_child.append([child[i * 3 + 0], child[i * 3 + 1], child[i * 3 + 2]])
    return n_child
    #                     new_child_copy[head][gen_loc].pop(random.randrange(len(new_child_copy[head][gen_loc])))

    # print(len(first_individual))
    # while len(new_child) < first_par_select:
    #     gen = secrets.choice(first_individual)
    #     first_individual
    #     new_child_copy[head][gen_loc].pop(random.randrange(len(new_child_copy[head][gen_loc])))
    #     if gen not in new_child:
    #         new_child.append(gen)
    # while len(new_child) < 7:
    #     gen = secrets.choice(second_individual)
    #     if gen not in new_child:
    #         new_child.append(gen)

    # print('before: ')
    # print(new_child)
    # new_child_copy = new_child
    # increase_chance = 0.2
    # decrease_chance = 0.8
    # chance = random.uniform(0, 1)
    # if increase_chance > chance:
    #     flag_increased = 0
    #     checked_items = []
    #     while flag_increased == 0 and len(checked_items) < 7:
    #         head = np.random.randint(0, 7)
    #         if head not in checked_items:
    #             checked_items.append(head)
    #         else:
    #             flag_head = 0
    #             while flag_head == 0:
    #                 head = np.random.randint(0, 7)
    #                 if head not in checked_items:
    #                     flag_head = 1
    #                     checked_items.append(head)
    #         flag_find_empty = 0
    #         checked_gens = []
    #         while flag_find_empty == 0 and len(checked_gens) < 3:
    #             gen_loc = np.random.randint(0, 3)
    #             if gen_loc not in checked_gens:
    #                 checked_gens.append(gen_loc)
    #             else:
    #                 flag_gen_loc = 0
    #                 while flag_gen_loc == 0:
    #                     gen_loc = np.random.randint(0, 3)
    #                     if gen_loc not in checked_gens:
    #                         flag_gen_loc = 1
    #                         checked_gens.append(gen_loc)
    #             unavailable_nurses = list(set(all_nurses) - set(new_child_copy[head][gen_loc]))
    #             if len(unavailable_nurses) > 0:
    #                 new_child_copy[head][gen_loc].append(random.choice(unavailable_nurses))
    #                 new_child = new_child_copy
    #                 flag_find_empty = 1
    #                 flag_increased = 1
    # else:
    #     flag_better_fitness = 0
    #     checked_items = []
    #     while flag_better_fitness == 0 and len(checked_items) < 7:
    #         flag_increased = 0
    #         checked_items = []
    #         while flag_increased == 0 and len(checked_items) < 7:
    #             head = np.random.randint(0, 7)
    #             if head not in checked_items:
    #                 checked_items.append(head)
    #             else:
    #                 flag_head = 0
    #                 while flag_head == 0:
    #                     head = np.random.randint(0, 7)
    #                     if head not in checked_items:
    #                         flag_head = 1
    #                         checked_items.append(head)
    #             flag_find_answer = 0
    #             checked_gens = []
    #             while flag_find_answer == 0 and len(checked_gens) < 3:
    #                 gen_loc = np.random.randint(0, 3)
    #                 if gen_loc not in checked_gens:
    #                     checked_gens.append(gen_loc)
    #                 else:
    #                     flag_gen_loc = 0
    #                     while flag_gen_loc == 0:
    #                         gen_loc = np.random.randint(0, 3)
    #                         if gen_loc not in checked_gens:
    #                             flag_gen_loc = 1
    #                             checked_gens.append(gen_loc)
    #                 if len(new_child_copy[head][gen_loc]) > 2:
    #                     new_child_copy[head][gen_loc].pop(random.randrange(len(new_child_copy[head][gen_loc])))
    #                     if individual_fitness(new_child_copy) > individual_fitness(new_child):
    #                         new_child = new_child_copy
    #                         flag_find_answer = 1
    #                         flag_better_fitness = 1
    # print('after: ')
    # print(new_child)


def mutation(new_child, mutation_rate, num_of_nurses):
    mutation_chance = random.uniform(0, 1)
    if mutation_chance < mutation_rate:
        which_day = np.random.randint(0, 7)
        daily_shifts_1 = np.arange(0, 3)
        num_of_terms_5 = np.random.randint(1, 4)
        selected_shifts = np.random.choice(daily_shifts_1, num_of_terms_5, replace=False)
        for e in selected_shifts:
            num_of_terms_6 = np.random.randint(1, num_of_nurses + 1)
            initialed_gen_9 = []
            for d in range(num_of_terms_6):
                initialed_gen_9.append(np.random.randint(1, num_of_nurses + 1))
            new_child[which_day][e] = list(dict.fromkeys(initialed_gen_9))
    return new_child

    # initialed_shift.append(list(dict.fromkeys(initialed_gen_1)))


def crossover_fitness(child):
    better_fitness_flag = 0
    changed_gens = child
    while better_fitness_flag == 0:
        changed_gens = child
        for i in range(7):
            changed_gens.pop(random.randrange(len(changed_gens)))
        for i in range(len(changed_gens)):
            del changed_gens[i][1]
        # print(changed_gens)
        # changed_gens = changed_gens[0]
        # print(len(changed_gens))
        # child = child[0:candidate_gens] + changed_gens
        # print(individual_fitness(changed_gens[0]))
        print(changed_gens)
        fitness_new_child = individual_fitness(changed_gens[0])
        if individual_fitness(child[0][0:7]) > fitness_new_child or individual_fitness(
                child[0][7:14]) > fitness_new_child:
            better_fitness_flag = 1
    print(':;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
    # print(changed_gens)
    return changed_gens[0]
