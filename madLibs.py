mad_libs = {}
current_mad_lib = ""
# Read in the mad libs in the text file, remove the '#' marks from before the number
with open("./story.txt", "r") as f:
    for line in f:
        if line.startswith("###"):
            current_mad_lib = line.strip()[3:]
            mad_libs[current_mad_lib] = ""
        else:
            mad_libs[current_mad_lib] += line
# Print a list of the available mad libs
print("Available Mad Libs:")
for index, mad_lib in enumerate(mad_libs.keys(), start=1):
    print(f"{index}. {mad_lib}")
# Get input for which mad lib the user picks
while True:
    try:
        choice = int(input("Choose a Mad Lib (enter the corresponding number): "))
        if 1 <= choice <= len(mad_libs):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
# Save the selected mad lib to a new variable
selected_mad_lib = list(mad_libs.values())[choice - 1]

words = set()
start_of_word = -1
# Define what marks the input 
target_start = "<"
target_end = ">"
# Add the entire word to the words list
for i, char in enumerate(selected_mad_lib):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = selected_mad_lib[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
# Make list of answers and add answers to that list for the location of the mad lib input
answers = {}
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
# Replacemad lib input space with the answered input
for word in words:
    selected_mad_lib = selected_mad_lib.replace(word, answers[word])
# Print the mad lib
print("\n" + selected_mad_lib)
print("\nYour mad lib has been saved to to storiesGenerated.txt")
# Save the mad lib to a storiesGenerated.txt output file
with open("./storiesGenerated.txt", "a") as output_file:
    output_file.write("\nGenerated Mad Lib:\n")
    output_file.write(selected_mad_lib)
