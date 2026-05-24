def save_to_file(filename, jobs):
    file = open(f"{filename}.csv", "w")
    file.write("position, company, link\n")

    for job in jobs:
        file.write(f"{job['position']}, {job['company']}, {job['link']}\n")
    file.close()