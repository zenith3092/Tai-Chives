import yaml

def read_yaml(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            config_yaml = yaml.load(file, Loader=yaml.FullLoader)
            return config_yaml
    except Exception as e:
        return e


def write_yaml(path, content, sort_keys=True):
    indicator = True
    message = 'Write to yaml successfully'
    try:
        with open(path, 'w') as file:
            yaml.dump(content, file, allow_unicode=True, sort_keys=sort_keys)
    except Exception as e:
        indicator = False
        message = str(e)
    return {"indicator": indicator, "message": message}

if __name__ == "__main__":
    EXAMPLE = read_yaml("example.yaml")
    print(EXAMPLE)

    EXAMPLE.update({"penguin": "Chia", "bad": "Fuchi"})
    write_yaml("example.yaml", EXAMPLE)

    EXAMPLE = read_yaml("example.yaml")
    print(EXAMPLE)