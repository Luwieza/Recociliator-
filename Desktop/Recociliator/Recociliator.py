import math
"""
  A tool used to calculate the tal number of rejected Arrays
  (lenses) per split.
"""
# update

# Ask user to input split number.
# Ask the user to confirm wether is working on the last split
# or not, by confirming 'yes' or 'no'.
# if 'Yes', calculate the following:
#     Ask the user to input the first carton number.
#     Ask the user to input the total number of lenses packed (EXCLUDING PARTIAL CASE).
#     AsK the user to input the total number of cartons inside a partial_case.
#     AsK the user to input QC samples.
#     Ask the user to assign all values to variables.
# Calculate total number of rejected arrays per split by using the following formulae:
#     partial_case = total_cartons * per_carton
#     total_rejects = total_lenses_packed - qc_sample + partial_case.   
# Use f"string" to display output as the following.
#     print(f"Total number of rejected lenses in split {split_number} is: . ")  
# if 'No', 

# Ask user to input split number.
split_number = int(input("Enter the split number: "))

# Ask the user to confirm split number, if working on the last split,
# confirm 'Yes' or 'No'.
confirm_split = input("Are you working on the last split? "
                      "Confirm, 'Yes' or 'No': ").strip().lower()

# If the user confirms 'yes'
if confirm_split == 'yes':

    # Ask for necessary inputs
    first_carton_no = int(input("Enter the first carton number: "))
    print("Hint: Use HMI to calculate total lenses to be packed!")
    lenses_to_pack = int(input("Enter the total number of lenses to be "
                               "packed: "))
    num_of_lenses_per_case = int(input("Enter the total number of lenses "
                                       "per case, excluding partial case: "))
    qc_sample = int(input("Enter QC samples: "))
    case_packed = int(input("Enter the total number of packed cases "
                            "excluding partial case: "))
    lenses_per_carton = int(input("Enter the number of lenses pe carton: ").strip())
    total_cartons_p = int(input("Enter the total number of cartons inside "
                                "partial case: "))

    # Validate input ranges.
    if qc_sample < 30:
        print("Invalid input: QC sample cannot be less than 30.")

    elif total_cartons_p <= 16:
        print("Invalid input: Total cartons in partial case must be "
              "between 16 and 100.")
        
    elif total_cartons_p <= 100:
        print("Invalid input: Total cartons in partial case must be "
              "between 16 and 100.")
        
        
    # Check if lenses_per_carton is 30 or 90
    elif lenses_per_carton not in [30, 90]:  # Check if lenses_per_carton is 30 or 90
        print("Invalid input: Lenses per carton must be either 30 or 90.")

    # Check if lenses_per_carton is 1440 or 3000
    elif num_of_lenses_per_case not in [1440, 3000]:  
        print("Invalid input: Lenses per carton must be either 1440 or 3000.")

    else:
        # Perform calculations.
        
        # Calculate partial case.
        partial_case = total_cartons_p * lenses_per_carton
        
        # Calculate sum of rejected products between partial_case and qc_sample.
        sum_rej = partial_case + qc_sample
        
        # Calculate the difference between lenses to pack and packed lenses.
        diff_rej = lenses_to_pack - (num_of_lenses_per_case * case_packed)
        
        # Calculate the total rejected lenses across the line.
        total_rejects = diff_rej - sum_rej
        
        # Check if total_rejects is correct
        check_answer = sum_rej + (num_of_lenses_per_case * case_packed) + total_rejects
        
        if check_answer == lenses_to_pack:
            print(f"Validation Passed: Total rejects calculation is correct. "
                  f"Lenses to pack: {lenses_to_pack}, Check Answer: {check_answer}")
        else:
            print(f"Validation Failed: Total rejects calculation is incorrect. "
                  f"Lenses to pack: {lenses_to_pack}, Check Answer: {check_answer}")
            
        print(f"Total number of rejected lenses in split {split_number} "
              f"is: {total_rejects} lenses.")


elif confirm_split == 'no':

     # Ask for necessary inputs
    first_carton_no = int(input("Enter the first carton number: "))
    print("Hint: Use HMI to calculate total lenses to be packed!")
    #lenses_to_pack = int(input("Enter the total number of lenses to be "
    #                           "packed: "))
    #num_of_lenses_per_case = int(input("Enter the total number of lenses "
    #                                   "per case, excluding partial case: "))
    qc_sample = int(input("Enter QC samples: "))
    #case_packed = int(input("Enter the total number of packed cases "
    #                        "excluding partial case: "))
    lenses_per_carton = int(input("Enter the number of lenses pe carton: ").strip())
    total_cartons_p = int(input("Enter the total number of cartons inside "
                                "partial case: "))
    
    # Constant values:
    
    # Total number of products to be packed.
    lenses_to_pack = 28000
    
    # total number of product packed.
    packed_lenses = 27000

    # Validate input ranges.
    if qc_sample < 30:
        print("Invalid input: QC sample cannot be less than 30.")
    
    
    # Check if total_cartons_p is between 1 and 16
    elif (total_cartons_p > 16):
        print("Invalid input: Total cartons must be between 1 and 16.")

    # Check if total_cartons_p is between 16 and 100
    elif not (total_cartons_p < 100):
        print("Invalid input: Total cartons in partial case must be between 16 and 100.")

        
    # Check if lenses_per_carton is 30 or 90
    elif lenses_per_carton not in [30, 90]:  # Check if lenses_per_carton is 30 or 90
        print("Invalid input: Lenses per carton must be either 30 or 90.")

    # Check if lenses_per_carton is 1440 or 3000
    # elif num_of_lenses_per_case not in [1440, 3000]:  
    #   print("Invalid input: Lenses per carton must be either 1440 or 3000.")

    else:
        # Perform calculations.
        
        # Calculate partial case.
        partial_case = total_cartons_p * lenses_per_carton
        
        # Calculate sum of rejected products between partial_case and qc_sample.
        sum_rej = partial_case + qc_sample
        
        # Calculate the difference between lenses to pack and packed lenses.
        diff_rej = lenses_to_pack - packed_lenses
        
        # Calculate the total rejected lenses across the line.
        total_rejects = diff_rej - sum_rej
        
        # Check if total_rejects is correct
        check_answer = sum_rej + total_rejects
        
        if check_answer == lenses_to_pack:
            print(f"Validation Passed: Total rejects calculation is correct. "
                  f"Lenses to pack: {lenses_to_pack}, Check Answer: {check_answer}")
        else:
            print(f"Validation Failed: Total rejects calculation is incorrect. "
                  f"Lenses to pack: {lenses_to_pack}, Check Answer: {check_answer}")
            
        print(f"Total number of rejected lenses in split {split_number} "
              f"is: {total_rejects} lenses.")