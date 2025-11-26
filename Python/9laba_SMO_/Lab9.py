import numpy as np

num_requests = 1000
mu_service = 1.0

def system_state(t):
    phase = t % 300
    if phase < 100:
        return "Перегрузка"
    elif phase < 200:
        return "Активна"
    return "Простой"

arrival_times = []
current_time = 0.0

while len(arrival_times) < num_requests:
    lam = {"Перегрузка": 1.5, "Активна": 0.8, "Простой": 0.2}[system_state(current_time)]
    current_time += np.random.exponential(1 / lam)
    arrival_times.append(current_time)

arrival_times = np.array(arrival_times)
service_times = np.random.exponential(1 / mu_service, num_requests)

last_departure = 0.0
times_in_states = {state: 0.0 for state in ["Перегрузка", "Активна", "Простой"]}
wait_times = np.empty(num_requests)
departure_times = np.empty(num_requests)
system_times = np.empty(num_requests)
queue_lengths = []

current_state = system_state(0)
state_start_time = 0.0

for i, arrival in enumerate(arrival_times):
    state_now = system_state(arrival)
    if current_state != state_now:
        times_in_states[current_state] += arrival - state_start_time
        current_state, state_start_time = state_now, arrival

    queue_length = 0
    for j in range(i):
        if departure_times[j] > arrival:
            queue_length += 1
    queue_lengths.append(queue_length)

    start_service = max(arrival, last_departure)
    wait_times[i] = start_service - arrival
    last_departure = start_service + service_times[i]
    departure_times[i] = last_departure
    system_times[i] = last_departure - arrival

times_in_states[current_state] += last_departure - state_start_time

total_time = last_departure
for state in times_in_states:
    times_in_states[state] /= total_time

average_wait_time = wait_times.mean()
average_service_time = service_times.mean()
average_system_time = system_times.mean()
average_queue_length = np.array(queue_lengths).mean()

print("Доля времени в состояниях:")
for state, fraction in times_in_states.items():
    print(f"  {state}: {fraction:.4f}")
print(f"Сумма долей состояний: {sum(times_in_states.values()):.4f}")

print(f"\nСреднее время ожидания: {average_wait_time:.4f}")
print(f"Среднее время обслуживания: {average_service_time:.4f}")
print(f"Среднее время в системе: {average_system_time:.4f}")
print(f"Средняя длина очереди: {average_queue_length:.4f}")