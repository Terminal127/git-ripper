with open("github_repositories.txt") as file:
    lines = file.readlines()[1:-1]  # Skip first and last lines

    first_columns = []
    for line in lines:
        words = line.split()
        if words:  # Check if there are any words in the line
            first_columns.append(words[0].strip())

    # Save the extracted first columns to a new file
    with open("repository_names.txt", "w") as outfile:
        outfile.write("\n".join(first_columns))
