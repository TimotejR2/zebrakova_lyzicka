from world import World
from config import DAYS, SPOONS, PRECISION
from decimal import Decimal, getcontext

SPOONS = Decimal(SPOONS)
getcontext().prec = PRECISION

def main():
    if SPOONS == 0 or DAYS == 0:
        raise ValueError('SPOONS and DAYS must be greater than 0')
    
    if SPOONS > DAYS:
        raise ValueError('SPOONS must be less than DAYS, probability is 1')

    new_queue, final_world = simulate()

    result(new_queue, final_world)

def simulate():
    simularion = World(used=0, probability=1)
    new_queue = [simularion]
    final_world = World(used=SPOONS, probability=0, parent=None)

    for i in range(DAYS):
        getcontext().prec = PRECISION + PRECISION * i * 2

        print('day',i)
        queue = new_queue.copy()

        new_queue = []
        for world in queue:
            # Exchange world from queue with its childs
            if add_world(world):
                for child in world.child:
                    new_queue.append(child)
            else:
                final_world.probability += world.probability
                print('not added')

        merge_duplicates(new_queue)
    return new_queue, final_world

def result(queue, final_world):
    if queue[-1].used == SPOONS:
        queue[-1].probability += final_world.probability

    with open('result.txt', 'w') as f:
        probability = count_probabilities(queue)
        f.write(str(probability) + '\n')

def count_probabilities(queue):
    # Count probabilitie that one selected was not used
    probability = 0
    for world in queue:
        probability += world.probability * (SPOONS - world.used) / SPOONS
    return probability

def merge_duplicates(queue):
    """
    Merge worlds with the same used spoons in the same queue (same day).

    This function goes through the queue and for each world, it checks if there is another world with the same used spoons. If so, it merges their probabilities and removes the duplicate world from the queue and its parent.
    """
    for world in queue:
        for world2 in queue:
            # Check if worlds are the same
            if world != world2 and world.used == world2.used:
                # Merge probabilities
                world.probability += world2.probability
                queue.remove(world2)
                # Remove world2 from parent
                world2.parent.child.remove(world2)
                   
def add_world(world : World):
    used = Decimal(world.used)
    probability = Decimal(world.probability)

    # If no new world possible to add, return
    if used == SPOONS:
        return False

    # Add world with used spoon
    if used > 0:
        new_probability = used / SPOONS * probability # Devide by probability to get total probability
        world.add_child(World(used=used, probability=new_probability, parent=world))
    
    # Add world with new spoon
    new_probability = (SPOONS - used) / SPOONS * probability # Devide by probability to get total probability
    world.add_child(World(used=used+1, probability=new_probability, parent=world))
    
    return True


if __name__ == '__main__':
    main()