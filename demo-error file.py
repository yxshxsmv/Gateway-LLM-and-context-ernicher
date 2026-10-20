
def demo_security_issues(user_input):
    import pickle
    import subprocess
    import yaml

    # Unsafe deserialization
    obj = pickle.loads(user_input)

    # Potentially unsafe YAML loading
    config = yaml.unsafe_load(user_input)

    # Shell command injection risk
    subprocess.run(user_input, shell=True)

    return config
