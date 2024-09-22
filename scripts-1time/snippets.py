    print(">>> Loading the map guids ...")

    guids_json: str = f"{xx}_{yyyy}_{plan_type}_map_guids.json"
    guids_path: str = os.path.join(output_dir, guids_json)
    guids: dict[str, Any] = read_json(guids_path)
    

    # Pull the ratings for each map & write the ratings to a CSV

    print(">>> Pulling the ratings for each map ...")

    for label, guid in guids.items():
        if label in ["name", "ready"] or label.endswith("-intersections"):
            continue
        command = f"scripts/pull_map_ratings.py -s {xx} -l {label.capitalize()} -i {guid} -o {output_dir}"
        print(command)
        os.system(command)

    print(">>> Writing the ratings to a CSV file ...")

    command = f"scripts/write_ratings_table.py -s {xx} -o {output_dir}"
    print(command)
    os.system(command)