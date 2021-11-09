set_length = int(input())

main_set = set(map(int, input().split(" ")))

operations = int(input())

for i in range(operations):
    operations_name , set_length = input().split()
    updater_set = set(map(int, input().split(" ")))
    
    if operations_name == "update":
        main_set.update(updater_set)
    elif operations_name == "intersection_update":
        main_set.intersection_update(updater_set)
    elif operations_name == "difference_update":
        main_set.difference_update(updater_set)
    elif operations_name == "symmetric_difference_update":
        main_set.symmetric_difference_update(updater_set)
    else:
        assert False

print(sum(main_set))