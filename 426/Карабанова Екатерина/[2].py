import random

# исходные данные
integer_list = list(range(1000000))
float_list = [random.uniform(-1, 1) for _ in range(99999)]
complex_points = [random.uniform(-1, 1) + random.uniform(-1, 1)*1j for _ in range(42000)]
book_excerpt = 'Платье - это нечто большее, нежели маскарадный костюм. В новой одежде человек становится иным, хотя сразу это не заметно. Тот, кто по-настоящему умеет носить платья, воспринимает что-то от них; как ни странно, платья и люди влияют друг на друга, и это не имеет ничего общего с грубым переодеванием на маскараде. Можно приспособиться к одежде и вместе с тем не потерять своей индивидуальности. Того, кто понимает это, платья не убивают, как большинство женщин, покупающих себе наряды. Как раз наоборот, такого человека платья любят и оберегают. Они помогают ему больше, чем любой духовник, чем неверные друзья и даже чем возлюбленный. Лилиан все это знала. Она знала, что шляпка, которая идет тебе, служит большей моральной опорой, чем целый свод законов. Она знала, что в тончайшем вечернем платье, если оно хорошо сидит, нельзя простудиться, зато легко простудиться в том платье, которое раздражает тебя, или же в том, двойник которого ты на этом же вечере видишь на другой женщине; такие вещи казались Лилиан неопровержимыми, как химические формулы. Но она знала. также, что в моменты тяжелых душевных переживаний платья могут стать либо добрыми друзьями, либо заклятыми врагами; без их помощи женщина чувствует себя совершенно потерянной, зато, когда они помогают ей, как помогают дружеские руки, женщине намного легче в трудный момент. Во всем этом нет ни грана пошлости, просто не надо забывать, какое большое значение имеют в жизни мелочи. Как хорошо, когда освоишь эту науку, - подумала Лилиан. К тому же она была почти единственная, еще доступная ей. У нее не осталось времени для того, чтобы оправдать свою жизнь чем-то большим; у нее не было времени даже для бунта. Бунт, о котором она мечтала когда-то, она уже совершила и теперь по временам начинала сомневаться в своей правоте. Сейчас ей осталось только одно - свести свои счеты с судьбой.'


sorting_algorithms = ['shaker sort', 'bubble sort', 'insertion sort', 'timsort']


def shaker_sort(arr):
    #Сортировка перемешиванием
    pass

def bubble_sort(arr):
    #Сортировка пузырьком
    pass

def insertion_sort(arr):
    #Сортировка вставкой
    pass

def timsort(arr):
    # гибридной сортировка timsort
    arr = sorted(arr)

for algorithm in sorting_algorithms:
    if algorithm == 'shaker sort':
        shaker_sort(integer_list)
    elif algorithm == 'bubble sort':
        bubble_sort(float_list)
    elif algorithm == 'insertion sort':
        insertion_sort(complex_points)
    elif algorithm == 'timsort':
        timsort(book_excerpt)

print("Сортировка integer:", integer_list[:20])
print("Сортировка float:", float_list[:20])
print("Сортировка complex:", complex_points[:20])
print("Сортировка book:", book_excerpt[:20])
