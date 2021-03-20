from Operations import *
import matplotlib.pyplot as plt
import numpy as np

population = []

populationSize = 10
numberOfRemainingGeneration = 0
tornumentSize = 20
# num_of_weeks = 3
individualSize = 7 * 3
mutation_rate = 0.3
# for raising diversity you increase normal_distribution_value_1
# normal_distribution_value_1 = 20
# normal_distribution_value_2 = 80
generation = []
best_individual = []
best_answer_fitness = 0
best_answer_gen = [1, 2]
counter = 1000
num_of_nurses = 8
# shift_period = 3
num_of_daily_shift = 3
# Generate new populations
for i in range(populationSize):
    initialed_individual = []
    for j in range(7):
        initialed_shift = []
        for l in range(num_of_daily_shift):
            initialed_gen = []

            initialed_shift.append([1, 2, 3, 4, 5, 6, 7, 8])


            #
            # for k in range(num_of_nurses):
            #     initialed_gen.append(np.random.randint(1, num_of_nurses + 1))
            # if list(dict.fromkeys(initialed_gen)) not in initialed_shift:
            #     initialed_shift.append(list(dict.fromkeys(initialed_gen)))
            #     print(',d;laskd;amd;asmd;alsmd;asm;dmas')
            #     print('initialed shift 1 :')
            #     print(list(dict.fromkeys(initialed_gen)))
            # else:
            #     initialed_gen_1 = []
            #     for k in range(num_of_nurses):
            #         initialed_gen_1.append(np.random.randint(1, num_of_nurses + 1))
            #     print('initialed shift 2:')
            #     print(list(dict.fromkeys(initialed_gen_1)))
            #     initialed_shift.append(list(dict.fromkeys(initialed_gen_1)))


        initialed_individual.append(initialed_shift)
    generation.append(Individual(initialed_individual))
print('Generation :')
print(generation[0].an_individual)

# print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
# for item in generation:
#     print(item.an_individual)
# print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
report = []
report_1 = []

flag_terminate = 0
while flag_terminate == 0 and numberOfRemainingGeneration < counter:
    print('new generation : ')
    for individual in generation:
        # print(individual.an_individual)
        if len(individual.an_individual) < 7:
            while len(individual.an_individual) < 7:
                initialed_gen_7 = []
                for y in range(3):
                    initialed_gen_2 = []
                    for k in range(num_of_nurses):
                        initialed_gen_2.append(np.random.randint(1, num_of_nurses + 1))
                    initialed_gen_7.append(list(dict.fromkeys(initialed_gen_2)))
                individual.an_individual.append(initialed_gen_7)

        for item in individual.an_individual:
            if len(item) > 3:
                while len(item) > 3:
                    del item[-1]
        individual.fitness = fitness(individual)
    # print(fitness(generation[0]))
    # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    generation_sorted = sorted(generation, key=operator.attrgetter('fitness'))
    # numberOfRemainingGeneration += 1
    population_selected = generation_sorted[0:tornumentSize]
    numberOfRemainingGeneration += 1

    new_generation = generate_crossover(population_selected, mutation_rate, num_of_nurses)

#     report.append({'generation': numberOfRemainingGeneration,
#                    'mean_fitness': np.mean(np.array([item.fitness for item in generation])),
#                    'worst_fitness': generation_sorted[len(generation_sorted) - 1].fitness,
#                    'best_fitness': generation_sorted[0].fitness})
#     print(report)
#     all_gens = new_generation + generation
#     all_gens_sorted = sorted(all_gens, key=operator.attrgetter('fitness'))
#     generation = all_gens_sorted[0:populationSize]
#
#     print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#     print(generation[0].an_individual)
#     # print(conditions(generation[0]))
#     print(generation[0].fitness)
#     print(generation[0].false_conditions)
#     condition = conditions(generation[0])
#     flag_ideal = 0
#     bad_cases = []
#     for item in condition:
#         if item[1] != 2:
#             flag_ideal = 1
#         else:
#             bad_cases.append(item[0])
#     if flag_ideal == 0:
#         # print('yes')
#         best_individual = generation[0].an_individual
#         a, b, cond_1_dict = individual_condition_2(best_individual)
#         # print('my dict : ')
#         # print(cond_1_dict)
#         # print('before : ')
#         # print(best_individual)
#         for a in range(len(best_individual)):
#             for b in range(len(best_individual[a])):
#                 for c in range(len(best_individual[a][b])):
#                     if c < len(best_individual[a][b]):
#                         # print('dicttttt : ')
#                         # print(cond_1_dict)
#                         if best_individual[a][b][c] in bad_cases and cond_1_dict[best_individual[a][b][c]] > 5:
#                             # print('areeee')
#                             if len(best_individual[a][b]) > 1:
#                                 if b == 0 and len(best_individual[a][b]) > 2:
#                                     # del generation[0].an_individual[a][b][c]
#                                     cond_1_dict[best_individual[a][b][c]] -= 1
#                                     best_individual[a][b].remove(best_individual[a][b][c])
#                                     # best_individual[a][b].remove(best_individual[a][b][c])
#                                 elif b == 1 and len(best_individual[a][b]) > 2:
#                                     cond_1_dict[best_individual[a][b][c]] -= 1
#                                     best_individual[a][b].remove(best_individual[a][b][c])
#                                     # best_individual[a][b].remove(best_individual[a][b][c])
#                                 elif b == 2 and len(best_individual[a][b]) > 1:
#                                     cond_1_dict[best_individual[a][b][c]] -= 1
#                                     best_individual[a][b].remove(best_individual[a][b][c])
#                                     # best_individual[a][b].remove(best_individual[a][b][c])
#         # print('after : ')
#         # print(best_individual)
#         if individual_fitness(best_individual) == 0:
#             # print('hooooooooooorrraaaaaaaaaaaaa')
#             generation[0].an_individual = best_individual
#             generation[0].fitness = fitness(generation[0])
#     if generation[0].fitness == 0:
#         flag_terminate = 1
#
#
#
#
# mean_MSE = [item['mean_fitness'] for item in report]
# worst_MSE = [item['worst_fitness'] for item in report]
# best_MSE = [item['best_fitness'] for item in report]
# generation = [item['generation'] for item in report]
#
# fig,axs = plt.subplots(1, constrained_layout=True)
# axs.plot(mean_MSE, '--')
# axs.set_xlabel('time ')
# axs.set_title('mean fitness')
# axs.set_ylabel('fitness')
# plt.show()
# fig,axs = plt.subplots(1, constrained_layout=True)
# axs.plot(worst_MSE, '--')
# axs.set_xlabel('time ')
# axs.set_title('worst fitness')
# axs.set_ylabel('fitness')
# plt.show()
# fig,axs = plt.subplots(1, constrained_layout=True)
# axs.plot(best_MSE, '--')
# axs.set_xlabel('time ')
# axs.set_title('best fitness')
# axs.set_ylabel('fitness')
# plt.show()