

def count_doctors_working_multiple_hospitals(A):
    doctor_counts = {}
    for hospital_schedule in A:
        for doctor_id in set(hospital_schedule):
            if doctor_id in doctor_counts:
                doctor_counts[doctor_id] += 1
            else:
                doctor_counts[doctor_id] = 1

    num_doctors_working_multiple_hospitals = sum(count > 1 for count in doctor_counts.values())

    return num_doctors_working_multiple_hospitals

# Example usage
A = [[1, 2, 2], [3, 1, 4]]
result = count_doctors_working_multiple_hospitals(A)
print( result)