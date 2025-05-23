from process import get_encounters, process, load_configs


def main():
    # download the images or not
    data = get_encounters()
    configs = load_configs("config.json")
    download = configs["download"]
    headers = {}
    headers["User-Agent"] = configs["User-Agent"]

    process(data, download, headers)


if __name__ == "__main__":
    main()
